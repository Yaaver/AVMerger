import os
import itertools
from moviepy.editor import VideoFileClip, AudioFileClip

class AVMerger:
    def __init__(self, video_folder, audio_folder, output_folder):
        self.video_folder = video_folder
        self.audio_folder = audio_folder
        self.output_folder = output_folder

    def merge(self, num_files=None):
        # Check if the output folder exists, create it if not
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        video_files = self._get_video_files()
        audio_files = self._get_audio_files()

        if num_files is not None:
            video_files = video_files[:num_files]
            audio_files = audio_files[:num_files]
        
        print(f"Total number of video files: {len(video_files)}")
        print(f"Total number of audio files: {len(audio_files)}")
        print()

        for video_path, audio_path in zip(video_files, audio_files):
            try:
                video_clip = VideoFileClip(video_path)
                audio_clip = AudioFileClip(audio_path)
                audio_clip = self._adjust_audio_duration(video_clip, audio_clip)
                merged_clip = video_clip.set_audio(audio_clip)

                # Remove spaces from output file name
                output_filename = f"merged_{os.path.basename(video_path).replace(' ', '_')}"
                output_path = os.path.join(self.output_folder, output_filename)
                merged_clip.write_videofile(output_path, codec='libx264')

                print(f"Merged [{os.path.basename(video_path)}] with [{os.path.basename(audio_path)}] successfully.\nSaved to: {os.path.basename(output_path)}")

            except Exception as e:
                print(f"Failed to merge {video_path} with {audio_path}: {e}")

    def _get_video_files(self):
        video_files = []
        for filename in os.listdir(self.video_folder):
            if filename.endswith(".mp4"):
                video_files.append(os.path.join(self.video_folder, filename))
        return sorted(video_files)

    def _get_audio_files(self):
        audio_files = []
        for filename in os.listdir(self.audio_folder):
            if filename.endswith(".mp3"):
                audio_files.append(os.path.join(self.audio_folder, filename))
        num_audio_files = len(audio_files)
        num_video_files = len(self._get_video_files())
        # Repeat audio files to match the number of video files
        repeated_audio_files = audio_files * (num_video_files // num_audio_files) + audio_files[:num_video_files % num_audio_files]
        return repeated_audio_files

    def _adjust_audio_duration(self, video_clip, audio_clip):
        video_duration = video_clip.duration
        audio_duration = audio_clip.duration

        if audio_duration < video_duration:
            audio_clip = audio_clip.volumex(0)
            while audio_clip.duration < video_duration:
                audio_clip = audio_clip.append(audio_clip)
            audio_clip = audio_clip.subclip(0, video_duration)
        elif audio_duration > video_duration:
            audio_clip = audio_clip.subclip(0, video_duration)

        return audio_clip

if __name__ == "__main__":
    video_folder = r"E:\- YouTube Work\Channel - Factual Fusion Hub\to_be_uploaded"
    audio_folder = r"E:\- YouTube Work\Channel - Factual Fusion Hub\to_be_uploaded\audios"
    output_folder = r"E:\- YouTube Work\Channel - Factual Fusion Hub\to_be_uploaded\output"

    # Set test mode and specify the number of files to process
    test_mode = False
    # test_mode = True
    num_files_to_process = 3

    merger = AVMerger(video_folder, audio_folder, output_folder)
    merger.merge(num_files=num_files_to_process if test_mode else None)

