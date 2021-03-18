import scrapy
import re
import requests


class GifSpider(scrapy.Spider):
    name = 'gif'
    allowed_domains = ['doutula.com']
    start_urls = [f'https://www.doutula.com/photo/list/?page={page}' for page in range(1, 5)]

    def parse(self, response):
        # 提取数据，即该处提取图片链接
        gif_urls = re.findall(r'data-original="(.*?)"', response.text, flags=re.S)
        #print(gif_urls)
        for url in gif_urls:
            self.getPicture(url=url)

    def getPicture(self, url):
        response = requests.get(url)
        picturePath = url.split('/')[-1]
        with open('doutu/doutupicture/' + picturePath, 'wb') as fp:
            fp.write(response.content)