# -*- coding: utf-8 -*-
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

requests.packages.urllib3.disable_warnings()

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}


def getTimeStamp():
	current_milli_time = lambda: int(round(time.time() * 1000))
	return current_milli_time()


class showpng(Thread):
	def __init__(self, data):
		Thread.__init__(self)
		self.data = data

	def run(self):
		img = Image.open(BytesIO(self.data))
		img.show()


# 验证cookie是否有效
def islogin(session):
	try:
		session.cookies.load(ignore_discard=True)
	except Exception:
		pass
	loginurl = session.post("https://id.app.acfun.cn/rest/web/token/get",data = {"sid": "acfun.midground.api"},headers=headers).json()
	if loginurl['result'] == 0:
		print('Cookies值有效，无需扫码登录！')
		return session, True
	else:
		print('Cookies值已经失效，请重新扫码登录！')
		return session, False


def kslogin():
	if not os.path.exists('accookies.txt'):
		with open("accookies.txt", 'w') as f:
			f.write("")
	session = requests.session()
	session.cookies = cookielib.LWPCookieJar(filename='accookies.txt')
	# 验证cookie是否有效
	session, status = islogin(session)
	if not status:
		queryform = 'type=WEB_LOGIN&_=%d' % getTimeStamp()
		loginurl = 'https://scan.acfun.cn/rest/pc-direct/qr/start?' + queryform
		urldata = session.get(loginurl, data={}, headers=headers).json()
		testpng = base64.b64decode(urldata['imageData'])
		token = urldata['qrLoginToken']
		Signat = urldata['qrLoginSignature']
		print((token, Signat))
		t = showpng(testpng)
		t.start()
		tokenurl = 'https://scan.acfun.cn/rest/pc-direct/qr/scanResult?qrLoginToken=%s&qrLoginSignature=%s&_=%d' % (
		token, Signat, getTimeStamp())
		# while 1:
		#
		# 	time.sleep(3)
		tokendata = session.post(tokenurl, data={}, headers=headers).json()
		signatToken = tokendata['qrLoginSignature']
		# if tokendate['result'] == 707:
		# 	print('登录二维码已过期，请重新运行！')
		if tokendata['result'] == 0:
			data = session.post('https://scan.acfun.cn/rest/pc-direct/qr/acceptResult?qrLoginToken=%s&qrLoginSignature=%s&_=%d' % (token, signatToken, getTimeStamp()), headers=headers)

			# 获取api_st等token 不确定是否必须 先搁置
			# actokenurl = 'https://id.app.acfun.cn/rest/web/token/get'
			# print(session.cookies)
			# res = session.post(actokenurl,data = {"sid": "acfun.midground.api"} ,headers=headers)
			# print('----')
			# # print(res.json())
			# actokens = res.json()
			# session.cookies.set('SecurityKey', actokens['ssecurity'])
			# session.cookies.set('userId', actokens['userId'])
			# session.cookies.set('ServiceToken', actokens['acfun.midground.api_st'])
			# session.cookies.set('acfun.midground.api.at', actokens['acfun.midground.api.at'])

			# print(session.cookies)
			print('已确认，登录成功！')
		# break
		session.cookies.save()
		return session


if __name__ == '__main__':
	kslogin()
