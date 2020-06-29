from apiclient.discovery import build
from datetime import datetime

api_key = "YourApiKey"
youtube = build('youtube', 'v3', developerKey=api_key)
startTime = datetime(year=2005, month=1, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')
endTime = datetime(year=2008, month=1, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')
request = youtube.search().list(q='python programming', part='snippet', type='video', publishedAfter=startTime, publishedBefore=endTime, maxResults=50)
res = request.execute()
for item in sorted(res['items'], key=lambda x:x['snippet']['publishedAt']):
	print(f"Title: {item['snippet']['title']}\nPublished at: {item['snippet']['publishedAt']}\nPublished by:{item['snippet']['channelTitle']}")
	print('\n')