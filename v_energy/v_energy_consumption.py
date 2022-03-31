# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : v_energy consumption.py
# Time       ：2022/3/30 15:55
# Author     ：Gao Shan
# Description：
"""
import requests
import json
import pprint
import pandas as pd

URL='https://yhgscx.miit.gov.cn/fuel-consumption-center/fcSearchCtr/queryList'
URL2='https://yhgscx.miit.gov.cn/fuel-consumption-center/fcSearchCtr/queryDetail'

data={
  "reportType": "1",
  "currentPage": 2,
  "pageSize": 67562,
  "position": "right",
  "pageSizes": [
    10,
    30,
    50,
    100,
    67562
  ],
  "layout": "sizes, total,prev, pager, next, jumper",
  "totalSize": 67562
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=UTF-8',
    'Authorization': '',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Origin': 'https://yhgscx.miit.gov.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://yhgscx.miit.gov.cn/fuel-consumption-web/mainPage',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie': 'route=1648540912.016.21345.810716',
}



data2={"applyId":"96b62692ba3549a1ab1126a96c688dd6"}



if __name__ =='__main__':
    response = requests.post(URL,headers=headers, data=json.dumps(data)).json()


    info_list = response['info']['list']
    df=pd.DataFrame(info_list)
    df.to_csv('v_enger.csv')
