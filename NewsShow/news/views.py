# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# news.page import PageInfo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import time
import sqlite3
import re
from .models import news
import jieba
import re

def search_form(request,pagenum):
	allnews = news.objects.all()
	pag = Paginator(allnews, 10)
	newslist = pag.page(pagenum)
	return render(request,'search_form.html',{'all_news':newslist})

def search(request,pagenum):
	q = request.GET['q']
	pattern = '(\d{4})-(\d{1,2})-(\d{1,2})'
	begin = '2015-09-15'
	endday = '2018-09-15'
	if 'begin' in request.GET:
		begin = request.GET['begin']
		res = re.search(pattern,begin)
		if res:
			year = res.group(1)
			yue = res.group(2)
			ri = res.group(3)
			if len(yue) == 1:
				yue = '0'+yue
			if len(ri) == 1:
				ri = '0'+ri
			begin = year+'-'+yue+'-'+ri
		else:
			begin = '2015-09-15'
	else: 
		begin = '2015-09-15'
	if 'end' in request.GET:
		endday = request.GET['end']
		res = re.search(pattern,endday)
		if res:
			year = res.group(1)
			yue = res.group(2)
			ri = res.group(3)
			if len(yue) == 1:
				yue = '0'+yue
			if len(ri) == 1:
				ri = '0'+ri
			endday = year+'-'+yue+'-'+ri
		else:
			endday = '2018-09-15'
	else: 
		endday = '2018-09-15'
	wordlist = list(jieba.cut(q))
	for word in wordlist:
		word = word.strip()
	allnews =[]
	start = time.clock()
	allnewstemp = news.objects.all()
	all_news = []
	for item in allnewstemp:
		if item.time >= begin and item.time <= endday:
			all_news.append(item)

	dictnum = {}
	if len(wordlist)>=3: 
		for word in wordlist:
			if len(word) == 1:
				wordlist.remove(word)

	if len(wordlist) == 1:
		for item in all_news:
			if q in item.title:
				allnews.append(item)
		for item in all_news:
			if q in item.body:
				allnews.append(item)
	else:		
		max = 0		
		for item in all_news:
			num = 0
			for word in wordlist:
				if word in item.title:
					num += 1
			if num > max : 
				max = num
			if dictnum.has_key(num):
				dictnum[num].append(item)
			else:
				dictnum[num]=[]
				dictnum[num].append(item)
		while max > 0:
			if dictnum.has_key(max):
				allnews.extend(dictnum[max])
			max -= 1
		max = 0
		dictnum = {}
		for item in all_news:
			num = 0
			for word in wordlist:
				if word in item.body:
					num += 1
			if num > max : 
				max = num
			if dictnum.has_key(num):
				dictnum[num].append(item)
			else:
				dictnum[num]=[]
				dictnum[num].append(item)
		while max > 0:
			if dictnum.has_key(max):
				for n in dictnum[max]:
					if n not in allnews:
						allnews.append(n)
			max -= 1
	endtime = time.clock()
	timing = endtime - start
	all_count =len(allnews)
	pag = Paginator(allnews, 10)	
	if pag.num_pages>10:
		page = int(pagenum)
		if page-5<1:
			pageRange=range(1,11)
		elif page+5>pag.num_pages:
			pageRange=range(page-5,pag.num_pages+1)
		else:
			pageRange=range(page-5,page+5)
	else:
		pageRange=pag.page_range
	newslist = pag.page(pagenum)
	return render(request,"search_result.html",{'begin':begin,'end':endday,'all_news':newslist,'time':timing,'word':q,'num':all_count,'keywl':wordlist,'range':pageRange})

def news_show(request,offset):
	try:
		index = int(offset)		
		con = sqlite3.connect('/Users/kingjames/Desktop/NewsShow/db.sqlite3')
		c = con.cursor()
		p = news.objects.get(id = index)
		#data = c.execute("SELECT title, time,author,body from news_news where id = index" )
		title = p.title
		title = title.replace("&nbsp;"," ")
		title = title.replace("&quot;",'"')
		time = p.time
		author = p.author
		tempbody = p.body
		tempbody = tempbody.replace("&nbsp;"," ")
		tempbody = tempbody.replace("&quot;",'"')
		body = tempbody.split('\n')
		temprec = p.recommend
		rec = temprec.split()
		
		p1 = news.objects.get(id = int(rec[0]))
		p2 = news.objects.get(id = int(rec[1]))
		p3 = news.objects.get(id = int(rec[2]))
		
		#return renddayer(request,'news_show.html',{'title':title})
		#return renddayer(request,"news_show.html",{'title':title,'time':time,'author':author,'body':body,'index':rec})
		return render(request,"news_show.html",{'title':title,'time':time,'author':author,'body':body,'first':p1,'second':p2,'third':p3})
	except ValueError:
		raise Http404()


# Create your views here.

