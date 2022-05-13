from bs4 import BeautifulSoup
import requests


class Parser:
    def __init__(self, word):
        self.word = word

    def get_html(self, url):
        resp = requests.get(url=url)
        if resp.status_code == 200:
            return resp.content
        else:
            return resp.status_code

    def get_link(self):
        src = self.get_html(url=f'https://surdo.me/vocabulary/vocabulary.html?gesture={self.word}')
        soup = BeautifulSoup(src, "lxml")
        video = soup.find("video")
        try:
            video_src = video.find("source").get('src')
            return 'https://surdo.me/' + video_src
        except:
            video_src = 'Жест не найден'
            return video_src



if __name__ == "__main__":
    pars = Parser('сто')
    print(pars.get_link())

