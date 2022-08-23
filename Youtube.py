from pytube import Playlist

def playListDownloader(url,path,quality=360):
    playList = Playlist(url)
    counter = 0
    for video in playList.videos:
        video.streams.filter(res=f"{quality}p").first().download(path)
        counter += 1
    return counter

