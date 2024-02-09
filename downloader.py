from pytube import YouTube
import os
from tabulate import tabulate

# Custom Modules
from modules import vidmerge


print(f"===============================\n Python YouTube Downloader v2.0\n===============================\n")

# videoURL = str(input("Enter Video Link : "))
print("\nLooking for Available Qualities..")
videoURL = 'https://www.youtube.com/watch?v=mDTMBdYAjHI'

yt = YouTube(videoURL)

mediaPath = f"{os.getcwd()}/vids"

streamsData = []

# print("-------VIDEOS-------")
for count, stream in enumerate(yt.streams.filter(only_video=True, mime_type="video/mp4"), start=1):
    # print(f"{count}.  Res: {stream.resolution}  |  Size:{stream.filesize_mb} mb")
    # print(stream)
    streamsData.append([count, stream.resolution, stream.filesize_mb])

streamsDataTable = tabulate(streamsData, headers=["No", "Resolution", "Size (MB)"], tablefmt='rounded_outline')
# Print the Table of Stream Data
print(streamsDataTable)

userInput = input(str("Enter the Res Number: "))

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

    

                                
