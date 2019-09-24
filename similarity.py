import jieba
from gensim import corpora,models,similarities
import os
#encoding:utf-8
all_doc = []
dictfile = {}
dirpath = "/Users/kingjames/Desktop/content3/html_"

for i in range(1,3569):
	f = open(dirpath+str(i)+'.html','r')
	line = f.readline()
	line = f.readline()
	line = f.readline()
	line = f.readline()
	line = f.readline()
	body = f.readline()
	dictfile[i] = file
	
	all_doc.append(body)

all_doc_list = []
for doc in all_doc:
	doc_list = [word for word in jieba.cut(doc)]
	all_doc_list.append(doc_list)

dictionary = corpora.Dictionary(all_doc_list)
dictionary.save('./dict.txt')
corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
tfidf = models.TfidfModel(corpus)
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.token2id.keys()))

def findsimilatity(doc_text):
	global index
	global tfidf
	doc_test_list = [word for word in jieba.cut(doc_text)]	
	doc_text_vec = dictionary.doc2bow(doc_test_list)	
	sim=index[tfidf[doc_text_vec]]
	anss = sim.tolist()
	ansdict={}
	llindex = 1
	for item in anss:
		ansdict[llindex] = item
		llindex+=1
	res=sorted(ansdict.items(),key = lambda item: item[1],reverse =True)
	return res
	#return str(res[1][0])+' '+str(res[2][0])+' '+str(res[3][0])
	#sorted(anss.items(),key = lambda item: item[1],reverse =True)

ans = findsimilatity(all_doc[207])
print(all_doc[ans[0][0]])
print(all_doc[ans[1][0]])
print(all_doc[ans[2][0]])
recommend = open('rec.txt','w')

print(jieba.cut('特朗普与习近平'))
'''
for item in all_doc:
	recommend.write(findsimilatity(item))
	recommend.write('\n')
'''













