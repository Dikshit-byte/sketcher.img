import os,sys,time
import openai
# import gradio as gr
# from typer import prompt

openai.organization = "org-XY7tvMhByFMbnaHiVRXoQjab"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()


start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

while(True):
    prompt = input("\nAsk me anything ? ")
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    result = response.choices[0].text
    for char in result: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
