from pytube import Playlist

def play_list_downloader(url,path,quality=360):
    play_list = Playlist(url)
    counter = 0
    for video in play_list.videos:
        video.streams.filter(res=f"{quality}p").first().download(path)
        counter += 1
    return counter

