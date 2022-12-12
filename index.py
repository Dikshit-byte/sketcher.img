import os
import pprint 
import openai
import wget
import pyperclip as pc
from pathlib import Path
openai.organization = "org-XY7tvMhByFMbnaHiVRXoQjab"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

local_download_path = str(Path.home()/"Downloads")
response = openai.Image.create(
  prompt="beautiful photo of blue jelly fish in water",
  n=1,
  size="1024x1024"
)

# pprint.pprint(dict(response),width=1)

img_url = response['data'][0]['url']
pc.copy(img_url)
wget.download(img_url,local_download_path)
