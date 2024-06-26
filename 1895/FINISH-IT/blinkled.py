import digitalio
import board
import textwrap
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789 # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357 # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735 # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351 # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331 # pylint: disable=unused-import




	# First define some constants to allow easy resizing of shapes.
BORDER = 20
FONTSIZE = 24
FONTSIZE = 24


#dc->gpio22



# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D22)
reset_pin = digitalio.DigitalInOut(board.D24)
# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000
# Setup SPI bus using hardware SPI:
spi = board.SPI()
# pylint: disable=line-too-long
# Create the display:
# disp = st7789.ST7789(spi, rotation=90, # 2.0" ST7789
# disp = st7789.ST7789(spi, height=240, y_offset=80, rotation=180, # 1.3", 1.54" ST7789
# disp = st7789.ST7789(spi, rotation=90, width=135, height=240, x_offset=53, y_offset=40, # 1.14"
# disp = hx8357.HX8357(spi, rotation=180, # 3.5" HX8357
# disp = st7735.ST7735R(spi, rotation=90, # 1.8" ST7735R
# disp = st7735.ST7735R(spi, rotation=270, height=128, x_offset=2, y_offset=3, # 1.44" ST7735R
# disp = st7735.ST7735R(spi, rotation=90, bgr=True, # 0.96" MiniTFT ST7735R
# disp = ssd1351.SSD1351(spi, rotation=180, # 1.5" SSD1351
# disp = ssd1351.SSD1351(spi, height=96, y_offset=32, rotation=180, # 1.27" SSD1351
# disp = ssd1331.SSD1331(spi, rotation=180, # 0.96" SSD1331
disp = ili9341.ILI9341(
spi,
rotation=90, # 2.2", 2.4", 2.8", 3.2" ILI9341
cs=cs_pin,
dc=dc_pin,
rst=reset_pin,
baudrate=BAUDRATE,
)
# pylint: enable=line-too-long
# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
if disp.rotation % 180 == 90:
	height = disp.width # we swap height/width to rotate it to landscape!
	width = disp.height
else:
	width = disp.width # we swap height/width to rotate it to landscape!
	height = disp.height
image = Image.new("RGB", (width, height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# Draw a green filled box as the background
draw.rectangle((0, 0, width, height), fill=(239, 141, 175))
disp.image(image)
# Draw a smaller inner purple rectangle
draw.rectangle(
(BORDER, BORDER, width - BORDER - 1, height - BORDER - 1), fill=(152, 47, 170)
)
# Load a TTF Font

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)
# Draw Some Text

#(font_width, font_height) = font.getsize(text)
# draw.text(
# (width // 2 - 10 // 2, height // 2 - 10 // 2),
# text,
# font=font,
# fill=(255, 255, 0),
# )


# Calculate text size and position
def displayLCD(score,command,text):
	

	draw.text((200,20), 'Score: '+score, font=font, fill=(255,255,0))
	draw.text((20,20), '*Dance To It*', font=font, fill=(255,255,0))
	draw.text((20,22),  '_____________',font=font, fill=(255,255,0))
	
	draw.text((75,75),command, font=font, fill=(255,255,0))
	
	text=textwrap.wrap(text,width=20)
#	(font_width,font_height)=font.getSize(text);
	
	for i,character in enumerate(text):
		newheight=125+20*i
		draw.text((width/2-len(character)*6, newheight), character, font=font, fill=(255, 255, 0))


	# Display image.
	disp.image(image)


displayLCD('0','Finish The Lyric:','i believe i can fly, i believe i can touch the ___')
