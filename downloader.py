from yt_dlp import YoutubeDL


print(f" ==========================\n Python YouTube Downloader \n​==========================\n")

# videoURL = str(input("Enter Video Link : "))
videoURL = 'https://www.youtube.com/watch?v=5cCaU6T1yFE'

ydl_opts = {
    "quiet": True,
    'outtmpl': "%(title)s_%(id)s.%(ext)s"
}

print("Fetching the info...")

with YoutubeDL( ydl_opts ) as ydl:
    vidInfo = ydl.extract_info(videoURL, download=False)

    print("\n🔹 Title:", vidInfo.get('title', None))
    print("🔹 Duration:", vidInfo.get('duration', None))
    print("🔹 Size:", vidInfo.get('filesize_approx', None) // 1048576, "MB")

print("Downloading...")

ydl.download(videoURL)

print("Video is Downloaded Successfully!")


    

                                          
    # usrChosenFormat = input("Enter Your Format number: ")

    # ydl = YoutubeDL({'format': usrChosenFormat})
    # ydl.download([videoURL])
