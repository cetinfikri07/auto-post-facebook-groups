from dotenv import load_dotenv
import facebook
import json
import os

load_dotenv()

groups = json.loads(os.environ['GROUPS'])
access_token = os.environ['ACCESS_TOKEN']

msg = "TEST 02"
link = 'https://mottovillas.com/'

graph = facebook.GraphAPI(access_token=access_token)

for group in groups:
    post = graph.put_object(group, 'feed',message = msg, link=link)
    print(post)


