import requests
import json

from constants import DATABASE_ID, FILTERS, NOTION_VERSION, BEARER_TOKEN

url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

payload = json.dumps(FILTERS)

headers = {
  'Authorization': f'Bearer {BEARER_TOKEN}',
  'Content-Type': 'application/json',
  'Notion-Version': NOTION_VERSION
}

response_text = requests.request("POST", url, headers=headers, data=payload)
response = json.loads(response_text.text)

for result in response["results"]:
    name = result["properties"]["Name"]["title"][0]["plain_text"]
    tags =  [multi_select["name"]  for multi_select in result["properties"]["Type"]["multi_select"]]
