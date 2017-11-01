import json  
import requests  # python-requests is installable from PyPI...
newaccount = {'user_name': 'wxf', 'pass_word':'admin','title':'cto','salary': 3000}
r = requests.post('http://127.0.0.1:5000/api/account', data=json.dumps(newaccount),headers={'content-type': 'application/json'})
#r = requests.get('http://127.0.0.1:5000/api/account', headers={'content-type': 'application/json'})
