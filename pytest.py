# -*- coding: utf-8 -*-
import scrapy


class WdjSpider(scrapy.Spider):
    name = 'wdj'
    allowed_domains = ['wandoujia.com']

    def start_request(self):
        base_url = "http://www.wandoujia.com/apps/com{}"
        # with open("../packageList", "r", encoding="utf-8") as f:
        #     list = f.readlines()
        list = [".taobao.taobao"]
        for i, data in enumerate(list):
            # data = data.strip()
            # if i > 2:
            #     break
            scrapy.Request(
                url=base_url.format(data),
                callback=self.parse,
            )

    def parse(self, response):
        appName = response.xpath('//p[@class="app-name"]/span').extract_first()
        remark = response.xpath("//div[@class='editorComment']/div").extract()
        span_msg = response.xpath("//div[@class='num-list']/span/i").extract()
        # TODO
            # span_msg = install_msg + Feedback_rate
        commnet_cnt = response.xpath("//div[@class='num-list']/div//i").extarct_first()
        size = response.xpath().extract_first("//div[@class='col-right']/div/dl/dd/meta/@content").extract_first()
        firstClass=response.xpath("//div[@class='col-right']/div/dl/dd['tag-box']/a/text()").extract()
        tag = response.xpath("//div[@class='col-right']/div[@class='infos']/dl/dd[3]/div/div/a/text()").extract()
        company = response.xpath("//span[@class='dev-sites']/text()").extract_first()
        descripation = response.xpath("//div[@class='desc-info']/div[@itemprop='description']/p//text()").extarct()
        msg_update = response.xpath("//div[@class='change-info']/div/text()").extract()
        print(appName,remark,span_msg,commnet_cnt,size,firstClass,tag,company,descripation,msg_update)