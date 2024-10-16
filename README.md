<div align="center">
  <img height="100" src="censorship_logo.png"  />
  <h1>CENSORSHIP.PY</h1>
</div>

![Static Badge](https://img.shields.io/badge/open-source-green)
![Static Badge](https://img.shields.io/badge/version-0.16-blue)
![PyPI - Downloads](https://img.shields.io/pypi/dm/censorship-py)


Censorship Audio is a Python library that allows you to censor specific words in an audio file based on a given list of words. The library outputs a censored version of the input audio, replacing the specified words with a beep sound.

## Features

- **Audio Censorship:** Automatically censors a list of provided words in an audio file.
- **Text-to-Speech Integration:** Supports transcribing audio to text using [Faster-Whisper](https://github.com/guillaumekln/faster-whisper).
- **Customizable Word List:** You can easily add or modify the words you want to censor.



## Installation

```bash
pip install censorship-py
```

Make sure you have installed **ffmpeg** for audio processing.

Use this command if you have Linux or a subsystem (recommended)

```bash
sudo apt update && sudo apt install ffmpeg
```

Or install it on Windows using Chocolatey

```bash
choco install ffmpeg
```

## Usage

Here is an example of how to use the Censorship Audio library:

```python
from censorship import Censorship_Audio

if __name__ == "__main__":
    censorship = Censorship_Audio()  # Create an instance of the Censorship class
    censorship.censure_audio('audio_to_censure.mp3', 'censored_audio.mp3', ['word1', 'word2'])

    # Optional: Transcribe the censored audio to text
    audio_to_text = censorship.return_audio_text('censored_audio.mp3')
    print(audio_to_text)
```

## Changing Whisper Model Parameters
By default, Censorship Audio uses the large-v3 Whisper model with cpu as the device and int8 for the compute type. However, you can change these parameters based on your system's capabilities or model preferences.

You can check the differents types of models and parameter in the [faster-whisper documentation](https://github.com/guillaumekln/faster-whisper).

### Example

```python
# Create an instance with custom Whisper model parameters
# Run on GPU with FP16
censorship = Censorship_Audio(model_size='large-v2', device='"cuda"', compute_type='"float16"')
```

## Contributing

If you find a bug or have an idea for improvement, feel free to open an issue or submit a pull request. Contributions are always welcome!
