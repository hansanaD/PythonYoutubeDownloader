from y2mate_api import Handler
import os , sys
from tabulate import tabulate
# Custom Modules
from modules import banner, cmds

# Clear the previous output from the terminal.
cmds.clear()
# print Welcome Banner
banner.WelcomeBanner()

videoURL = str(input("Enter Video Link : "))

# Don't Enable if you're don't know what it does.
# videoURL = 'https://www.youtube.com/watch?v=mDTMBdYAjHI' 

cmds.clear()
banner.WelcomeBanner()
print("Looking for Available Qualities..")

api = Handler(videoURL)

q_list = ['4k', '1080p', '720p', '480p', '360p', '240p']
q_list.reverse()

urlList = {} 


def getVidInfo(r):
    for video_metadata in api.run(quality=r):
        
        quality = video_metadata.get("q")
        vidLink = video_metadata.get("dlink")
        
        if vidLink == None:
            pass
        else:
            urlList.update({quality : vidLink})
            # print(r, " fetched")
            
# Iterate over q_list to check if res quality exist on that video
for count, r in enumerate(q_list):
    getVidInfo(r)
        
# print qualities to the terminal
showList = {}
for count, q in enumerate(urlList, 1):
    showList.update({count: q})
    
print(tabulate(showList.items(), headers=["Q-No", "Quality"], tablefmt="heavy_grid"))


userInput = int(input("Enter the your Q-No: "))
cmds.clear()
print("Downloading...Please wait!")

mediaPath = f"{os.getcwd()}/vids"

# Download the video using user's input
for video_metadata in api.run(quality=showList[userInput]):
    # print(video_metadata)
     
    if not os.path.exists(mediaPath):
        os.makedirs(mediaPath)

    api.save(third_dict=video_metadata, dir="vids", progress_bar=True)

    vidFileName = f"{video_metadata["title"]} {video_metadata["vid"]}_{video_metadata["fquality"]}.{video_metadata["ftype"]}"
    print("Downloading:", vidFileName)
    # Delete your file automatically after it downloaded.
    # os.remove(f"{mediaPath}/{vidFileName}")



cmds.clear()
banner.WelcomeBanner()
print(f"\nPlease Check the 'vid' Folder for your files!\n")
print("Download Completed! ✅")

    

                                

