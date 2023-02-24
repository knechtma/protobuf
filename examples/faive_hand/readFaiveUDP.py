import faive_hand_pb2
import sys
import serial
import time
from socket import *

address = ('192.168.0.143', 5000)
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)
hand = faive_hand_pb2.Hand()
finger = faive_hand_pb2.Finger()
event = faive_hand_pb2.Event()
command = faive_hand_pb2.Event()
# message = b'Hello, world!'
# time.sleep(1.5)


command.type = 2
message = command.SerializeToString()
print(message)

try: 
    # print("Try to send data")
    client_socket.sendto(message, address)
except:
    pass
# print("Sent data")

time.sleep(0.5)

while True:
    try:
        # print("Try to read data")
        rec_data, addr = client_socket.recvfrom(1024)
        print("Received data")
        # print(rec_data)
        # print(type(rec_data))
        # data = rec_data
        # print(type(data))
        event.ParseFromString(rec_data)

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
    except:
        pass

    # print(data)

    # datastr = ser.readline().decode('utf-8')

    # data = bytes.fromhex(datastr)

    # event.ParseFromString(data)

    # if event.type == 1:
    #     print("Reading Hand Data")
    #     hand = event.handdata
    #     thumb = hand.fingers[0]
    #     for finger in hand.fingers:
    #         print("Finger: ", finger.type)
    #         for sensor in finger.sensors:
    #             if sensor.type:
    #                 print("   Sensor: ", sensor.type)
    #                 for data in sensor.data:
    #                     if data.value:
    #                         print("      Data axs: ", data.axis)
    #                         print("      Data val: ", data.value)
    # elif event.type == 2:
    #     print("Reading Finger Data")
    #     finger = event.fingerdata
    #     for sensor in finger.sensors:
    #             if sensor.type:
    #                 print("   Sensor: ", sensor.type)
    #                 for data in sensor.data:
    #                     if data.value:
    #                         print("      Data axs: ", data.axis)
    #                         print("      Data val: ", data.value)

    # time.sleep(1)
    time.sleep(0.5)

    try: 
        # print("Try to send data")
        client_socket.sendto(message, address)
    except:
        pass
    # print("Sent data")

    time.sleep(0.5)


    # break