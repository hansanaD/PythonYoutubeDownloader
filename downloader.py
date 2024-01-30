from yt_dlp import YoutubeDL

# with YoutubeDL() as ydl:
#     info_dict = ydl.extract_info('https://www.youtube.com/watch?v=BaW_jenozKc', download=False)
#     video_title = info_dict.get('title', None)
#     print(f"The title of the video is: {video_title}")

print(f" ==========================\n Python YouTube Downloader \n​==========================\n")

# videoURL = str(input("Enter Video Link : "))
videoURL = 'https://www.youtube.com/watch?v=HE7ViC-n25g'

ydl_opts = {
    "quiet": True,
    'outtmpl': "%(title)s_%(id)s.%(ext)s"
}


with YoutubeDL( ydl_opts ) as ydl:
    vidInfo = ydl.extract_info(videoURL, download=False)

    print("\n🔹 Title:", vidInfo.get('title', None))
    print("🔹 Views:", vidInfo.get('view_count', None), "views")
    print("🔹 Size:", vidInfo.get('filesize', None))

    print("\n CHOOSE YOUR RESOLUTION \n--------------------------")

    for format in vidInfo['formats']:
        print(f"{format['format_id']} - {format['format']} - {format['ext']}")
                                       






# from yt_dlp import YoutubeDL

# ydl = YoutubeDL({'listformats': True})
# ytlink = "https://www.youtube.com/watch?v=HE7ViC-n25g"
# info = ydl.extract_info(ytlink, download=False)



# for format in info['formats']:
#     print(f"{format['format_id']} - {format['format']} - {format['ext']}")

# usrChosenFormat = str(input("Choose Format: "))

# ydl = YoutubeDL({'format': usrChosenFormat})
# ydl.download([ytlink])

#give a specific no to each specific format, so i can choose them in the userChosenFormat and download the exact format i want. also make the output more organized for better user experience.


# from yt_dlp import YoutubeDL

# ydl = YoutubeDL()
# ytlink = "https://www.youtube.com/watch?v=HE7ViC-n25g"
# info = ydl.extract_info(ytlink, download=False)

# # Print out a numbered list of available formats
# for i, format in enumerate(info['formats']):
#     print(f"{i+1}. {format['format_id']} - {format['format']} - {format['ext']}")

# # Get user input and validate it
# while True:
#     try:
#         usrChosenFormat = int(input("Choose Format: ")) - 1
#         if usrChosenFormat < 0 or usrChosenFormat >= len(info['formats']):
#             raise ValueError()
#         break
#     except ValueError:
#         print("Invalid input. Please enter a number corresponding to a format.")

# # Download the chosen format
# ydl = YoutubeDL({'format': info['formats'][usrChosenFormat]['format_id']})
# ydl.download([ytlink])

