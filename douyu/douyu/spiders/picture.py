import scrapy
import json
from douyu.items import DouyuItem


class PictureSpider(scrapy.Spider):
    name = 'picture'
    allowed_domains = ['douyu.com']
    basic_urls = 'https://m.douyu.com/api/room/list?page={}&type=yz'
    offset = 0
    start_urls = [basic_urls.format(offset)]

    def parse(self, response):
        #提取信息
        data_list = json.loads(response.body)['data']
        if len(data_list['list']) == 0:
            return
        for data in data_list['list']:
            item = DouyuItem()
            #print(item)
            item['nickname'] = data['nickname'].encode('utf-8')
            item['verticalSrc'] = data['verticalSrc']
            #print(item['nickname'])

            yield item

        self.offset += 1
        url = self.basic_urls.format(self.offset)
        print(url)

        yield scrapy.Request(url, callback=self.parse, dont_filter=True)