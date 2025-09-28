from bs4 import BeautifulSoup
import requests
import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

log = logging.info
url = "https://www.aljazeera.com/"
require = requests.get(url)
html = require.text


class LiveUpdates():
    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(html, "html.parser")
    
    def get_html(self):
        return self.html
    
    def time_news(self):
        times = self.soup.find_all("span", class_="liveblog-timeline__update-display-time")
        times_all = []
        for timing in times[:10]:
            times_all.append(timing.get_text())
        return times_all
    
    def name_news(self):
        names = self.soup.find_all("h4", class_="liveblog-timeline__update-content")
        names_all = []
        for naming in names[:10]:
                names_all.append(naming.get_text())
        return names_all 
        
    def actually(self):
        actualles = self.soup.find_all("strong", class_="post-label__text")
        for actually in actualles:
            actual = actually.get_text()
        return actual
        
def calls():
    object = LiveUpdates(html)
    log(f"\033[1m{object.actually()}\033[0m\n")
    for name, time in zip(object.name_news(), object.time_news()):
        log(f"{time} - {name}")

calls()
