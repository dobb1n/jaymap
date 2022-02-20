import requests
import re 
import os
from datetime import date
from datetime import timedelta

today = date.today()
report_date = today - timedelta(days=6)

api_key = os.environ.get('GUARDIAN_API_KEY')
payload = {}

# really i need to url encode the reviewer, so that can be a different critic
url2 = f"https://content.guardianapis.com/search?section=food&from-date={report_date}&q=jay%20rayner&api-key={api_key}"


response = requests.request("GET", url2, data = payload)
responsejson = response.json()

print(responsejson)