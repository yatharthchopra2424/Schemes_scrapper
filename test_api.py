import urllib.request
import json
import urllib.error

data = json.dumps({
    'data': {
        'businessName': 'Test Business',
        'businessType': 'Startup',
        'businessDescription': 'Software development'
    }
}).encode('utf-8')

req = urllib.request.Request(
    'http://127.0.0.1:8000/recommend-schemes',
    data=data,
    headers={'Content-Type': 'application/json'}
)

try:
    res = urllib.request.urlopen(req)
    print("Success:", res.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error:", e.read().decode('utf-8'))
