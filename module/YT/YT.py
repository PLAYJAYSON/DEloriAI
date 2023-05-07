import urllib.request as ur
import json
def yt_video_search(myKeyward):
    videoId_search = list()
    qq = myKeyward.encode('utf-8')
    k=0
    with open('C:\BOT\privacy/TockenFileYT.txt', 'r') as YTkey_file:
        YTkey = YTkey_file.read()
    with ur.urlopen(f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=3&q={qq}&type=video&key={YTkey}') as response:
        data = response.read()
        '''print(data)'''
        jsonDATA = json.loads(data)
        print(jsonDATA['items'])
        for i in jsonDATA['items']:
                videoId_search.append(i['id']['videoId'])
                k+=1
        print(videoId_search)
        print(k)
    return videoId_search
def yt_video_return(thisVideoIdList):
    linkList = list()
    for i in thisVideoIdList:
        linkList.append(f'https://www.youtube.com/watch?v={i}')
    return linkList


