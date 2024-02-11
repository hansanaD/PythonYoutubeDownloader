import pytube
import os , sys
from tabulate import tabulate

# Custom Modules
from modules import vidmerge, progressBar, banner

# print Welcome Banner
banner.WelcomeBanner()
videoURL = str(input("Enter Video Link : "))

# Don't Enable if you're don't know what it does.
# videoURL = 'https://www.youtube.com/watch?v=mDTMBdYAjHI' 

os.system('cls')
banner.WelcomeBanner()
print("Looking for Available Qualities..")


yt = pytube.YouTube(videoURL, on_progress_callback=progressBar.progress_hook)

streams = yt.streams.filter(only_video=True, mime_type="video/mp4")
streamsData = []

mediaPath = f"{os.getcwd()}/vids"

# -------VIDEOS-------

for count, stream in enumerate(streams, start=1):
    # print(f"{count}.  Res: {stream.resolution}  |  Size:{stream.filesize_mb} mb")
    # print(stream)
    streamsData.append([count, stream.resolution, stream.filesize_mb])

streamsDataTable = tabulate(streamsData, headers=["No", "Resolution", "Size (MB)"], tablefmt='rounded_outline')

# Clear the terminal
os.system('cls')

# Print the Table of Stream Data
print(streamsDataTable)

try:
    userInput = int(input("Enter the Res Number: ")) - 1
    streams[userInput].download(filename=f"{yt.title}.mp4", output_path=mediaPath)
    print("Video Downloaded. ✔")

except:
    print("Wrong Input! Try Again!")
    sys.exit()

# -------AUDIOS-------
    
for stream in yt.streams.filter(only_audio=True, abr="128kbps"):
    stream.download(filename=f"{yt.title}.mp3", output_path=mediaPath)
    print("Audio Downloaded. ✔")


videoID = pytube.extract.video_id(videoURL)
videoFileName = f"{yt.title}_{videoID}"

# Merge the Audio & Video File 
vidmerge.merge(title=f"{yt.title}", outVidTitle=videoFileName)

# Remove Seperate Media Files
os.remove(f"{mediaPath}/{yt.title}.mp4")
os.remove(f"{mediaPath}/{yt.title}.mp3")

os.system('cls')
banner.WelcomeBanner()
print("Download Completed! ✔")
print(f"\nCheck the 'vid' Folder for your files!\n")

    

                                

