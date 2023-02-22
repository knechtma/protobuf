import simple_pb2
import sys
import serial
import time
import binascii

ser = serial.Serial('/dev/ttyACM0', 9600)
msg = simple_pb2.SimpleMessage()


while True:
    datastr = ser.readline()
    data = binascii.a2b_hex(datastr)

    msg.ParseFromString(data)
    print(msg.lucky_number)
    time.sleep(0.1)

    # data = b'082A' # input data from serial
    # print(data)
    # print(type(data))

    # datastr = data.decode('utf-8') # convert to string
    # print(datastr)
    # print(type(datastr))

    # databy = bytes.fromhex(datastr) # convert back to bytes in hex format
    # print(databy)
    # print(type(databy))

    # datbin = binascii.a2b_hex(data) # alternative without conversion to string
    # print(datbin)
    # print(type(datbin))

    # msg.ParseFromString(databy)
    # print(msg.lucky_number)
    # break