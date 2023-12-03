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
![bing](today.jpg) 
*update time: {now} {current_timezone}*
"""

description="""

[简体中文](readme_zh.md)

This project is based on GitHub Actions and aims to simplify the process of accessing the captivating Bing daily images. Every day, Bing showcases a stunning image on its homepage representing various aspects such as nature, culture, and more.

## About
This project provides a simple solution that uses GitHub Actions workflow to automate the process of fetching the daily Bing wallpaper. It runs a script at either 16:00 UTC every day or whenever you push a commit to the repository, fetching the latest Bing wallpaper image and saving it locally for easy access. You can use it as a desktop background or for other purposes.

## Features

- Automated retrieval of the latest Bing wallpaper using GitHub Actions.
- Saving the images locally for easy access.
- Can be used to set Bing wallpaper as your desktop background.
- Simple and easy-to-use Python script.

## Usage

1. Fork this repository.
2. Go to "Settings-Actions-General-Workflow permissions" and select "Read and write permissions," then click "Save."
3. The script will automatically run and fetch the latest Bing wallpaper image at 16:00 UTC every day or whenever you push a commit to the repository.

## Contributions
Contributions to this project are welcome. If you find any issues or have any improvements in mind, feel free to raise an issue or submit a pull request.

---
Enjoy the captivating Bing daily images effortlessly with My-Bing-Wallpaper using GitHub Actions!
"""

description_zh="""

[English](readme.md)

这个项目是基于 GitHub Actions 的，旨在简化访问迷人的必应每日图片的过程。每天，必应在其主页展示一张令人惊叹的图片，代表着自然、文化等各个方面。

## 关于
该项目提供了一个简单的解决方案，使用 GitHub Actions 自动化流程来获取每日必应壁纸。它在每天 UTC 时间 16:00 或每当你向存储库推送提交时运行脚本，获取最新的必应壁纸图片并将其保存在本地，方便您用作桌面背景或其他用途。

## 特点

- 基于 GitHub Actions，自动化获取最新的必应壁纸图片。
- 将图片保存在本地，以便轻松访问。
- 可用于将必应壁纸设置为桌面背景。
- 简单易用的 Python 脚本。

## 使用方法

1. Fork 此存储库。
2. 进入 "Settings-Actions-General-Workflow permissions"，选择 "Read and write permissions"，然后点击 "Save"。
3. 每天 UTC 时间 16:00 或每当您向存储库推送提交时，脚本将自动运行并获取最新的必应壁纸图片。

## 贡献
欢迎对这个项目进行贡献。如果您发现任何问题或有改进建议，请随时提出问题或提交拉取请求。

---
使用 My-Bing-Wallpaper，通过 GitHub Actions 轻松享受迷人的必应每日图片吧！
"""

with open('./readme.md','w+',encoding='utf-8') as f:
    f.write(readme+description)

with open('./readme_zh.md','w+',encoding='utf-8') as f:
    f.write(readme+description_zh)