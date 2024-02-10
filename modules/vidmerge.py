
import os
from moviepy.editor import VideoFileClip, AudioFileClip

def merge(title, outVidTitle):

    input_video = os.path.join(os.getcwd(), "vids",f"{title}.mp4")  
    input_audio = os.path.join(os.getcwd(), "vids",f"{title}.mp3")  

    # Load the video and audio clips
    video_clip = VideoFileClip(input_video)
    audio_clip = AudioFileClip(input_audio)

    # Combine them
    final_clip = video_clip.set_audio(audio_clip)

    # Write the final clip to a new file
    final_clip.write_videofile(f"vids/{outVidTitle}.mp4", codec="libx264")









