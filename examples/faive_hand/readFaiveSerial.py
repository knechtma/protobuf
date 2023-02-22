import faive_hand_pb2
import sys
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
hand = faive_hand_pb2.Hand()

while True:
    datastr = ser.readline().decode('utf-8')

    data = bytes.fromhex(datastr)

    hand.ParseFromString(data)

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
    print(hand.fingers.type)
    print(thumb.type)
    HE1 = thumb.sensors[0]
    print(HE1.type)
    print(HE1.data[0].value)
    time.sleep(1)
    break