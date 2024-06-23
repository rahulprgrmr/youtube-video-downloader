from typing import Any
import ffmpeg

class FFMPEGProvider:

    @staticmethod
    def create_input_stream(file_path: str) -> Any:
        return ffmpeg.input(file_path)
    
    @staticmethod
    def combine_video_audio(video_path: str, audio_path: str, output_path: str, audio_codec: str, video_codec: str) -> None:
        video_stream = FFMPEGProvider.create_input_stream(video_path)
        audio_stream = FFMPEGProvider.create_input_stream(audio_path)
        video_ext = video_path.split('.').pop()
        audio_ext = audio_path.split('.').pop()
        if video_ext == 'webm' and audio_ext == 'webm':
            ffmpeg.output(audio_stream, video_stream, output_path, vcodec='copy', acodec='copy').run()
        else:
            ffmpeg.output(audio_stream, video_stream, output_path, vcodec='copy').run()