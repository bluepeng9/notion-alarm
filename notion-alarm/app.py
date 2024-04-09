import os

import requests
from notion2md.exporter.block import StringExporter

md = StringExporter(block_id=os.environ['NOTION_BLOCK_ID']).export()
mattermost_webhook_header = os.environ['MATTERMOST_WEBHOOK_HEADER']
text_result = f'{mattermost_webhook_header}\n{md}'

# webhooks to mattermost
url = os.environ['MATTERMOST_WEBHOOK']
data = {
    "text": text_result
}
response = requests.post(url, json=data)
print(response.status_code)
