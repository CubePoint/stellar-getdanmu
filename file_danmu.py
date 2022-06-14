import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re
import bs4
import csv
import random

class file_danmu():
    def __init__(self, url):
        self.url = url
        self.medianame = '弹幕文件'
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    
    def get_danmu_by_url(self):
        danmudata = []
        jsonlist = []
        self.get_danmu(jsonlist)
        jsonout = {'danmu_type':'file','danmu':jsonlist}
        danmudata.append({'title':self.medianame,'data':jsonout})
        return danmudata

    def get_danmu(self,jsonlist):
        res = requests.get(self.url,verify=False)
        if res.status_code == 200:
            jsondata = json.loads(res.text, strict=False)
            for item in jsondata:
                newitem = {'tp':item['tp'],'msg':item['msg']}
                jsonlist.append(newitem)
            

if __name__ == '__main__':
    r = input('请输入文件网页地址：\n')
    dm = file_danmu(r)
    dm.get_danmu_by_url('f:\\py')