import requests
import os
import datetime
from PIL import Image
from io import BytesIO
import json 

url='https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US&uhd=1&uhdwidth=3840&uhdheight=2160'
response = requests.get(url)

imgurl=f'https://www.bing.com{response.json()["images"][0]["url"]}&w=3840&h=2160'
imgdate=response.json()["images"][0]["startdate"]

imgtitle = response.json()["images"][0]["title"]
imgcopyright = response.json()["images"][0]["copyright"]

print(f"img title: {imgtitle}\nimg date: {imgdate}\nimg url: {imgurl}\nimg copyright: {imgcopyright}")

#download image
img=requests.get(imgurl)

storepath='./images'

# if folder not exist, create it
if not os.path.exists(storepath):
    os.mkdir(storepath)

img=Image.open(BytesIO(img.content))
save_kwargs = {
    'format': 'JPEG',
    'quality': 'high',
    'progressive': True
}

img.save(f'{storepath}/{imgdate}.jpg',**save_kwargs)

info={f"{imgdate}.jpg":
    {
    'title':imgtitle,
    'date':imgdate,
    'url':imgurl,
    'copyright':imgcopyright
    }
}

with open(f"{storepath}/{imgdate}.json", "w") as f:
    json.dump(info, f)
    

img.save('today.jpg', **save_kwargs)

now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(now)

current_timezone = datetime.datetime.now().astimezone().tzinfo


readme=f"""
# My Bing Wallpaper
![bing](today.jpg) 
*update time: {now} {current_timezone}*
"""

description="""

[简体中文](readme_zh.md)

This project is based on GitHub Actions and aims to simplify the process of accessing the captivating Bing daily images. Every day, Bing showcases a stunning image on its homepage representing various aspects such as nature, culture, and more.

You can view the entire collection at [thanejoss.com](https://thanejoss.com).

To obtain the original image, please use the following link: [Today's Wallpaper](https://bingwallpaper.thanejoss.com).
## About
This project provides a simple solution that uses GitHub Actions workflow to automate the process of fetching the daily Bing wallpaper. It runs a script at either 16:00 UTC every day or whenever you push a commit to the repository, fetching the latest Bing wallpaper image and saving it locally for easy access. You can use it as a desktop background or for other purposes.

## Features

- Automated retrieval of the latest Bing wallpaper using GitHub Actions.
- Saving the images locally for easy access.
- Can be used to set Bing wallpaper as your desktop background.
- Simple and easy-to-use Python script.

## Usage

1. Fork this repository.
2. The script will automatically run and fetch the latest Bing wallpaper image at 16:00 UTC every day or whenever you push a commit to the repository.

## Contributions
Contributions to this project are welcome. If you find any issues or have any improvements in mind, feel free to raise an issue or submit a pull request.

---
Enjoy the captivating Bing daily images effortlessly with MyBingWallpaper using GitHub Actions!
"""

description_zh="""

[English](readme.md)

这个项目是基于 GitHub Actions 的，旨在简化访问迷人的必应每日图片的过程。每天，必应在其主页展示一张令人惊叹的图片，代表着自然、文化等各个方面。

您可以在 [thanejoss.com](https://thanejoss.com) 浏览完整合集。

要获取原始图片，请使用以下链接：[今日壁纸](https://bingwallpaper.thanejoss.com)。

## 关于
该项目提供了一个简单的解决方案，使用 GitHub Actions 自动化流程来获取每日必应壁纸。它在每天 UTC 时间 16:00 或每当你向存储库推送提交时运行脚本，获取最新的必应壁纸图片并将其保存在本地，方便您用作桌面背景或其他用途。

## 特点

- 基于 GitHub Actions，自动化获取最新的必应壁纸图片。
- 将图片保存在本地，以便轻松访问。
- 可用于将必应壁纸设置为桌面背景。
- 简单易用的 Python 脚本。

## 使用方法

1. Fork 此存储库。
2. 每天 UTC 时间 16:00 或每当您向存储库推送提交时，脚本将自动运行并获取最新的必应壁纸图片。

## 贡献
欢迎对这个项目进行贡献。如果您发现任何问题或有改进建议，请随时提出问题或提交拉取请求。

---
使用 MyBingWallpaper，通过 GitHub Actions 轻松享受迷人的必应每日图片吧！
"""

with open('./readme.md','w+',encoding='utf-8') as f:
    f.write(readme+description)

with open('./readme_zh.md','w+',encoding='utf-8') as f:
    f.write(readme+description_zh)
