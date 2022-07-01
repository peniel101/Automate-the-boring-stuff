import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup



class PlaylistDownload:
    global url_list 

    def __init__(self, url: str, path: str) -> None:
        self.url = url
        self.path = path
        self.get_urls(self.url, self.path)


    def get_urls(self, url, path):
        service = Service(executable_path=path)
        driver = webdriver.Chrome(service=service)
        driver.get(url)
        content = driver.page_source.encode("utf-8").strip()
        playlist_name = driver.find_element_by_css_selector("#title > yt-formatted-string > a")
        print(f"Playlist Name{playlist_name}")
        driver.quit()
        
        soup = BeautifulSoup(content, 'lxml')
        # articles = soup.find_all("div", {"class": "views-row"})
        playlist = soup.find("div", {'class': "style-scope ytd-playlist-video-renderer"})
        playlists = soup.find_all("ytd-playlist-video-renderer", {"class" : "style-scope ytd-playlist-video-list-renderer"})
        #a_tags = playlist.find_all("a")
        #print(len(a_tags))
        playlist_soup = BeautifulSoup(playlists, "lxml")
        tags =  playlist_soup.find_all("a")
        print(tags)

url = "https://www.youtube.com/playlist?list=PLeo1K3hjS3uvCeTYTeyfe0-rN5r8zn9rw"
path = r"C:\Users\Peniel\Desktop\Programming projects\Autodownload\chromedriver.exe"
# res = requests.get(url = url)
PlaylistDownload(url=url, path=path)
# print(res)

