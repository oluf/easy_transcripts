# Whisper Evaluation Tool

A speech transcription and diarization tool built on top of [WhisperX](https://github.com/m-bain/whisperX), providing enhanced output capabilities for audio transcription.

## Overview

This tool extends the functionality of WhisperX by adding convenient output formatting options. It transcribes audio files with speaker diarization and outputs the results in both JSON and text formats to make the transcriptions easily accessible for different use cases.

## Features

- **Accurate Speech Recognition**: Leverages WhisperX's powerful ASR capabilities with word-level timestamps
- **Speaker Diarization**: Identifies different speakers in the audio
- **Multiple Output Formats**:
  - JSON output with detailed information including timestamps and speaker labels
  - Human-readable text output formatted with clear speaker identification
- **Organized Output Storage**: All transcriptions are saved to an `./outputs` directory

## Installation

### Prerequisites

- Python 3.7+
- CUDA-compatible GPU (recommended for faster processing)

### Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/whisper_eval.git
   cd whisper_eval
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install WhisperX:
   ```
   pip install git+https://github.com/m-bain/whisperX.git
   ```

## Usage

### Basic Usage

```bash
python diarize.py <audio_file>
```

This will:
1. Transcribe the audio file using WhisperX
2. Perform speaker diarization
3. Save the results to:
   - `./outputs/<audio_filename>.json` (JSON format with detailed information)
   - `./outputs/<audio_filename>.txt` (Text format with speaker labels)

### Example

```bash
python diarize.py recordings/meeting.mp3
```

Output:
```
Model loaded successfully.
Audio loaded successfully.
Transcription result: ...
Aligned segments: ...
Diarized result: ...
Word segments after speaker assignment: ...
JSON transcript saved to ./outputs/meeting.json
Text transcript saved to ./outputs/meeting.txt
Transcription complete. Files saved to:
  - JSON: ./outputs/meeting.json
  - Text: ./outputs/meeting.txt
```

## Output Formats

### JSON Format

The JSON output contains detailed information including:
- Start and end timestamps for each segment
- Speaker identification
- Transcribed text

Example:
```json
[
  {
    "start_time": 0.5,
    "end_time": 4.2,
    "text": "Hello, welcome to the meeting.",
    "speaker": "SPEAKER_01"
  },
  {
    "start_time": 4.8,
    "end_time": 8.3,
    "text": "Thanks for having me. Let's discuss the project.",
    "speaker": "SPEAKER_02"
  }
]
```

### Text Format

The text output is formatted for easy reading:

```
SPEAKER 01:
Hello, welcome to the meeting.

SPEAKER 02:
Thanks for having me. Let's discuss the project.
```

## Acknowledgements

This project builds upon [WhisperX](https://github.com/m-bain/whisperX) by Max Bain et al., which provides fast automatic speech recognition with word-level timestamps and speaker diarization.

If you use WhisperX in your research, please cite:
```
@article{bain2022whisperx,
  title={WhisperX: Time-Accurate Speech Transcription of Long-Form Audio},
  author={Bain, Max and Huh, Jaesung and Han, Tengda and Zisserman, Andrew},
  journal={INTERSPEECH 2023},
  year={2023}
}
```

## License

This project is licensed under the terms of the [BSD-2-Clause license](https://github.com/m-bain/whisperX/blob/main/LICENSE), the same as WhisperX.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 