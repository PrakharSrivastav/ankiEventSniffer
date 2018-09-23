import requests
import json

headers = {'Content-Type': 'application/json'}
r = requests.post('http://localhost:8080/anki-rest', json={
    "type": "CAR_TRANSITIONED",
    "carId": "FC:70:98:68:10:BA:01",
    "deviceId": "",
    "carName": "Skull",
    "trackSegment": 22,
    "lap": 123,
    "raceStatus": "",
    "trackStyle": "Left Turn",
    "raceId": 1,
    "dateTime": 1537366468,
    "dateTimeString": "18/09/19 16:14:28:403930",
    "demozone": ""
}, headers=headers)
