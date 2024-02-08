from pytube import YouTube
import pathlib


print(f"===============================\n Python YouTube Downloader v2.0\n===============================\n")

# videoURL = str(input("Enter Video Link : "))
videoURL = 'https://www.youtube.com/watch?v=mDTMBdYAjHI'
# https://youtu.be/krsBRQbOPQ4?si=UKY-g36vKVM7Umqc : MrBeast Video

yt = YouTube(videoURL)


print("-------VIDEOS-------")

for count, stream in enumerate(yt.streams.filter(only_video=True, mime_type="video/mp4"), start=1):
    print(f"{count})  Res: {stream.resolution}  |  Size:{stream.filesize_mb} mb")
    # print(stream)

userInput = input(str("Enter Res: "))

for stream in yt.streams.filter(only_video=True, mime_type="video/mp4", res=userInput):
    stream.download(filename=f"{yt.title}.mp4", output_path=f"{pathlib.Path(__file__).parent.resolve()}/vids")
    print(userInput, ": MP4 Downloaded.✔")



print("-------AUDIOS-------")

for stream in yt.streams.filter(only_audio=True, abr="128kbps"):
    stream.download(filename=f"{yt.title}.mp3", output_path=f"{pathlib.Path(__file__).parent.resolve()}/vids")
    print(stream.abr,": MP3 Downloaded. ✔")

    
      



    

                                
