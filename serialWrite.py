import serial
import struct

values = (35,0,0,250,0,250,0,250,0,33)
string = ''

for i in values:
	string += struct.pack('B',i)

#newstr = "#"+string+"!"

print string
print values
port = serial.Serial("/dev/ttyUSB0", baudrate = 9600, bytesize = 8, stopbits = 1, timeout = 2)
port.open()

for i in range(0, 50):
	port.write(string)
	
print "%d" % i
data = port.read(30)
print data
port.close()
print"""Good
Bye"""
