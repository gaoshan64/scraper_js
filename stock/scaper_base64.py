# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : scaper_base64.py
# Time       ：2022/3/30 7:18
# Author     ：Gao Shan
# Description：
"""

import base64
import pprint
import json
import time
import math
import requests
import js2py
import execjs
import calendar
import datetime
import pandas as pd


js2='time=Math.floor(new Date().getTime()/1000)'

js3='''
		function missjson (input) {
			var keyStr = "ABCDEFGHIJKLMNOP" + "QRSTUVWXYZabcdef" + "ghijklmnopqrstuv"   + "wxyz0123456789+/" + "=";
			var output = "";
			var chr1, chr2, chr3 = "";
			var enc1, enc2, enc3, enc4 = "";
			var i = 0;
			do {
				chr1 = input.charCodeAt(i++);
				chr2 = input.charCodeAt(i++);
				chr3 = input.charCodeAt(i++);
				enc1 = chr1 >> 2;
				enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
				enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
				enc4 = chr3 & 63;
				if (isNaN(chr2)) {
					enc3 = enc4 = 64;
				} else if (isNaN(chr3)) {
					enc4 = 64;
				}
				output = output + keyStr.charAt(enc1) + keyStr.charAt(enc2)
						+ keyStr.charAt(enc3) + keyStr.charAt(enc4);
				chr1 = chr2 = chr3 = "";
				enc1 = enc2 = enc3 = enc4 = "";
			} while (i < input.length);

			return output;}

		function getResCode(){
			var time=Math.floor(new Date().getTime()/1000); return missjson(""+time);
		}

    getResCode()'''

def get_mcode():
    #print("js################")
    #time_str=js2py.eval_js(js2)
    #print(time_str)
    result=js2py.eval_js(js3)

    return result
def get_mcode2():
    print("python#############")
    time_str=str(int(time.time()))
    print(time_str)
    result=base64.b64encode(time_str.encode())
    print(result)
    return result
def get_mcode3():
    print("Mr. He###############")
    ts=calendar.timegm(time.gmtime())
    print(ts)
    mcode=base64.b64encode(str(ts).encode()).decode()
    print(mcode)
    return mcode




URL='http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007'
data={
    'tdate':"2022-03-29",
    'market':'SZE'
}
header={
    'mcode':get_mcode3(),
    'Cookie':'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1648562943; JSESSIONID=BF970A1E255FFFA4395727161B1B7136; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1648617485',
    #'Host':'webapi.cninfo.com.cn',
    'Referer':'http://webapi.cninfo.com.cn/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
}
response=requests.post(URL,headers=header,data=data).json()



if __name__ == '__main__':

    record = response['records']
    df = pd.DataFrame(record)
    col = ['证券代码', '证券简称', '交易日期', '开盘价', '最高价', '最低价', '收盘价', '成交数量']
    df = df[col]
    print(df)
    df.to_csv('result.csv')






