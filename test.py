import yt_dlp


def download_loading_bar(d):
    if d['status'] == 'downloading':
        # Get the download percentage as a float
        percentage = float(d['_percent_str'].replace('%', ''))
        # Calculate how many # symbols to print
        num_symbols = int(percentage / 5)
        # Print the loading bar with the percentage and ETA, using \r and end=''
        print(f"\rLoading: [{'#' * num_symbols}{'-' * (20 - num_symbols)}] {d['_percent_str']} {d['_eta_str']}", end='')


ydl_opts = {
    'progress_hooks': [download_loading_bar],
    'no_color': True,
}


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BxUS1K7xu30'])
