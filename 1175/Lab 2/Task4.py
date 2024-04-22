from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
colors = [[255,0,0],
	[255,127,0],
	[255,255,0],
	[0,255,0],
	[0,0,255],
	[75,0,130],
	[148,0,211],
	[255, 255, 255],
	[148,0,211],
	[75,0,130],
	[0,0,255],
	[0,255,0],
	[255,255,0],
	[255,127,0],
	[255,0,0]]
e = [0,0,0]

while True:
    for val in range(15):
        sleep(.1)
        for i in range(8):
            for j in range(8):
                if(i+j == val):
                    sense.set_pixel(i,j,colors[val])
                else:
                    sense.set_pixel(i,j, e)