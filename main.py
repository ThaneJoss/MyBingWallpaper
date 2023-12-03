import requests,datetime,os
import datetime

url='https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'
response = requests.get(url)

imgurl=f'https://www.bing.com{response.json()["images"][0]["url"]}'
imgdate=response.json()["images"][0]["startdate"]

#download image
img=requests.get(imgurl)

# if folder not exist, create it
if not os.path.exists('./images'):
    os.mkdir('./images')

with open(f'./images/{imgdate}.jpg','wb+') as f:
    f.write(img.content)

with open('today.jpg','wb+') as f:
    f.write(img.content)

now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(now)

current_timezone = datetime.datetime.now().astimezone().tzinfo


readme=f"""
# Bing Wallpaper
![bing](./images/{imgdate}.jpg) 
*update time: {now} {current_timezone}*
"""

with open('./readme.md','w+') as f:
    f.write(readme)