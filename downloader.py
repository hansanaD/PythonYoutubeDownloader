from yt_dlp import YoutubeDL

with YoutubeDL() as ydl:
    info_dict = ydl.extract_info('https://www.youtube.com/watch?v=BaW_jenozKc', download=False)
    video_title = info_dict.get('title', None)
    print(f"The title of the video is: {video_title}")
