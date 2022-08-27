from pytube import Playlist


def play_list_downloader(url: str, path: str, quality: int = 480):
    """
    Download all videos of a youtube playlist

    params:
        url (str) : youtube link\n
        path (str) : The directory that downloaded videos will be saved there\n
        quality (int) [optional] : quality of videos (default = 480)

    Return:
        Number of downloaded videos
    """
    play_list = Playlist(url)
    counter = 0
    for video in play_list.videos:
        video.streams.filter(res=f"{quality}p").first().download(path)
        counter += 1
    return counter
