import serial


values = (65,0,250,0,250,0,250,0)

port = serial.Serial("/dev/ttyUSB0", baudrate = 9600, bytesize = 8, stopbits = 1, timeout = 2)
port.open()

for i in range(0, 50):
	port.write("125")
	print "%d" % i

port.close()
print"""Good
Bye"""
