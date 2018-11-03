# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class ThinkpadPipeline(object):
    def open_spider(self, spider):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', db='test', password='12345678',
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            sql = 'insert into xiaoshuo (title,caption,detail) VALUES (%s,%s,%s)'
            self.cursor.execute(sql, (item['book_title'], item['caption'], item['detail']))
            self.conn.commit()
            print('一条数据插入成功')
        except Exception as e:
            print(e)

        return item

    def close_spider(self, spider):
        print('close', spider)
