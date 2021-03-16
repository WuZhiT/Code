# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_link = item['verticalSrc']
        yield scrapy.Request(image_link)

    def item_completed(self, results, item, info):
        path = 'E:/WorkSpace/Code/douyu/picture/'
        print('*'*20)
        print(results)

        if results[0][0] == True:
            os.rename(path + results[0][1]['path'], path + str((item['nickname']).decode() + '.jpg'))