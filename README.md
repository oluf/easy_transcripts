# Audio Transcription Tool

A speech transcription and diarization tool that uses [WhisperX](https://github.com/m-bain/whisperX) as a library, providing enhanced output capabilities for audio transcription.

## Overview

This tool leverages WhisperX's powerful API to provide convenient output formatting options. It transcribes audio files with speaker diarization and outputs the results in both JSON and text formats to make the transcriptions easily accessible for different use cases.

## Features

- **Accurate Speech Recognition**: Uses WhisperX's powerful ASR capabilities with word-level timestamps
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

2. Install WhisperX and other dependencies:
   ```
   pip install git+https://github.com/m-bain/whisperX.git
   ```

   Or if you have a requirements.txt file:
   ```
   pip install -r requirements.txt
   ```

   You can generate a requirements.txt file for your environment using:
   ```
   pip freeze > requirements.txt
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

## Dependencies

This project uses [WhisperX](https://github.com/m-bain/whisperX) as a library dependency. WhisperX is a powerful tool developed by Max Bain et al. that provides fast automatic speech recognition with word-level timestamps and speaker diarization.

If you're interested in the underlying technology, check out the WhisperX paper:
```
@article{bain2022whisperx,
  title={WhisperX: Time-Accurate Speech Transcription of Long-Form Audio},
  author={Bain, Max and Huh, Jaesung and Han, Tengda and Zisserman, Andrew},
  journal={INTERSPEECH 2023},
  year={2023}
}
```

## License

This project is licensed under the terms of the [MIT License](LICENSE), which allows for both personal and commercial use with minimal restrictions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 
