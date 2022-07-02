from tqdm import tqdm
from pytube import Playlist, YouTube
import os 
from pytube.cli import on_progress


url = "https://www.youtube.com/playlist?list=PLeo1K3hjS3uvCeTYTeyfe0-rN5r8zn9rw"
path = r"C:\Users\Peniel\Desktop\Programming projects\Autodownload\chromedriver.exe"


class ytDownloader:
    def __init__(self, url, resolution="720p") -> None:
        self.url = url
        self.resolution = str(resolution)

    def download_video(self):
        video = YouTube(self.url, on_progress_callback=on_progress)
        stream = video.streams.filter(res=self.resolution)
        v_filesize = (stream.filesize) // 1000000
        title = video.title
        print(f'{title} - {v_filesize} MB')
        stream.download()

    def download_audio(self, ):
        audio = YouTube(self.url, on_progress_callback=on_progress)
        audio_streams = audio.streams.filter(only_audio=True).first()
        a_filesize = audio_streams.filesize
        print(f'{audio.title} with size of {a_filesize} MB')
        audio_streams.download()

    def download_playlist(self, video=True, audio=False):
        playlist = Playlist(self.url)
        playlist_name = playlist.title
        length = len(playlist.video_urls)
        print(f"Downloading Playlist: {playlist_name} contains {length} vidoes")

        for video_url in playlist.video_urls:
            yt_video = YouTube(video_url, on_progress_callback=on_progress)
            title = yt_video.title
            
            if video == True:
                stream = yt_video.streams.filter(res=self.resolution).first()
                video_filesize = (stream.filesize) // 1000000
                print(f'{title} with size of {video_filesize} MB')
                    # creating a folder to store the playlist videos 
                    # download_dir = r"C:\Users\Peniel\Desktop\Programming projects"
                    # current_dir = os.path.join(download_dir, playlist_name)
                    # path = os.makedirs(current_dir)                
                stream.download()
                    # add your own progress bar 
            # if you want to download the audio only 
            elif audio == True:
                audio_stream = yt_video.streams.filter(only_audio=True).first()
                audio_filesize = (audio_stream.filesize) // 1000000
                print(f'{title} with size of {audio_filesize} MB')
                audio_stream.download()

            # progress bar section using tqpm
        # what if the  use wants to download the audio of the playlist 
        
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
