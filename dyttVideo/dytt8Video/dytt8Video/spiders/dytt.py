# _*_ coding = utf-8 _*_
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DyttSpider(CrawlSpider):
    name = 'dytt'
    allowed_domains = ['ygdy8.com']
    start_urls = ['https://www.ygdy8.com/index.html']

    #采集规则的集合
    rules = (
        # 具体实现的采集规则
        # 采集导航页中的电影部分，allow是选择出，allow是正则表达式，
        Rule(LinkExtractor(allow=r'index.html', deny='game')),
        #follow = True是下一次提取的网页中如果包含我们需要提取的信息，是否还要继续提取
        Rule(LinkExtractor(allow=r'list_\d+_\d+.html'), follow=True), #正则表达式中\d+代表数字，多个数字 ，\d代表0-9
        #allow=r''提取详情页信息，callback回调函数，将结果交给谁
        Rule(LinkExtractor(allow=r'/\d+/\d+.html'), callback='parse_item', follow=True),

    )

    #提取采集的数据
    def parse_item(self, response):
        #打印出导航页网址
        print(response.url)
        #提取下载链接
        download_url1 = re.findall(r'href="(.*?)"><strong>', response.text)
        download_url2 = re.findall(r'//div/span/table/tbody/tr/td/a', response.text)
        print(download_url1)
        print(download_url2)

        #保存
        # with open('url.txt', 'a') as fp:
        #     fp.write(download_url1, download_url2)