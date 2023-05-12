from dotenv import load_dotenv
import facebook
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

def post_content(groups,message,link):
    access_token = os.environ['ACCESS_TOKEN']
    graph = facebook.GraphAPI(access_token=access_token)
    posts = []
    for group in groups:
        post = graph.put_object(group, 'feed', message=message, link=link)
        posts.append(post)

    return posts

def write_response_to_txt(message):
    with open('response.txt','w') as f:
        f.write(message)

def read_response_from_txt():
    with open('response.txt','r') as f:
        message = f.read()

    return message

groups = ["1600790610213556"]
link = 'https://mottovillas.com/'

message = generate('Villa Tepe')
write_response_to_txt(message)
message = read_response_from_txt()

posts = post_content(groups,message,link)

