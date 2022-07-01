
url = "https://www.youtube.com/playlist?list=PLeo1K3hjS3uvCeTYTeyfe0-rN5r8zn9rw"
path = r"C:\Users\Peniel\Desktop\Programming projects\Autodownload\chromedriver.exe"


from pytube import Playlist

playlist = Playlist(url=url)
playlist_name = playlist.title
length = len(playlist.video_urls)
print(f"{playlist_name}= {length}")

for video_url in playlist.video_urls:
    #print(video_url)
    pass


for video in playlist.videos:
    titles = video.title
    print(titles)
# create folder and store the videos 
# 
