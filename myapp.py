import requests
import json

URL = "http://127.0.0.1:8000/facebookapi/"

def get_data(id = None):
 data = {}
 if id is not None:
  data = {'id':id}
 json_data = json.dumps(data)
 headers = {'content-Type':'application/json'}
 r = requests.get(url = URL, headers=headers, data = json_data)
 data = r.json()
 print(data)
get_data()

def post_data():
 data = {
  'user': 'vishal',
  'followers': 3,
  'following': 4,
  'bio': 'bye',
  'likes': 6,
 }
 headers = {'content-Type':'application/json'}

 json_data = json.dumps(data)
 r = requests.post(url = URL, headers=headers, data = json_data)
 data = r.json()
 print(data)

post_data()

def update_data():
 data = {
  'id': 3,
  'user':'Jack',
  'followers': 6,
 }
 headers = {'content-Type':'application/json'}

 json_data = json.dumps(data)
 r = requests.put(url = URL, headers=headers, data = json_data)
 data = r.json()
 print(data)

update_data()

def delete_data():
 data = { 'id': 3 }
 headers = {'content-Type':'application/json'}
 json_data = json.dumps(data)
 r = requests.delete(url = URL, headers=headers,  data = json_data)
 data = r.json()
 print(data)

 delete_data()





