import scrapy
import re

def remove_tag(content):
   cleanr =re.compile('<.*?>')
   content =content.replace("\n", " ")
   cleantext = re.sub(cleanr, '', content)
   return cleantext 

f=open('crawling.txt', 'w', encoding='utf-8')

class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    start_urls = ['https://music.bugs.co.kr/chart']

    def parse(self, response):
        for i in range (1,101):
            song_rank = remove_tag(response.css(f"#CHARTrealtime > table > tbody > tr:nth-child({i}) > td:nth-child(4) > div > strong").get())
            title = remove_tag(response.css(f"#CHARTrealtime > table > tbody > tr:nth-child({i}) > th > p > a").get())
            artist = remove_tag(response.css(f"#CHARTrealtime > table > tbody > tr:nth-child({i}) > td:nth-child(8) > p > a").get())
            album_name = remove_tag(response.css(f"#CHARTrealtime > table > tbody > tr:nth-child({i}) > td:nth-child(9) > a").get())

            f.write("순위 : " + song_rank + "\n")
            f.write("제목 : " + title + "\n")
            f.write("아티스트 : " + artist + "\n")
            f.write("앨범 이름 : " + album_name + "\n\n")  
        pass
