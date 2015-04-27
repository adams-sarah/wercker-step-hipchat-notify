import sys
import requests
import json

if len(sys.argv) < 8:
    print 'There should be 8 arguments'
    sys.exit(1)

token = str(sys.argv[1])
room_id = str(sys.argv[2])
from_name = str(sys.argv[3])
message = str(sys.argv[4])
color = str(sys.argv[5])
message_format = str(sys.argv[7])

notify = '0'
if str(sys.argv[6]) == 'true':
    notify = '1'

query = {'auth_token': token}
headers = {'Content-type': 'application/json'}
body = {
    'color': color,
    'message': message,
    'notify': notify,
    'message_format': message_format,
}

resp = requests.post('https://api.hipchat.com/v2/room/'+room_id+'/notification', params=query, headers=headers, data=json.dumps(body))

resp.raise_for_status()
