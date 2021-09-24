import urllib.request
import urllib.parse
import string
import random

def adIDGen():
	str_list = [random.choice(string.digits + string.ascii_letters) for i in range(36)]
	random_str = ''.join(str_list).lower()
	return random_str


def main():
	url = 'https://www.acfun.cn/rest/pc-direct/new-danmaku/add'
	header = {
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
		"cookie": '_did=web_456171085B3EBB4F; _did=web_456171085B3EBB4F; uuid=3f7d080f5d0da39b9931c6bb458710a2; actoken=nM5Xp-D8DPLp_JP-LfBLEElM; did=web_1b5a0aa91e1c79055b7fe7b7c325d435; lsv_js_player_v2_main=ed9cb1; acPasstoken=ChVpbmZyYS5hY2Z1bi5wYXNzdG9rZW4ScA1oIb7tF_o866pu_G8mc3-x4zNYFCg0Lgm1ObRfTtVcrlKspt75ny-GslMYBCrEPW2fXZ4n_n-bTUZnDKa6YdGKr4lGlckDhP-5CuIZYJ6yaLp8GtEj2Udc0LaqsM-E36sv4RAJ8fROXr326wOOghgaEnfcCHKF_CPUPpmjyzdSlISnMCIgz7FEnVbDE6EScQfNN84CpPgqjCCmph5NfUjEQrSlkIIoBTAB; auth_key=472630; ac_username=%E7%BA%A2%E6%9C%88%E5%A6%AE%E5%A8%85; acPostHint=5c5bee63ff94af63d4908a4e6c555d9c872f; ac_userimg=https%3A%2F%2Fimgs.aixifan.com%2Fcontent%2F2020_11_3%2F1.6043781783454473E9.png; didv=1631620468995; safety_id=AAJmRzj6S3VQE5FQq1QmPODU; csrfToken=b0vuMDYoSu-0vjdfkXDl8YXI; session_id=503198542FB361FA; webp_supported=%7B%22lossy%22%3Atrue%2C%22lossless%22%3Atrue%2C%22alpha%22%3Atrue%2C%22animation%22%3Atrue%7D; Hm_lvt_2af69bc2b378fb58ae04ed2a04257ed1=1631620158,1631678068,1631679072,1631703820; Hm_lpvt_2af69bc2b378fb58ae04ed2a04257ed1=1631703866; cur_req_id=7480637792273662_self_acc142cc00ad514377c2ec22fc322161; cur_group_id=7480637792273662_self_acc142cc00ad514377c2ec22fc322161_0; WEBLOGGER_INCREAMENT_ID_KEY=28433; WEBLOGGER_HTTP_SEQ_ID=21065',
		'referer': 'https://www.acfun.cn/v/ac31100201',
		'content-type': 'application/x-www-form-urlencoded',
		'sec-ch-ua': 'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': "Windows",
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin'
	}

	currdmkid = adIDGen()
	print('main id:',currdmkid)

	advancedDanmakuExtDataValue = '{"id":"' + currdmkid + '","content":"请求测试-主要","contentType":0,"startTime":0,"durationTime":1000,"anchor":4,"wordStyle":{"font":"SimHei","size":25,"bold":false,"stroke":false,"color":"#ffffff"},"scale":{"x":1,"y":1,"z":1},"rotate":{"x":0,"y":0,"z":0},"animationFrames":[{"from":{"pos":{"x":0,"y":50,"z":1}},"to":{"pos":{"x":100,"y":50,"z":1}},"timingFunction":"linear","staticTime":0,"moveTime":2000}],"zIndex":50,"startTimeNow":false,"user":"472630"}'

	data = {
		'body': '请求测试-主要',
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

	data = urllib.parse.urlencode(data).encode('utf-8')

	request = urllib.request.Request(url, headers=header, data=data)

	response = urllib.request.urlopen(request)

	data = response.read().decode()

	print(data)

# main()
# {"result":0,"danmakuId":219157678,"host-name":"hb2-acfun-kce-node121.aliyun"}
