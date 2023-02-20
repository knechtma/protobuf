import faive_hand_pb2
import sys
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
hand = faive_hand_pb2.Hand()

# instr = '\n:\n\x05thumb\x10\x01\x1a\x17\n\x06HE_MCP\x10\x01"\x0b\x08\x01\x11q=\n\xd7\xa3\xb0(@\x1a\x16\n\x03FSR\x10\x01\x18\x02"\x0b\x08\x01\x11H\xe1z\x14\xae\xf9\x80@'

# hand.ParseFromString(instr)

while True:
    data = ser.readline()
    hand.ParseFromString(data)
    thumb = hand.fingers[0]
    print(thumb.type)
    HE1 = thumb.sensors[0]
    print(HE1.type)
    print(HE1.data[0].value)
    time.sleep(1)