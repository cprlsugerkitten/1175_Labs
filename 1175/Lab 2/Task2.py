from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
r = (255,0,0)
b = (0, 0, 255)
e = (0, 0, 0)
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
image_red=[r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r]
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
sense.set_pixels(image_red)
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