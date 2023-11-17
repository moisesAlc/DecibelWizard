from moviepy.video.io.VideoFileClip import VideoFileClip


def get_duration(clip_filepath: str):
    return str(VideoFileClip(clip_filepath).duration)
