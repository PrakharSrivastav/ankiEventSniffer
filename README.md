# ankiEventSniffer
Anki Overdrive demo: python code to sniff BLE data between Mobile App and Anki cars

* Main code from Adafruit
* Anki Overdrive main parts from Oracle Australian Presales Team (John Graves ```<john.graves@oracle.com>``` and others)
* Additional changes and improvements by Oracle Spanish Presales Team (Víctor Mendo ```<victor.mendo@oracle.com>``` and Carlos Casares ```<carlos.casares@oracle.com```)
 
# Event types

SPEED_MEASUREMENT
```json
 {
  "demozone": demozone,
  "deviceId": piId,
  "dateTime": int(time.time()),
  "dateTimeString": dateTimeString,
  "raceStatus": raceStatus,
  "raceId": raceCount,
  "carId": myDeviceAddress,
  "carName": myCarName,
  "speed": speed,
  "trackId": trackId,
  "lap": currentLap,
  "type": "SPEED_MEASUREMENT"
 }
```

LANE_CHANGED
```json
{
  "demozone": demozone,
  "deviceId": piId,
  "dateTime": int(time.time()),
  "dateTimeString": dateTimeString,
  "raceStatus": raceStatus,
  "raceId": raceCount,
  "type": "LANE_CHANGED",
  "carId": myDeviceAddress,
  "carName": myCarName,
  "lap": currentLap
}
```

LAP_COMPLETED
```json
{
  "demozone": demozone,
  "deviceId": piId,
  "dateTime": int(time.time()),
  "dateTimeString": dateTimeString,
  "raceStatus": raceStatus,
  "raceId": raceCount,
  "carId": myDeviceAddress,
  "carName": myCarName,
  "lap": currentLap,
  "lapTime": lapTime,
  "type": "LAP_COMPLETED"
}
```
CAR_TRANSITIONED
```json
{
  "demozone": demozone,
  "deviceId": piId,
  "dateTime": int(time.time()),
  "dateTimeString": dateTimeString,
  "raceStatus": raceStatus,
  "raceId": raceCount,
  "carId": myDeviceAddress,
  "carName": myCarName,
  "trackStyle": trackStyle,
  "trackSegment": trackSegment,
  "lap": currentLap,
  "type": "CAR_TRANSITIONED"
}
```
VEHICLE_DELOCALIZED
```json
{
  "demozone": demozone,
  "deviceId": piId,
  "dateTime": int(time.time()),
  "dateTimeString": dateTimeString,
  "raceStatus": raceStatus,
  "raceId": raceCount,
  "carId": myDeviceAddress,
  "carName": myCarName,
  "lap": currentLap,
  "type": "VEHICLE_DELOCALIZED",
  "lastKnownTrack": tentative_offtrack_position
}
```