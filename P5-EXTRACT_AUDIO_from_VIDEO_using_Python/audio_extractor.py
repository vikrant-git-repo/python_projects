#moviepy - pip install moviepy

from moviepy.editor import VideoFileClip

cvt_video = VideoFileClip(r"C:\Users\ah85745\OneDrive - Elevance Health\Desktop\VS Code Folders\python_projects\EXTRACT_AUDIO_from_VIDEO_using_Python\Formal Introduction - Relax - Phrases ( lingoneo.org ).mp4")

ext_audio = cvt_video.audio

ext_audio.write_audiofile(r"C:\Users\ah85745\OneDrive - Elevance Health\Desktop\VS Code Folders\python_projects\EXTRACT_AUDIO_from_VIDEO_using_Python\audio_Extracted.mp3")

