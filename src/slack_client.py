import json
import requests

class SlackClient(object):
    URL = 'TBD'

    def call_slack(self, msg):
        slack_data = {'text': msg}
        json_data = json.dumps(slack_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(SlackClient.URL, data=json_data,
                    headers=headers)
        
        print(response.status_code, response.text)