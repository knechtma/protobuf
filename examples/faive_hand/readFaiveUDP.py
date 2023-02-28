import faive_hand_pb2
import sys
import serial
import time
from socket import *

address = ('192.168.0.143', 5000)
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.bind(('192.168.0.144', 5000))

client_socket.settimeout(1)

def sendCmdUDP(command):
    """
    send a command via UDP
    """
    message = command.SerializeToString()
    try: 
        client_socket.sendto(message, address)
        return True
    except:
        pass
    return False

def initMotor(motorID, driverID, CSpin, Output):
    """
    initialize a motor
    """
    command = faive_hand_pb2.Event()
    command.type = 8
    for i in range(16): # data structure needs all motors for nanopb to work
        command.motordata.motors.add()
    cmdmotdat = command.motordata.motors[0]
    cmdmotdat.motorid = motorID
    cmdmotdat.driverid = driverID
    cmdmotdat.CS_pin = CSpin
    cmdmotdat.Output = Output
    sendCmdUDP(command)

def setMotorSpeed(motor, speed):
    """
    set the speed of a motor
    """
    command = faive_hand_pb2.Event()
    command.type = 4
    cmdmetadat = command.metadata
    cmdmetadat.id = motor
    cmdmetadat.value = speed
    sendCmdUDP(command)

def setMotorMode(motor, mode):
    """
    set the mode of a motor
    """
    command = faive_hand_pb2.Event()
    command.type = 3
    cmdmetadat = command.metadata
    cmdmetadat.id = motor
    cmdmetadat.value = mode
    sendCmdUDP(command)

def readUDP():
    event = faive_hand_pb2.Event()
    try:
        rec_data, addr = client_socket.recvfrom(1024)
        event.ParseFromString(rec_data)
        return True, event
    except:
        pass
    return False, event

def decodeCommand(event):
    if event.type == 1:
        print("Reading Hand Data")
        hand = event.handdata
        # thumb = hand.fingers[0]
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



def main():

    # hand = faive_hand_pb2.Hand()
    # finger = faive_hand_pb2.Finger()
    # event = faive_hand_pb2.Event()

    # fingdat = faive_hand_pb2.Event()
    # fingdat.type = 2

    # motmode = faive_hand_pb2.Event()
    # motmode.type = 4
    # motmodemeta = motmode.metadata
    # motmodemeta.id = 0
    # motmodemeta.value = 1


    # while True:
    #     success, event = readUDP()
    #     if success:
    #         decodeCommand(event)
        
    #     time.sleep(0.5)

    #     setMotorMode(0, 1)

    time.sleep(1)
    initMotor(0, 0, 10, 1)
    time.sleep(0.1)
    initMotor(1, 0, 10, 2)
    time.sleep(0.1)
    setMotorMode(0, 1)
    time.sleep(0.1)
    setMotorMode(1, 1)
    time.sleep(0.1)
    setMotorSpeed(0, 0.5)
    time.sleep(0.1)
    setMotorSpeed(1, 0.5)
    time.sleep(1)
    setMotorSpeed(0, 0)
    time.sleep(1)
    setMotorMode(0,2)
    time.sleep(0.1)
    setMotorSpeed(0,0.5)
    time.sleep(1)
    setMotorSpeed(0, 0)
    time.sleep(0.1)
    setMotorSpeed(1, 0)
    time.sleep(0.1)
    setMotorMode(0, 0)
    time.sleep(0.1)
    setMotorMode(1, 3)
    time.sleep(1)
  

if __name__ == "__main__": 
    main()

