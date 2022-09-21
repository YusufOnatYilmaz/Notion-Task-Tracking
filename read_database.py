import requests
import json

from constants import *

payload = json.dumps(FILTERS)

headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': NOTION_VERSION
}

def retrieve_database():
    text = ""
    for key in DATABASE_ID:

        url = f"https://api.notion.com/v1/databases/{DATABASE_ID[key]}/query"

        response_text = requests.request("POST", url, headers=headers, data=payload)
        response = json.loads(response_text.text)

        text += f"{key}:\n"
        for result in response["results"]:
            
            name = result["properties"]["Name"]["title"][0]["plain_text"]
            tags =  [multi_select["name"]  for multi_select in result["properties"]["Type"]["multi_select"]]
            
            text += f"- {name}"
            for tag in tags:
                text += f" ({tag})"
            text += "\n"
    return text

if __name__ == '__main__':
    print(retrieve_database())
