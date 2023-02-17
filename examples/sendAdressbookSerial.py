import addressbook_pb2
import sys
import serial
import time


address_book = addressbook_pb2.AddressBook()

person1 = address_book.people.add()
person1.id = 1
person1.name = "John Doe"
person1.email = "jonny@email.com"
phone1 = person1.phones.add()
phone1.number = "555-555-5555"
phone1.type = addressbook_pb2.Person.MOBILE


ser = serial.Serial('/dev/ttyACM0', 9600)
ser.close()

while True:
    ser.open()
    ser.write(address_book.SerializeToString())
    ser.close()
    time.sleep(3)
