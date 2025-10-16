
from moviepy.video.io.VideoFileClip import VideoFileClip

cvt_video = VideoFileClip(r"C:\Users\HP\Desktop\VS_Code\python_projects\P5-EXTRACT_AUDIO_from_VIDEO_using_Python\Formal Introduction - Relax - Phrases ( lingoneo.org ).mp4")

ext_audio = cvt_video.audio

ext_audio.write_audiofile(r"C:\Users\HP\Desktop\VS_Code\python_projects\P5-EXTRACT_AUDIO_from_VIDEO_using_Python\audio_Extracted.mp3")

