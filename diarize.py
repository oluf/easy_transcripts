import whisperx
import torch
import sys
import json
import os
from pathlib import Path

def transcribe_audio(audio_path):
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Load WhisperX model
    model = whisperx.load_model("large-v3", device, compute_type="float16")
    print("Model loaded successfully.")

    # Load audio
    audio = whisperx.load_audio(audio_path)
    print("Audio loaded successfully.")

    # Transcribe audio
    result = model.transcribe(audio)

    # Load alignment model for word timestamps
    model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
    aligned_segments = whisperx.align(result["segments"], model_a, metadata, audio, device)

    # Load Pyannote speaker diarization model
    diarization_model = whisperx.DiarizationPipeline(use_auth_token=True, device=device)
    diarized_result = diarization_model(audio_path)
    print("Diarized result:", diarized_result)

    # Assign speakers
    word_segments = whisperx.assign_word_speakers(diarized_result, aligned_segments)


    # ✅ Extract words from segments properly
    if isinstance(word_segments, dict) and "segments" in word_segments:
        word_segments = [
            word for segment in word_segments["segments"] if "words" in segment
            for word in segment["words"]
        ]

    # ✅ Ensure `word_segments` is a list before processing
    if not isinstance(word_segments, list):
        raise ValueError("word_segments is not a list! Check diarization output.")

    # ✅ Process word segments and build transcript
    transcript_json = []
    current_sentence = []
    for word in word_segments:
        if not isinstance(word, dict):
            print("Skipping malformed entry:", word)
            continue  # Avoid crashing on unexpected data

        if "start" not in word or "end" not in word or "word" not in word or "speaker" not in word:
            print("Skipping incomplete entry:", word)
            continue

        # Convert numpy.float64 to Python float
        start_time = float(word["start"])
        end_time = float(word["end"])

        current_sentence.append({
            "start_time": round(start_time, 2),
            "end_time": round(end_time, 2),
            "text": word["word"],
            "speaker": word["speaker"]
        })

        # Check for sentence-ending punctuation
        if word["word"].endswith(('.', '!', '?')):
            transcript_json.append({
                "start_time": current_sentence[0]["start_time"],
                "end_time": current_sentence[-1]["end_time"],
                "text": ' '.join([w["text"] for w in current_sentence]),
                "speaker": current_sentence[0]["speaker"]
            })
            current_sentence = []

    # Add any remaining words as the last sentence
    if current_sentence:
        transcript_json.append({
            "start_time": current_sentence[0]["start_time"],
            "end_time": current_sentence[-1]["end_time"],
            "text": ' '.join([w["text"] for w in current_sentence]),
            "speaker": current_sentence[0]["speaker"]
        })

    return transcript_json

def save_to_json(transcript, audio_path):
    """
    Save transcript to a JSON file in the outputs directory.
    
    Args:
        transcript: The transcript data to save
        audio_path: Path to the original audio file
    
    Returns:
        Path to the saved JSON file
    """
    # Create outputs directory if it doesn't exist
    os.makedirs("./outputs", exist_ok=True)
    
    # Generate output filename based on input audio filename
    output_file = os.path.join("./outputs", Path(audio_path).stem + ".json")
    
    # Save transcript to file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(transcript, f, indent=4)
    
    print(f"JSON transcript saved to {output_file}")
    return output_file

def save_to_text(transcript, audio_path):
    """
    Save transcript to a text file in the outputs directory,
    formatted the same way as in convert.py.
    
    Args:
        transcript: The transcript data to save
        audio_path: Path to the original audio file
    
    Returns:
        Path to the saved text file
    """
    # Create outputs directory if it doesn't exist
    os.makedirs("./outputs", exist_ok=True)
    
    # Generate output filename based on input audio filename
    output_file = os.path.join("./outputs", Path(audio_path).stem + ".txt")
    
    formatted_output = []
    
    for entry in transcript:
        speaker = entry["speaker"].replace("_", " ")  # Format speaker name
        text = entry["text"]
        
        formatted_output.append(f"{speaker}:\n{text}\n")
    
    # Save formatted transcript to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(formatted_output))
    
    print(f"Text transcript saved to {output_file}")
    return output_file

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python diarize.py <audio_file>")
        sys.exit(1)

    audio_file = sys.argv[1]

    if not Path(audio_file).exists():
        print(f"Error: File '{audio_file}' not found.")
        sys.exit(1)

    transcript = transcribe_audio(audio_file)
    
    # Save transcript to JSON and text files
    json_file = save_to_json(transcript, audio_file)
    text_file = save_to_text(transcript, audio_file)
    
    print(f"Transcription complete. Files saved to:")
    print(f"  - JSON: {json_file}")
    print(f"  - Text: {text_file}")