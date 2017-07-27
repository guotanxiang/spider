#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
datetime:20170525
author	:guotanxiang
target	:抓取链家租房信息
'''
# 记载所需库
import urllib2
import urllib
import re
# 创建类
class lianjia:
	def __init__(self):
		# https://bj.lianjia.com/zufang/pg1/
		self.baseurl = 'https://bj.lianjia.com/zufang/'
	
	#获取全部内容 
	def getContent(self,pageIndex):
		# url
		url = self.baseurl + 'pg' + str(pageIndex)
		# print url
		# request url
		request = urllib2.Request(url)
		# 获取响应
		response = urllib2.urlopen(request)
		# Content
		content = response.read()
		# print content
		return content
	
	#获取需要的数据	 
	def parserData(self,pageIndex):
		# content 
		content = self.getContent(pageIndex)
		pattern = re.compile('<div.*?class="info-panel">.*?<h2>.*?<a.*?target="_blank".*?>(.*?)</a>.*?</h2>.*?<div.*?class="col-1">.*?<div.class="where"*?>.*?<a.*?href=".*?>.*?<span.*?class="region">(.*?)</span>.*?</div>.*?</div>.*?</div>',re.S)
		items = re.findall(pattern,content)
		for item in items:
			# title,户型，地点，楼层，建房日期，价格，看房人数
			print '租房标题：',item[0]
			print '小区名称：',item[1]
			print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

	#获取全量北京租房信息
	def getAll(self):

		# 便利所有网页
		for pageIndex in range(1,100):
			print '当前页码是：',pageIndex
			self.parserData(pageIndex)

lj = lianjia()
lj.getAll()