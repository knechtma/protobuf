import simple_pb2
import sys
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
msg = simple_pb2.SimpleMessage()


while True:
    datastr = ser.readline().decode('utf-8')
    data = bytes.fromhex(datastr)

    msg.ParseFromString(data)
    print(msg.lucky_number)
    time.sleep(0.1)