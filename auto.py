import requests
import os
ids = ['280','346','484','261','229','344','221']

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

