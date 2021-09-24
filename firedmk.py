# -*- coding = utf-8 -*-
# @Time : 2021/9/20 20:25
# @Author : knia
# @File : firedmk.py
# @Software : PyCharm
import base64
import agent
from threading import Thread
import time
import requests
from io import BytesIO
import http.cookiejar as cookielib
from PIL import Image
import os
import time

from adHelper import adIDGen

def tstfire():
	# cookiejar转为cookie字符串
	session = requests.session()
	session.cookies = cookielib.LWPCookieJar(filename='accookies.txt')
	session.cookies.load(ignore_discard=True)
	cks = session.cookies
	cookie_str = ''
	for c in cks:
		cookie_str += c.name + '=' + c.value + ';'
	addurl = 'https://www.acfun.cn/rest/pc-direct/new-danmaku/add'
	headers = {
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
		'referer': 'https://www.acfun.cn/v/ac31100201',
		'content-type': 'application/x-www-form-urlencoded',
		'sec-ch-ua': 'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': "Windows",
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'cookie':cookie_str
	}
	dmkid = adIDGen()
	print('firedmk:',dmkid)
	advancedDanmakuExtDataValue = '{"id":"' + dmkid + '","content":"请求测试-cookie测试1","contentType":0,"startTime":0,"durationTime":2000,"anchor":4,"wordStyle":{"font":"SimHei","size":25,"bold":false,"stroke":false,"color":"#cb6d2e"},"scale":{"x":1,"y":1,"z":1},"rotate":{"x":0,"y":0,"z":0},"animationFrames":[{"from":{"pos":{"x":0,"y":50,"z":1}},"to":{"pos":{"x":100,"y":50,"z":1}},"timingFunction":"linear","staticTime":0,"moveTime":2000}],"zIndex":50,"startTimeNow":false,"user":"472630"}'

	data = {
		'body': '请求测试-cookie测试1',
		'videoId': 26032657,
		'mode': 1,
		'position': 0,
		'mode': 1,
		'size': 6,
		'color': 0,
		'type': 'douga',
		'subChannelId': 1,
		'subChannelName': '动画',
		'id': 31100201,
		'danmakuType': 1,
		'advancedDanmakuExtData': advancedDanmakuExtDataValue,
		'roleId': ''
	}
	dmkres = session.post(addurl, data=data, headers=headers).json()
	print(dmkres)

# 通过读取cookie来发送弹幕测试通过
# if __name__ == '__main__':
# 	tstfire()

# #firedmk: zgusw07opnap26pqzaaewhlllfk99e6686cc
# {'result': 0, 'danmakuId': 220139462, 'host-name': 'hb2-acfun-kce-node26.aliyun'}
# 09/20/22.02