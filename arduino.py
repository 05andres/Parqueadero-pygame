import serial
import simplejson

ser=serial.Serial('COM2',11334)
while True:
    jsonresult = ser.readline()
    try:
        jsonObject = simplejson.loads(jsonresult)
        print jsonObject["x"]
    except Exception:
        pass


