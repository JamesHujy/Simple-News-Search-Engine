#encoding:utf-8
import re
import requests
import os

import jieba

index = 1

def solvetime(time):
	newtime = ""
	num = 0
	while num < 10:
		newtime = newtime + time[num]
		num = num+1
	return newtime


def solve(filename):
	filenametemp = '/Users/kingjames/Desktop/html3/'+filename
	f=open(filenametemp,'r')
	html = f.read()
	patterntitle = "<title>([^_|]*).*</title>"
	title = re.search(patterntitle,html)
	patternkeywords = '<meta name="keywords" content="([^"]*) '
	patterndescription = '<meta name="description" content="([^"]*)'
	patterntime = '<meta property="article:published_time" content="([^">]*)'
	publishtime = re.search(patterntime,html)
	keywords = re.search(patternkeywords,html)
	descriptions = re.search(patterndescription,html)
	patternauthor = '<meta property="article:author" content="([^">]*)'
	author = re.search(patternauthor,html)
	patternbody = '<p>([^<>]*)</p>'
	body = re.compile(patternbody).findall(html)
	filenametemp = '/Users/kingjames/Desktop/content3/'+filename
	file = open(filenametemp,"w")
	#del body[-1]
	#del body[-1]
	if title:
		file.write(title.group(1))
	file.write("\n")
	if publishtime:
		file.write(solvetime(publishtime.group(1)))
	file.write("\n")
	if author:
		file.write(author.group(1))
	file.write("\n")
	if keywords:
		file.write(keywords.group(1))
	file.write("\n")
	if descriptions:
		file.write(descriptions.group(1))
	file.write("\n")
	strdel = "更多猛料"
	strdel2 = "扫描二维码"
	strdel3 = "Copyright"
	strdel4 = "咨询"
	list_word = []
	for list in body:		
		if (strdel in list) or (strdel2 in list) or (strdel3 in list) or (strdel4 in list):
			continue
		templist = jieba.cut_for_search(list)
		list_word.extend(templist)
		file.write(list)
		file.write("\n")
	filenamewords ='/Users/kingjames/Desktop/breakwords2/'+filename
	fileword = open(filenamewords,"w")
	for item in list_word:
		fileword.write((item).encode('utf-8'))
		fileword.write(' ')
	fileword.close()
	file.close()


'''
print(title.group(1))
print(keywords.group(1))
print(publishtime.group(1))
print(author.group(1))
print(body)
'''

dirpath = "/Users/kingjames/Desktop/html3/"

#solve("html_financial1813.txt")

for filepath,dirnames,filenames in os.walk(dirpath):
	for file in filenames:
		if file[0] == 'h':
			print(file)
			solve(file)


