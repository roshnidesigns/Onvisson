import requests 

from isodate import parse_duration
from django.conf import settings
from django.shortcuts import render, redirect



def index(request):
	videoInfoList =[]
		
	if request.method=="POST":

		search_url='https://www.googleapis.com/youtube/v3/search'
		video_url = 'https://www.googleapis.com/youtube/v3/videos'

		search_parameters = {
			'part' : 'snippet',
			'q' : request.POST['search'],
			'key' : settings.YOUTUBE_DATA_API_KEY,
			'maxResults' : 48,
			'type' : 'video'
		}

		r = requests.get(search_url, params =search_parameters)
		results = r.json()['items']

		videoIdList = []
		for re in results:
			videoIdList.append(re['id']['videoId'])

		if request.POST['submit'] == 'feelinglucky':
			return redirect(f'https://www.youtube.com/watch?v={ videoIdList[0] }')

		video_parameters = {
			'part' : 'snippet,contentDetails',
			'key' : settings.YOUTUBE_DATA_API_KEY,
			'id': ','.join(videoIdList),
			'maxResults' : 9
		}

		r = requests.get(video_url,params = video_parameters)
		results = r.json()['items']

		for re in results:
			videoInfo = {
			'title': re['snippet']['title'],'id': re['id'], 
			'duration' :parse_duration(re['contentDetails']['duration']),
		 	'thumbnail': re['snippet']['thumbnails']['high']['url'],
			'url' : f'https://www.youtube.com/watch?v={ re["id"]}'			
			}
			videoInfoList.append(videoInfo)

	#print(videoInfoList)

	data = {
	'videoInfoList' : videoInfoList
	}

	return render(request, 'search/index.html',data)
