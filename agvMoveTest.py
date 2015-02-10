import serial
import struct

dir_L = input("Direction of the left wheel [0 or 250]: ")
vel_L = input("Velocity of the left wheel [uint8]: ")
dir_R = input("Direction of the right wheel [0 or 250]: ")
vel_R = input("Velocity of the right wheel [uint8]: ")

values = (35,dir_L,0,vel_L,0,dir_R,0,vel_R,0,33)
string = ''

for i in values:
	string += struct.pack('B',i)

port = serial.Serial("/dev/ttyUSB0", baudrate = 9600, bytesize = 8, stopbits = 1, timeout = 2)
port.open()

for i in range(0, 150):
	port.write(string)
	
port.close()

print("End...")
