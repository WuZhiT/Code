# coding = utf-8
import scrapy  #导入scrapy
import re

#爬虫类
class SgyySpider(scrapy.Spider):
    name = 'sgyy' #爬虫名字
    allowed_domains = ['purepen.com']  #网站
    start_urls = ['http://www.purepen.com/sgyy/index.htm']   #第一次开始采集的网址

    #start_urls 采集的信息返回的内容
    def parse(self, response):
        #print(response.text) #打印爬虫文本内容
        detailURLs = re.findall('<TD><A HREF="(.*?)">', response.text)
        #构造完整的网址
        for url in detailURLs[:10]:
            url = f'http://www.purepen.com/sgyy/{url}'
            print(url)
            #发出请求 获取详情页信息
            yield scrapy.Request(url, callback=self.parsedetail)

    def parsedetail(self, response):
        #提取详情页
        text = re.findall('face="宋体" size="3">(.*?)</font>', response.text, flags=re.S)
        #print(text)
        title = re.findall('<title>(.*?)</title>', response.text, flags=re.S)
        #print(title)
        if text:
            self.savefile(title[0], text[0])

    @classmethod
    def savefile(cls, title, text):
        with open(f'{title}.txt', 'a', encoding='utf-8') as fp:
            fp.write(text)