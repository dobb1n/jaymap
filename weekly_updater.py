import requests
import re 
import os

from datetime import date, datetime
from dateutil.relativedelta import relativedelta, SA
date_of_interest = datetime.now() + relativedelta(weekday=SA(-1))

start_date = date_of_interest.strftime("%Y-%m-%d")

page_size = 5

#we need to fail if the key isnt set
try:
    api_key = os.environ['GUARDIAN_API_KEY']
except:
    raise SystemExit("specify the API key as an env var before continuing")


#base url which looks for the jay tags 
url = f"https://content.guardianapis.com/search?api-key={api_key}&tag=food/series/jay-rayner-on-restaurants&page-size={page_size}&from-date={start_date}"
payload = {}
headers = {
  'Cookie': 'AWSELB=75B9BD811C5C032EDEF76366759629DCCB8726D7A371904BEC1C3B7DFC40019571E370E2C4E4519DDF3CD336789F71716B110728D88A7C69AE901D39C1821FF2C5E227F5F9; AWSELBCORS=75B9BD811C5C032EDEF76366759629DCCB8726D7A371904BEC1C3B7DFC40019571E370E2C4E4519DDF3CD336789F71716B110728D88A7C69AE901D39C1821FF2C5E227F5F9; BCSI-CS-682e9ee7ab0fdcff=1'
}

count = 1
#function to go through the results
def review_grabber(apiresults, count):
    with open('jaymap_new.csv', 'a') as csvfile:
        #if status is ok, work through the list of results and find the postcodes in the linked articles
        if apiresults['response']['status'] == 'ok':
            for result in apiresults['response']['results']:
                article = requests.request("GET", result['webUrl'], headers=headers, data = payload)
                postcode = re.findall(r'\b[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}\b', article.text)
                if len(postcode) > 0:
                    csvfile.write(f"\n{count},{result['webTitle']},{result['webUrl']},{postcode[0]}")
                    print(count, result['webTitle'], result['webUrl'], postcode[0])
                count += 1
            return count

#fetch the first page listing articles by jay
response = requests.request("GET", url, headers=headers, data = payload)

#read the response into json so we can index it
responsejson = response.json()

if responsejson['response']:
    if responsejson['response']['status'] == 'ok':
        #the articles are a list
        for article in responsejson['response']['results']:
            print(article['webTitle'])
            article_text = requests.request("GET", article['webUrl'], headers=headers, data = payload)
            postcode = re.findall(r'\b[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}\b', article_text.text)
            if len(postcode) > 0:
                print(postcode)