from apiclient.discovery import build

api_key = "AIzaSyC-bR9P4rY9-7s098zUihwqRYDXV9GrTDQ"
youtube = build('youtube', 'v3', developerKey=api_key)
request = youtube.search().list(q='cricket', part='snippet', type='video', maxResults=10)
res = request.execute()
for item in res['items']:
	print(item['snippet']['title'])