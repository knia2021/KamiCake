# -*- coding = utf-8 -*-
# coding=utf-8
# @Time : 2021/9/18 2:34
# @Author : knia
# @File : kcapp.py
# @Software : PyCharm
import os
from glob import glob
from guy import Guy
import urllib.request
import urllib.parse
import string
import random
import requests


class App(Guy):
	size = (1000, 1000)

	def render(self, path):
		with open(os.path.join(path, "static/index.html"), encoding='utf-8') as html:
			buf = html.read()
		with open(os.path.join(path, "static/kamicake.css")) as css:
			bufCss = css.read()
		buf = buf.replace("/* CSS */", bufCss)
		# buf = buf.replace("/* JS */", r.script)
		return buf

	def test(self):
		print("hello world")

	def getCookies(self,account,pwd):
		# loginurl = 'https://id.app.acfun.cn/rest/web/login/signin'
		# header = {
		# 	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
		# }
		# data = {
		# 	"username": account,
		# 	"password": pwd,
		# 	"key": "",
		# 	"captcha": ""
		# }
		# data = urllib.parse.urlencode(data).encode('utf-8')
		# request = urllib.request.Request(loginurl, headers=header, data=data)
		# response = urllib.request.urlopen(request)
		# data = response.read().decode()
		# cookie_value = ''
		# print(data)
		# for k, v in response.getheaders():
		# 	if k == 'Set-Cookie':
		# 		cookie_value += v + ';'
		# cookieList = cookie_value.split(';')
		# cookieList = list(set(cookieList))
		# cookies = ''
		# for l in cookieList:
		# 	if l.find('acPasstoken') != -1 or l.find('auth_key') != -1 or l.find('acPostHint') != -1 or l.find(
		# 		'acPostHint') != -1 or l.find('ac_userimg') != -1 or l.find('ac_username') != -1:
		# 		cookies += l + ';'
		# cookies = 'acPasstoken=;auth_key=;ac_userimg=;ac_username=;'
		return ''

	async def login(self):
		# userdata {'id': '123', 'pwd': '321'}
		userdata = await self.js.getname()
		cookies = self.getCookies(userdata['id'],userdata['pwd'])

		#获取actoken
		getTokenURL = 'https://id.app.acfun.cn/rest/web/token/get'
		header = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
			"cookie": cookies
		}
		data = {
			"sid": "acfun.midground.api"
		}
		data = urllib.parse.urlencode(data).encode('utf-8')
		request = urllib.request.Request(getTokenURL, headers=header, data=data)
		response = urllib.request.urlopen(request)
		data = response.read().decode()
		print(data)
		# {"result": 0, "ssecurity": "vJAUtvm2G0Q994kGplInVQ==", "userId": 40030215,
		#  "acfun.midground.api_st": "","acfun.midground.api.at": ""}
		#主要获取userId  SecurityKey(ssecurity) serviceToken
		#

if __name__ == "__main__":
	app = App()
	app.run()
