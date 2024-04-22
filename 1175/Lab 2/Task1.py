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
image_red=[r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r,
	r,r,r,r,r,r,r,r]

#Task 1

while True:
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