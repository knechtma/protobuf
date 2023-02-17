import faive_hand_pb2
import sys
import serial
import time

hand = faive_hand_pb2.Hand()

thumb = hand.fingers.add()
thumb.id = 1
thumb.name = "thumb"
thumb_HE1 = thumb.sensors.add()
thumb_HE1.id = 1
thumb_HE1.name = "HE_MCP"
thumb_HE1.type = faive_hand_pb2.Sensor.HES
thumb_HE1_Dat1 = thumb_HE1.data.add()
thumb_HE1_Dat1.axis = 1
thumb_HE1_Dat1.value = 12.345
thumb_FSR = thumb.sensors.add()
thumb_FSR.id = 1
thumb_FSR.name = "FSR"
thumb_FSR.type = faive_hand_pb2.Sensor.FSR
thumb_FSR_Dat = thumb_FSR.data.add()
thumb_FSR_Dat.axis = 1
thumb_FSR_Dat.value = 543.21


ser = serial.Serial('/dev/ttyACM0', 9600)
ser.close()

while True:
    ser.open()
    outstr = hand.SerializeToString()
    print(outstr)
    # ser.write(outstr)
    ser.close()
    time.sleep(3)
