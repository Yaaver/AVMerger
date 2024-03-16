# AVMerger

AVMerger is a Python script for merging audio and video files written by Yawar Abbas Khokhar (Yaaver).

## Introduction

AVMerger is a tool designed to merge audio and video files seamlessly. It allows you to combine multiple video files with corresponding audio files, ensuring that the audio playback length matches the video playback length.

AVMerger is useful for tasks such as adding background music to video clips or merging recorded audio with video.

## Features

- Merges audio and video files into a single video file.
- Handles sequential naming of input video and audio files.
- Repeats audio files to match the length of video files.
- Maintains the aspect ratio of the original video files.
- Customizable input audio folder location.
- Customizable input video folder location.
- Customizable output folder location.
- Test mode for processing a specified number of files, before processing all files in the folder.

## Usage

1. Create AVMerger directory/folder:
    
    Linux:
    ```bash
    mkdir AVMerger
    ```
    
    Windows:
    ```bash
    Right click and create the folder :-P
    ```
2. Clone the repository:
    ```bash
    git clone https://github.com/Yaaver/AVMerger.git

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

4. Run the script:
    ```bash
    python main.py
