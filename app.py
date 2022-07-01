
url = "https://www.youtube.com/playlist?list=PLeo1K3hjS3uvCeTYTeyfe0-rN5r8zn9rw"
path = r"C:\Users\Peniel\Desktop\Programming projects\Autodownload\chromedriver.exe"

from tqdm import tqdm
from pytube import Playlist
from pytube import YouTube


class PlaylistDownloader:
    def __init__(self, url: str, resolution) -> None:
        self.url = url 
        self.resolution = resolution
        self.download_videos(self.url)

    def percent(self):
        pass

    def progress_bar(self, stream, chunk, file_handle, bytes_remaining):
        # get the size 
        # the 
        pass 

    def download_videos(self, url: str) -> None:
        playlist = Playlist(url = url)
        playlist_name = playlist.title
        length = len(playlist.video_urls)
        print(f"Downloading Playlist: {playlist_name} - {length} vidoes")
        

        for video_url in playlist.video_urls:
            yt_video = YouTube(video_url)
            stream = yt_video.streams.filter(resolution=self.resolution)
            filesize = yt_video.filesize

        for video in playlist.videos:
            titles = video.title
            print(titles)

    
# create folder and store the videos 
# {
# 8

# Call your progress function inside the Youtube class

# yt = YouTube(video_link, on_progress_callback=progress_function)

# This is your progress function

# def progress_function(self,stream, chunk,file_handle, bytes_remaining):

#     size = stream.filesize
#     p = 0
#     while p <= 100:
#         progress = p
#         print str(p)+'%'
#         p = percent(bytes_remaining, size)
# # 
#This computes the percentage converting the file size and the bytes remaining

# def percent(self, tem, total):
#         perc = (float(tem) / float(total)) * float(100)
#         return perc
# 
# }
