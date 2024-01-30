from yt_dlp import YoutubeDL

# with YoutubeDL() as ydl:
#     info_dict = ydl.extract_info('https://www.youtube.com/watch?v=BaW_jenozKc', download=False)
#     video_title = info_dict.get('title', None)
#     print(f"The title of the video is: {video_title}")

print(f" ==========================\n Python YouTube Downloader \n​==========================\n")

# videoURL = str(input("Enter Video Link : "))
videoURL = 'https://www.youtube.com/watch?v=HE7ViC-n25g'

with YoutubeDL() as ydl:
    vidInfo = ydl.extract_info(videoURL, download=False)

    print("\n- Title 👉", vidInfo.get('title', None))
    print("- Views 👉", vidInfo.get('view_count', None), "views")
    print("- Thubnail 👉", vidInfo.get('thumbnail', None))


