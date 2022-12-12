import os
import pprint 
import openai
import pyperclip as pc
openai.organization = "org-XY7tvMhByFMbnaHiVRXoQjab"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

response = openai.Image.create(
  prompt="lakshadweep island with blue water",
  n=1,
  size="1024x1024"
)

# pprint.pprint(dict(response),width=1)

img_url = response['data'][0]['url']
pc.copy(img_url)    