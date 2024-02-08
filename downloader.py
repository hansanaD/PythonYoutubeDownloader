from pytube import YouTube
import os
from modules import vidmerge


print(f"===============================\n Python YouTube Downloader v2.0\n===============================\n")

videoURL = str(input("Enter Video Link : "))
# videoURL = 'https://www.youtube.com/watch?v=mDTMBdYAjHI'

yt = YouTube(videoURL)

mediaPath = f"{os.getcwd()}/vids"

# print("-------VIDEOS-------")
for count, stream in enumerate(yt.streams.filter(only_video=True, mime_type="video/mp4"), start=1):
    print(f"{count})  Res: {stream.resolution}  |  Size:{stream.filesize_mb} mb")
    # print(stream)

userInput = input(str("Enter Res: "))

for stream in yt.streams.filter(only_video=True, mime_type="video/mp4", res=userInput):
    stream.download(filename=f"{yt.title}.mp4", output_path=mediaPath)
    print(userInput, ": MP4 Downloaded.✔")



# print("-------AUDIOS-------")
for stream in yt.streams.filter(only_audio=True, abr="128kbps"):
    stream.download(filename=f"{yt.title}.mp3", output_path=mediaPath)
    print(stream.abr,": MP3 Downloaded. ✔")


# Merge the Audio & Video File 
vidmerge.merge(title=yt.title)

# Remove Seperate Media Files
os.remove(f"{mediaPath}/{yt.title}.mp4")
os.remove(f"{mediaPath}/{yt.title}.mp3")

print("Download Completed! ✔")

    

                                
