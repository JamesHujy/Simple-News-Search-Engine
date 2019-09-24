#encoding:utf-8
from django.core.paginator import Paginator,Page

class PageInfo(object):
	"""docstring for PaegInfo"""
	def __init__(self, current_page, all_count,base_url,per_page=10,show_page=11):
		try:
			self.current_page = int(current_page)
		except Exception as e:
			self.current_page = 1

		a,b = divmod(all_count,per_page)
		if b:
			a+=1
		self.all_page = a
		self.base_url = base_url
		self.per_page = per_page
		self.show_page = show_page

	def start_data(self):
		return (self.current_page - 1)*self.per_page

	def end_data(self):
		return self.current_page * self.per_page

	def pager(self):
		page_list = []
		half = int((self.show_page - 1)/2)
		if self.all_page < self.show_page:
			start_page = 1
			end_page = self.all_page + 1
		else:
			if self.current_page + half > self.all_page:
				end_page = self.all_page + 1
				start_page = end_page - self.show_page
			else:
				start_page = self.current_page - half
				end_page = self.current_page + half + 1
		first_page = "<li><a href='%s?page=%s'>首页</a></li>"%(self.base_url,1)
		page_list.append(first_page)


		if self.current_page <= 1:
			prev_page = "<li><a href='#'>上一页</a></li>"
		else:
			prev_page = "<li><a href='%s?page=%s'>上一页</a></li>"%(self.base_url,self.current_page- 1)
		page_list.append(prev_page)

		for i in range(start_page,end_page):
			if i == self.cerrent_page:
				temp = "<li class='active'><a href='%s?page=%s'>%s</a></li>"%(self.base_url,i,i)
			else:
				temp = "<li><a href='%s?page=%s'>%s</a></li>"%(self.base_url,i,i)
			page_list.append(temp)

		if self.current_page >= self.all_page:
			next_page = "<li><a href='#'>下一页</a></li>"
		else:
			next_page = "<li><a href='%s?page=%s'>下一页</a></li>"%(self.base_url,self.current_page+1)
		page_list.append(next_page)

		if self.all_page > 1:
			last_page = "<li><a href='%s?page=%s'>末页</a></li>" % (self.base_url, self.all_page)
			page_list.append(last_page)
		return ' '.join(page_list)

		















