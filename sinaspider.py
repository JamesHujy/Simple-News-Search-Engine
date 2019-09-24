import requests
import re
import time

filename = "/Users/kingjames/Desktop/html2/"



htmlset = set()
for line in open(filename+"url.txt","r"):
	urls = line.strip()
	htmlset.add(urls)

filename = "/Users/kingjames/Desktop/html3/"
f = open(filename+"url.txt","w")

index = 0
def newsparser(website,pattern,type):	
	global index
	response  = requests.get(website)
	response.encoding = 'utf-8'
	html = response.text
	res = re.compile(pattern).findall(html)	
	for url in res:		
		if url in htmlset:
			continue
		htmlset.add(url)
		index = index+1
		fh = open(filename+"html_"+str(index)+".txt","w")
		news = requests.get(url)
		news.encoding = "utf-8"
		fh.writelines(news)
		f.write(str(index))	
		f.write(":"+url)
		f.write("\n")
		fh.close()
		time.sleep(0.5)
	

#politics
website1 = "https://news.sina.com.cn/world/"
website2 = "https://news.sina.com.cn/china/"
pattern1 = "http://news\.sina\.com\.cn/./\d{4}-\d{2}-\d{2}/doc-\w*\.shtml"

newsparser(website1,pattern1,"interpolitics")

newsparser(website2,pattern1,"nationalpolitics")

#sports
website3 = "http://sports.sina.com.cn/"
pattern2 = "http://sports\.sina\.com\.cn/\S*/doc-\w*\.shtml"

newsparser(website3,pattern2,"sports")

#entertament
website4 = "http://ent.sina.com.cn/"
pattern3 = "http://ent\.sina\.com\.cn/[^(video)]*/doc-\w*\.shtml"
newsparser(website4,pattern3,"entertament")

#mulitary
website5 = "https://mil.news.sina.com.cn/"
pattern4 = "http://mil\.sina\.com\.cn/\S*/doc-\w*\.shtml"
newsparser(website5,pattern4,"mulitary")

#financial
website6 = "https://finance.sina.com.cn/"
pattern5 = "http://finance\.sina\.com\.cn/\S*/doc-\w*\.shtml"
newsparser(website6,pattern5,"financial")

#tech
website6 = "https://tech.sina.com.cn/"
pattern5 = "http://tech\.sina\.com\.cn/[^(photo)]*/doc-\w*\.shtml"
newsparser(website6,pattern5,"tech")


f.close()
