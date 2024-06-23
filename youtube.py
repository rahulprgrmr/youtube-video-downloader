from typing import Tuple
from pytube import YouTube, Stream
from ffmpeg_utils import FFMPEGProvider
import os

DOWNLOAD_PATH = "C:/Users/rahul/Downloads"

class YouTubeDownloader:
    url: str
    ytd: YouTube
    def __init__(self, url: str) -> None:
        self.url = url
        self.ytd = YouTube(self.url)

    def download_and_save(self) -> None:
        high_res_video_stream, high_res_audio_stream = self.__get_high_res_stream()
        print(high_res_video_stream.default_filename)
        high_res_video_stream.download(DOWNLOAD_PATH, f"temp_video.{high_res_video_stream.default_filename.split('.')[1]}")
        high_res_audio_stream.download(DOWNLOAD_PATH, f"temp_audio.{high_res_audio_stream.default_filename.split('.')[1]}")
        print(f"{high_res_audio_stream.audio_codec = }")
        print(f"{high_res_video_stream.video_codec = }")

        video_file = f"C:/Users/rahul/Downloads/temp_video.{high_res_video_stream.default_filename.split('.')[1]}"
        video_file = os.path.join(DOWNLOAD_PATH, f"temp_video.{high_res_video_stream.default_filename.split('.')[1]}")
        audio_file = f"C:/Users/rahul/Downloads/temp_audio.{high_res_audio_stream.default_filename.split('.')[1]}"
        audio_file = os.path.join(DOWNLOAD_PATH, f"temp_audio.{high_res_audio_stream.default_filename.split('.')[1]}")
        output_file = f"C:/Users/rahul/Downloads/out.{high_res_audio_stream.default_filename.split('.')[1]}"
        output_file = os.path.join(DOWNLOAD_PATH, high_res_video_stream.default_filename)

        FFMPEGProvider.combine_video_audio(video_file, audio_file, output_file, audio_codec=high_res_audio_stream, video_codec=high_res_video_stream.video_codec)

        if os.path.exists(video_file):
            os.remove(video_file)

        if os.path.exists(audio_file):
            os.remove(audio_file)

        # video_stream = ffmpeg.input(f"C:/Users/rahul/Downloads/temp_video.{high_res_video_stream.default_filename.split('.')[1]}")
        # audio_stream = ffmpeg.input(f"C:/Users/rahul/Downloads/temp_audio.{high_res_audio_stream.default_filename.split('.')[1]}")
        # ffmpeg.input(video_stream).output(audio_file, output_file, vcodec='copy', acodec='copy').run()
        # ffmpeg.output(audio_stream, video_stream, f"C:/Users/rahul/Downloads/out.{high_res_audio_stream.default_filename.split('.')[1]}", vcodec='copy', acodec='copy').run()



    def __get_high_res_stream(self) -> Tuple[Stream, Stream]:
        high_res_video_stream: Stream = self.ytd.streams.filter(adaptive=True).order_by('resolution').desc().first()
        high_res_audio_stream: Stream = self.ytd.streams.filter(only_audio=True).order_by('bitrate').desc().first()
        return high_res_video_stream, high_res_audio_stream