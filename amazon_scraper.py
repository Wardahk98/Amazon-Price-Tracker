from bs4 import BeautifulSoup
import requests

class AmazonScraper:
    def __init__(self, url):
        self.url = url
        self.header =  {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 "
                          "Safari/537.36",
            "Accepted-Language": "en-US",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.response = requests.get(url= self.url, headers=self.header)
        self.data = self.response.text
        self.soup = BeautifulSoup(self.data, "lxml")
        p_name = self.soup.title.string.split(": ")
        self.product_name = p_name[1]
        self.product_price = self.soup.find(class_="a-offscreen").string
        pass
