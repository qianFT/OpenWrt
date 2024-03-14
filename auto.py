import requests
import os
ids = ['280','346','484','261','229','344']

for i,id_i in enumerate(ids):
	response = requests.get('http://mpp.liveapi.mgtv.com/v1/epg/turnplay/getLivePlayUrlMPP?version=PCweb_1.0&platform=1&buss_id=2000001&channel_id='+id_i)
	data = response.json()
	text = data['data']['url']


	path = 'm3u8/hn'+str(i)+'.m3u8'
	directory = os.path.dirname(path)
	if not os.path.exists(directory):
		os.makedirs(directory)

	with open(path, "w") as file:
		file.write('#EXTM3U\n')
		file.write('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1280000\n')
		file.write(text)




'''
湖南经视 id=280
湖南都市 id=346
湖南电视剧 id=484
湖南公共 id=261
湖南国际 id=229
湖南娱乐 id=344
快乐购 id=267
茶频道 id=578
金鹰纪实 id=316
金鹰卡通 id=287
快乐垂钓 id=218
先锋乒羽 id=329
长沙新闻 id=269
长沙政法 id=254
长沙女性 id=230
'''