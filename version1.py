import os
import pprint
from numpy import quantile 
import openai
import wget
import pyperclip as pc
from pathlib import Path
from PIL import Image
openai.organization = "org-XY7tvMhByFMbnaHiVRXoQjab"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

local_download_path = "C:\\Users\\singh\\AppData\\Local\\OpenAIWallpaper"
# user_query = input("What you want ? : ")
# response = openai.Image.create(
#   prompt = user_query,
#   n=1,
#   size="1024x1024"
# )

# photo_path = "C:\\Users\\singh\\AppData\\Local\\OpenAIWallpaper\\1.png"
# im = Image.open(photo_path) 
# im.show()

# image = Image.open("C:\\Users\\singh\\AppData\\Local\\OpenAIWallpaper\\2.png")
# new_img = image.resize((400,400))
# new_img.save(local_download_path+'\\3.png')
# new_img.show()
# response = openai.Image.create_variation(
#   image = open("C:\\Users\\singh\\AppData\\Local\\OpenAIWallpaper\\3.png","rb"),
#   n=1,
#   size="1024x1024"
# )
# img_url = response['data'][0]['url']

# pprint.pprint(dict(response),width=1)

# img_url = response['data'][0]['url']
# pc.copy(img_url)
# wallpaper =  wget.download(img_url,local_download_path)
# words = wallpaper.split("/")
# print(words[1])

# photo_path = "C:\\Users\\singh\\AppData\\Local\\OpenAIWallpaper\\"+words[1]
# im = Image.open(photo_path)
# print(photo_path)
# im.show()

image_path = "C:\\Users\\singh\\AppData\\Local\\OpenAIWallpaper\\4.png"
image_file = Image.open(image_path)

image_file.save(local_download_path+'\\5.png',quality=95)

image_path1 = "C:\\Users\\singh\\AppData\\Local\\OpenAIWallpaper\\5.png"
im = Image.open(image_path1)
im.show()
