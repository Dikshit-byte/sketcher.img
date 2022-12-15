import os,sys,time
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

while(True):
    prompt = input("\nAsk me anything ? ")
    response = openai.Completion.create(
     model="text-davinci-003",
    prompt=prompt,
    temperature=0.5,
    max_tokens=1024,
    top_p=0.3,
    frequency_penalty=0.5,
    presence_penalty=0
    )
    result = response.choices[0].text
    for char in result: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
