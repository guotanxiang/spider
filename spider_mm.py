#!/usr/bin/python
# -*- coding: utf-8 -*-
''' 
	author		: guotanxiang
	datetime	: 20170525
	dec		: 爬去想看的图片	
'''
# 加载所需库
import re
import urllib2
import urllib
import os
import random
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')
# 创建类
class MM:
	def __init__(self):
		self.baseUrl = 'http://www.mm131.com/xinggan/'

	def getName(self,indexPage):
		# url
		url = self.baseUrl + 'list_6_' + str(indexPage) + '.html'
		# request
		request = urllib2.Request(url)
		# response
		content = urllib2.urlopen(request).read()
		return content

	def getUrl(self,indexPage):
		# content
		content = self.getName(indexPage)
		# 正则表达式
		pattern = re.compile('<a.*?target="_blank".*?href="(http://www.mm131.com/xinggan.*?)">.*?<img.*?src="http://img1.mm131.com/pic/.*?>(.*?)</a>',re.S)
		# 匹配名字列表
		items = re.findall(pattern,content)
		# 遍历出名字和链接
		for item in items:
			print 'name is : ',item[1].decode('gbk')
			print 'href is : ',item[0]
			url = item[0]
			self.getImage(url)
	'''
		下载每个主题下的图片 
	'''
	# 目录是否存在
	def mkdir(self,filename):
		# 检验是否存在filename目录
		isExists = os.path.exists(filename)	
		if not isExists:
			os.mkdir(filename)
		else:
			print '存在此目录'
			
	# 获取主题
	def getImage(self,url):

		#url  url = item[0][0:-5]+'_'+str(page)+'.html'
		
		#request
		request = urllib2.Request(url)
		#response
		response = urllib2.urlopen(request)
		# content
		content = response.read()
		# 正则表达式
		pattern = re.compile('<h5>(.*?)</h5>.*?<div class="content-pic">.*?<img.*?src="(.*?)" />.*?</div>.*?<div class="content-page">.*?<span class="page-ch">(.*?)</span>.*?</div>',re.S)
		# 匹配
		items = re.findall(pattern,content)
		# item
		for item in items:
			# 获取主题（名字）
			print '主题是 ：',item[0]
			# 获取url
			print 'url is  : ',item[1]
			# 获取页码
			print 'pageNum is : ',item[2][2:4]

			filename 	= item[0].decode('gbk')
			self.mkdir(filename)
			url 		= item[1]
			endPage 	= int(item[2][2:4])
			print filename,url,endPage
			self.saveImage(filename,url,endPage)

	def saveImage(self,filename,url,endPage):
		'''
			#getUrl		: http://www.mm131.com/xinggan/2745.html
			#updateUrl	: http://www.mm131.com/xinggan/2745_2.html
			# http://img1.mm131.com/pic/2745/2.jpg
		'''
		# 遍历此主题的全部图片
		for num in range(1,endPage):
			# pulic url
			baseUrl = url.split('/')[0] + '//' + url.split('/')[2] + '/' + url.split('/')[3] + '/' + url.split('/')[4] + '/'
			# url
			url = baseUrl + str(num) + '.jpg'
			print 'url is : ',url
			# request
			request = urllib2.Request(url)
			# response
			response = urllib2.urlopen(request)
			#data
			data = response.read()
			#filename
			f = filename + '/' + str(num)+'.jpg' 
			# open file
			f = open(f,'wb')
			# write file
			f.write(data)
			# close file
			f.close()
			print 'save Image~'
mm = MM()
# 爬取那一页里的图片
page = int(raw_input('page is:'))
mm.getUrl(page)
