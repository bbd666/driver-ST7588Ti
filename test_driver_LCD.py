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
lcd.draw_rectangle(100,20,140,10,1,1,2)
lcd.draw_text(80,60,"HELLO WORLD",None,'/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',12,"ms',0,"left")
lcd.refresh()
#GPIO.cleanup()

