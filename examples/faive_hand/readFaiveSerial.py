import faive_hand_pb2
import sys
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
hand = faive_hand_pb2.Hand()
finger = faive_hand_pb2.Finger()
event = faive_hand_pb2.Event()

while True:
    datastr = ser.readline().decode('utf-8')

    data = bytes.fromhex(datastr)

    event.ParseFromString(data)

    if event.type == 1:
        print("Reading Hand Data")
        hand = event.handdata
        thumb = hand.fingers[0]
        for finger in hand.fingers:
            print("Finger: ", finger.type)
            for sensor in finger.sensors:
                if sensor.type:
                    print("   Sensor: ", sensor.type)
                    for data in sensor.data:
                        if data.value:
                            print("      Data axs: ", data.axis)
                            print("      Data val: ", data.value)
    elif event.type == 2:
        print("Reading Finger Data")
        finger = event.fingerdata
        for sensor in finger.sensors:
                if sensor.type:
                    print("   Sensor: ", sensor.type)
                    for data in sensor.data:
                        if data.value:
                            print("      Data axs: ", data.axis)
                            print("      Data val: ", data.value)

    time.sleep(1)
    break