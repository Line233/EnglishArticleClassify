#!/usr/bin/python
import re
import os

words=open('words.txt','r')

words2 = open("PureVocabulary.txt", 'a')
i=0
for eachline in words:
    line=eachline.strip()
    for w in line:
        if not w.isspace():
            words2.write(w)
        else:
            break
    words2.write('\n')
    i=i+1
print(i);


#打开fie_name路径下的my_infor.txt文件,采用追加模式

#若文件不存在,创建，若存在，追加

# my_open.write('蚌埠\n')

# my_open.close()
# line = "Cats are smarter than dogs"
 
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
#  # _*_ coding: utf-8 _*_
# import urllib.request
# # import json
# # get json/two ways to test
# #   first-web
# url1 = "https://www.baidu.com"
# url1 = "https://api.douban.com/shuo/v2/users/4569399/followers"
# response = urllib.request.urlopen(url1)
# # test=response.read()
# # second-a.json
# # file=open('a.json','r',encoding='utf-8')
# # test=file.read()
# # file.close()

# # #to dict
# # dicts=json.loads(test)
# # arr=[]
# # # #arr.append()
# # i=0

# # for var in dicts:
# #     arr.append(var['id'])
# #     i=i+1
# # print(i)
# # print(arr)
