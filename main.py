from dotenv import load_dotenv
import facebook
import json
import os

from generate_post import generate

load_dotenv()
groups = json.loads(os.environ['GROUPS'])
access_token = os.environ['ACCESS_TOKEN']

message = generate('Villa Tepe')
graph = facebook.GraphAPI(access_token=access_token)

for group in groups:
    post = graph.put_object(group, 'feed',message=message, link='https://mottovillas.com/')
    print(post)


