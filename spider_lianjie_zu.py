#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
	datetime:20170525
	author	:guotanxiang
	target	:最近租房爬了链家的租房信息，展示部分内容
'''

#记载所需库
import urllib2
import urllib
import re

class lianjia:
	def __init__(self):
		self.baseurl = 'https://bj.lianjia.com/zufang/'
	
	#get Content 
	def getContent(self,pageIndex):
		# comple url
		url = self.baseurl + 'pg' + str(pageIndex)
		# request url
		request = urllib2.Request(url)
		# response
		response = urllib2.urlopen(request)
		# get Content
		content = response.read()
		# print content
		return content
	
	#get Data	 
	def parserData(self,pageIndex):
		content = self.getContent(pageIndex)
		pattern = re.compile('<div.*?class="info-panel">.*?<h2>.*?<a.*?target="_blank".*?>(.*?)</a>.*?</h2>.*?<div.*?class="col-1">.*?<div.class="where"*?>.*?<a.*?href=".*?>.*?<span.*?class="region">(.*?)</span>.*?</div>.*?</div>.*?</div>',re.S)
		items = re.findall(pattern,content)
		for item in items:
			# title,户型，地点，楼层，建房日期，价格，看房人数
			print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
			print '租房标题：',item[0]
			print '小区名称：',item[1]
			print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

	#获取全量北京租房信息
	def getAll(self):

		# 应该有获取页数的函数，由于我懒，省去了>_<
		for pageIndex in range(1,100):
			print '当前页码是：',pageIndex
			self.parserData(pageIndex)

lj = lianjia()
lj.getAll()