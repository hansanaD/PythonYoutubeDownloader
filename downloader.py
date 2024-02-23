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
# q_list.reverse()

urlList = []


def getVidInfo(r):
    for video_metadata in api.run(quality=r):
        
        q = video_metadata.get("q")
        dlink = video_metadata.get("dlink")
        size = video_metadata.get("size")
        
        if dlink == None:
            pass
        else:
            urlList.append([q, size,dlink])
            # print(r, " fetched")
            


# Iterate over q_list to check if res quality exist on that video
for r in q_list:
    getVidInfo(r)

# print(urlList)

# Create a new list to show
showList = {}
for count, item in enumerate(urlList, 1):
    del item[2] # Remove dlink from list
    q = item[0]
    # print(i)
    size = item[1] 
    showList.update( { count: { "q":q, "size": size }} )

# print(showList)

def showQTable():
    tableList = []
    for count, item in enumerate(showList, 1):
        q = showList[item]["q"]
        size = showList[item]["size"]
        tableList.append( [count, q, size ] )
    print(tabulate(tableList, headers=["Q-No", "Quality", "Size"], tablefmt="heavy_grid"))

showQTable()





try:
    userInput = int(input("Enter the your Q-No: "))
    cmds.clear()
    banner.WelcomeBanner()
    print("Downloading...Please wait!\n")
except:
    print("Wrong Input try again!")

mediaPath = f"{os.getcwd()}/vids"

# Download the video using user's input
for video_metadata in api.run(quality=showList[userInput]["q"]):
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
print(f"Download Completed:\n{vidFileName} ✅")
print(f"\nPlease Check the 'vid' Folder for your files!\n")

    

                                

