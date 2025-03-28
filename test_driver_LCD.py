from driver_LCD import LcdDisplay
import time
from time import sleep
from PIL import Image, ImageDraw,ImageFont

lcd=LcdDisplay()
lcd.clean_display()
lcd.set_intensity(0.5)
image_raw=Image.open("logo.bmp")
image=image_raw.resize((132,80),Image.LANCZOS)
lcd.load_image(image)
lcd.draw_rectangle(50,20,40,30,0,1)
#lcd.draw_text(10,20,"HELLO WORLD",1,10,1)
lcd.refresh()
#GPIO.cleanup()

