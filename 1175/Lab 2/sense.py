from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

b = (0, 0, 255)
e = (0, 0, 0)
r = (255,0,0)

image = [e,e,e,e,b,e,e,e,
	 e,e,e,e,b,e,e,e,
	 e,e,e,e,b,e,e,e,
	 e,e,e,e,b,e,e,e,
	 e,e,e,e,b,e,e,e,
	 e,e,e,b,b,b,e,e,
	 e,e,e,b,b,b,e,e,
	 e,e,e,b,b,b,e,e]


image2_l =[e,e,e,e,b,e,e,e,
	   e,e,e,e,b,e,e,e,
	   e,e,e,e,b,e,e,e,
	   e,e,e,b,e,e,e,e,
	   e,e,e,b,e,e,e,e,
	   e,e,b,b,b,e,e,e,
	   e,e,b,b,b,e,e,e,
	   e,e,b,b,b,e,e,e]
image3_l =[e,e,e,e,b,e,e,e,
	   e,e,e,e,b,e,e,e,
	   e,e,e,b,e,e,e,e,
	   e,e,b,e,e,e,e,e,
	   e,b,b,b,e,e,e,e,
	   e,b,b,b,e,e,e,e,
	   e,b,b,b,e,e,e,e,
	   e,e,e,e,e,e,e,e]
image2_r=[e,e,e,e,b,e,e,e,
	  e,e,e,e,b,e,e,e,
	  e,e,e,e,b,e,e,e,
	  e,e,e,e,e,b,e,e,
	  e,e,e,e,e,b,e,e,
	  e,e,e,e,b,b,b,e,
	  e,e,e,e,b,b,b,e,
	  e,e,e,e,b,b,b,e]
image3_r=[e,e,e,e,b,e,e,e,
	  e,e,e,e,b,e,e,e,
	  e,e,e,e,e,b,e,e,
	  e,e,e,e,e,e,b,e,
	  e,e,e,e,e,b,b,b,
	  e,e,e,e,e,b,b,b,
	  e,e,e,e,e,b,b,b,
	  e,e,e,e,e,e,e,e]


#Task 1
def task_1():
	for i in range(1):
		sense.set_pixels(image)
		sleep(.5)
		sense.set_pixels(image2_l)
		sleep(.5)
		sense.set_pixels(image3_l)
		sleep(.5)
		sense.set_pixels(image2_l)
		sleep(.5)
		sense.set_pixels(image)
		sleep(.5)
		sense.set_pixels(image2_r)
		sleep(.5)
		sense.set_pixels(image3_r)
		sleep(.5)
		sense.set_pixels(image2_r)
		sleep(.5)
		
	sense.set_pixels(image)

#task_1()
#Task 2
#direction - up, left, down, right,
#action - held, released, pressed
def task_2():
	while True:
		for event in sense.stick.get_events():
			if event.action == "released":
				sense.set_pixels(image_red)
			elif event.direction == "left":
				message = f"Temperature = {sense.get_temperature()}"
				sense.show_message(message, scroll_speed=.05)
			elif event.direction == "right":
				message = f"Pressure = {sense.get_pressure()}"
				sense.show_message(message, scroll_speed=.05)
			elif event.direction == "up":
				message = f"Humidity = {sense.get_humidity()}"
				sense.show_message(message, scroll_speed=.05)
			elif event.direction == "down":
				task_1()
				

#task_2()

#Task 3
colors = [[255,0,0],
	[255,127,0],
	[255,255,0],
	[0,255,0],
	[0,0,255],
	[75,0,130],
	[148,0,211],
	[255, 255, 255]]
def task_3():
    while True:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        x = round(x,1)
        y = round(y,1)
        z = round(z,1)
    
        temp_x = abs(x)
        temp_y = abs(y)
        temp_z = abs(z)
        #handling x-axis
        if x!=0:

            for col in range(8):
                color=colors[col]
                for row in range(8):
                    if x>0:
                        sense.set_pixel(col, row, color)
                    else:
                        sense.set_pixel(7-col, row, color)
                
                sleep(0.05)
                sense.clear()
        if y!=0:
            for col in range(8):
                color=colors[col]
                for row in range(8):
                    if x>0:
                        sense.set_pixel(col, row, color)
                    else:
                        sense.set_pixel(col, 7-row, color)
                
                sleep(0.05)
                sense.clear()
        #handling z-axis
        if z > 0:
            message = "Pi is facing up!"
            sense.show_message(message, scroll_speed=.05)
        elif z>0:
            print("Pi is facing down :(")
        sleep(.1)

#task 4

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
def task_4():
    while True:
        for val in range(15):
            sleep(.1)
            for i in range(8):
                for j in range(8):
                    if(i+j == val):
                        sense.set_pixel(i,j,colors[val])
                    else:
                        sense.set_pixel(i,j, e)
                        

