from yt_dlp import YoutubeDL


print(f" ==========================\n Python YouTube Downloader \n​==========================\n")

videoURL = str(input("Enter Video Link : "))
# videoURL = 'https://www.youtube.com/watch?v=5cCaU6T1yFE'

# Progress bar shows when a video is downloading
def download_loading_bar(d):
    if d['status'] == 'downloading':
        # Get the download percentage as a float
        percentage = float(d['_percent_str'].replace('%', ''))
        # Calculate how many # symbols to print
        num_symbols = int(percentage / 5)
        # Print the loading bar with the percentage and ETA, using \r and end=''
        print(f"\rLoading: [{'#' * num_symbols}{'-' * (20 - num_symbols)}] {d['_percent_str']} {d['_eta_str']}", end='')

        
ydl_opts = {
    "quiet": True,
    'outtmpl': "%(title)s_%(id)s.%(ext)s",

    'progress_hooks': [download_loading_bar],
    'no_color': True,
}

print("Fetching the info...")

with YoutubeDL( ydl_opts ) as ydl:
    vidInfo = ydl.extract_info(videoURL, download=False)

    vidTitle = vidInfo.get('title', None)
    vidDuration = vidInfo.get('duration', None)
    vidSize = vidInfo.get('filesize_approx', None) // 1048576

    print("\n🔹 Title:", vidTitle)
    print("🔹 Duration:", vidDuration)
    print("🔹 Size:", vidSize , "MB")

print("\nDownloading...")

ydl.download(['https://www.youtube.com/watch?v=BxUS1K7xu30'])

print("Downloaded Successfully! \n ")


    

                                
