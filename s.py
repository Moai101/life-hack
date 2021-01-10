import requests
from bs4 import BeautifulSoup
import re
import time
import json 
import csv


local_project_url_list = []
local_project_title = []

# num=2
# for i in range(1,num):
#   time.sleep(1)
#   site = requests.get(f"https://camp-fire.jp/projects/category/local?page={i}")

#   soup = BeautifulSoup(site.text, "html.parser")

#   all_text = soup.text

#   all_text_list  = all_text.split("\n")

#   for text in all_text_list:
#         if "ecommerce" in text:

#           dataLayer = text.replace("dataLayer.push","")
#           dataLayer = dataLayer.replace("(","")
#           dataLayer = dataLayer.replace(";","")
#           dataLayer = dataLayer.replace(")","")
#           dic = eval(dataLayer)
#           try:
#             items = dic[0]["ecommerce"]["impressions"]

#             for  item in items:
#               local_project_url_list.append(f"https://camp-fire.jp/projects/view/{item['id']}?list=local_popular_page")
#               local_project_title.append(item["name"])
#           except:
#             break

# csvlist = [["URL","タイトル"]]

# print(local_project_title)
# for i in range(0,len(local_project_url_list)):
#     csvlist.append([local_project_url_list[i],local_project_title[i]])

# f = open("/Users/hattoriakitsugu/Desktop/life-hack/campfire1.csv", "w",encoding='shift_jis')
# writecsv = csv.writer(f, lineterminator='\n')

# # 出力
# writecsv.writerows(csvlist)

# # CSVファイルを閉じる。
# f.close()