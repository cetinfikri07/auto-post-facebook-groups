from dotenv import load_dotenv
import openai
import json
import os

load_dotenv()


def generate(key):
    openai.api_key = os.environ['GPT_API_KEY']
    with open('promts.json') as file:
        promts = file.read()

    promts = json.loads(promts)
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': promts[key]}],
    )

    response = completion.choices[0].message.content
    return response
