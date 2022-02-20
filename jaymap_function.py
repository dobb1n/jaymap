import requests
import re 
import os
from datetime import date
from datetime import timedelta
import json

today = date.today()
report_date = today - timedelta(days=6)

api_key = os.environ.get('GUARDIAN_API_KEY')
payload = {}

# really i need to url encode the reviewer, so that can be a different critic
url2 = f"https://content.guardianapis.com/search?section=food&from-date={report_date}&q=jay%20rayner&api-key={api_key}"


response = requests.request("GET", url2, data = payload)
responsejson = response.json()

#print(json.dumps(responsejson, indent=4, sort_keys=True))
for result in responsejson['response']['results']:
    print(result['apiUrl'])
    article = requests.request("GET", result['apiUrl'], data = payload)
    print(article)
