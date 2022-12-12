import os
import pprint 
import openai
openai.organization = "org-XY7tvMhByFMbnaHiVRXoQjab"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)

# pprint.pprint(dict(response),width=1)

print(response[0])