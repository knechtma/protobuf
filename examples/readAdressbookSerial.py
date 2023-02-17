import addressbook_pb2
import sys
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
address_book = addressbook_pb2.AddressBook()

while True:
    data = ser.readline()
    address_book.ParseFromString(data)
    jonny = address_book.people[0]
    print(jonny.name)
    print(jonny.email)