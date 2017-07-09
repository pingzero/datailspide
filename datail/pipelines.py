# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymysql
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

class DatailPipeline(ImagesPipeline):
    def file_path(self,request,response=None,info=None):
        image_guid=request.url.split('/')[-1]
        return 'full/%s' %(image_guid)
    def get_media_requests(self,item,info):
        self.con=pymysql.Connect(user='root',password='zero',db='tests',charset='UTF8')
        self.cu=self.con.cursor()
        title=item['title']
        url=item['url']
        img=item['img']
        imgs='/datail/images'+img.split('/')[-1]
        insert_sql='replace into datail (url,img,title) values(%s,%s,%s)'
        value=[url,imgs,title]
        titles_sql="select title from datail where title=%s"
        if  self.cu.execute(titles_sql,title) <=0:
            self.cu.execute(insert_sql,value)
            self.con.commit()
            yield Request(img)
    def item_completed(self,results,item,info):
        images_paths=[x['path'] for ok,x in results if ok]
        self.con.close()
        if not images_paths:
            raise DropItem('Item contains no images')
        return item
