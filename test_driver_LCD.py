from datetime import datetime
from driver_LCD import LcdDisplay
import time
from time import sleep
from PIL import Image, ImageDraw,ImageFont

now=datetime.now()
lastnow=datetime.now()
time_var=["",""]
date_var=["",""] 

def set_time(arg):
    now = datetime.now()
    global time_var
    global date_var
    time_var[arg] = now.strftime('%H:%M:%S')
    date_var[arg] = now.strftime("%d/%m/%Y")      

lcd=LcdDisplay()
lcd.set_intensity(0.5)
image_raw=Image.open("logo.bmp")
image=image_raw.resize((132,80),Image.LANCZOS)

image1=Image.new('1',(132,80))

image2_raw=Image.open("logo1.bmp")
image2=image2_raw.resize((132,80),Image.LANCZOS)

i=0
while (1):
	if (i%2==4):
		lcd.draw_rectangle(60,20,120,10,1,1,2)
		lcd.update_display()   
	if (i%2==3):
		lcd.draw_rectangle(60,60,120,70,1,1,2)
		lcd.update_display()   
#	if (i%2==0):
	if i==0:
		lcd.load_image(image)
		lcd.update_display()   
	if (i%2==2):
		lcd.load_image(image2)
		lcd.update_display()

#	if (i%2==1):
	if i==-1:
		lcd.load_image(image1)
		#lcd.draw_text(80,60,"HELLO WORLD",1,"/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",12,"ms",0,"left")
		lcd.draw_rectangle(30,60,130,70,1,1,2)
		lcd.draw_text(80,70,"HELLO WORLD",0,"/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",12,"ms",0,"left")
		#lcd.update_display()   
		lcd.update_submap(7,10)
		now=datetime.now()
	now=datetime.now()
	deltat=now-lastnow
	if (deltat.microseconds>950000):
			set_time(0)
			lcd.draw_rectangle(30,60,130,70,0,0,2)
			lcd.draw_rectangle(30,10,130,20,0,0,2)
			lcd.draw_text(85,20,date_var[0],1,"/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",12,"ms",0,"left")
			lcd.draw_text(80,70,time_var[0],1,"/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",12,"ms",0,"left")
#			lcd.update_area(55,120,1,4)
			lcd.update_area(50,107,7,9)
			#lcd.update_display()
	i=i+1
		
