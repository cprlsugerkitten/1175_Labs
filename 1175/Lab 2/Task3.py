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
	[255, 255, 255]]
while True:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        x = round(x)
        y = round(y)
        z = round(z)

        #handling x-axis
        if x==1:
            for col in range(8):
                color=colors[col]
                for row in range(8):
                    sense.set_pixel(col, row, color)
                sleep(0.05)
                sense.clear()
        elif x==-1:
            for col in range(8):
                color=colors[col]
                for row in range(8):
                    sense.set_pixel(7-col, row, color)
                sleep(0.05)
                sense.clear()
        elif y==1:
            for row in range(8):
                color=colors[row]
                for col in range(8):
                    sense.set_pixel(col, row, color)
                sleep(0.05)
                sense.clear()
        elif y==-1:
            for row in range(8):
                color=colors[row]
                for col in range(8):
                    sense.set_pixel(col, 7-row, color)
                sleep(0.05)
                sense.clear()
        elif z==1:
            message = "Pi is facing up!"
            sense.show_message(message, scroll_speed=.05)
            sleep(0.05)
            sense.clear()
        elif z==-1:
            print("Pi is facing down :(")
            
