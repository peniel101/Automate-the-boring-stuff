from this import d
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup



class PlaylistDownload:
    global url_list 

    def __init__(self, url, path) -> None:
        self.url = url
        self.path = path
        self.get_urls(self.url, self.path)


    def get_urls(self, url, path):
        service = Service(executable_path=path)
        driver = webdriver.Chrome(service=service)
        driver.get(url)
        content = driver.page_source.encode("utf-8").strip()
        soup = BeautifulSoup(content, "lmxl")
        print(soup.prettify)


url = "https://www.youtube.com/playlist?list=PLeo1K3hjS3uvCeTYTeyfe0-rN5r8zn9rw"
path = r"C:\Users\Peniel\Desktop\Programming projects\Autodownload\chromedriver.exe"
check = PlaylistDownload(url, path)

