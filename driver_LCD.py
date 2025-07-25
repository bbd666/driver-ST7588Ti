lib="busio"

if lib=="smbus":
	import smbus				    #smbus
else:
	if lib=="smbus3":
		from smbus3 import SMBus,i2c_msg	#smbus3
	else:
		import busio                #busio
		import board
    
import array    
import time
from time import sleep
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw, ImageFont

class LcdDisplay:
	def __init__(self,address=0x3f):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(18,GPIO.OUT)
		self.pwm = GPIO.PWM(18,40)
		self.FRAME_BUFFER=Image.new('1',(132,80))
		self.police1= ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
		self.SEND_COMMAND=0x00                       #A0=0
		self.SEND_DATA=0x40                          #A0=1
		self.SET_F=0x20
		self.SET_H01=self.SET_F | 0x01                            #H1=0 H0=1
		self.SET_H10=self.SET_F | 0x02                            #H1=1 H0=0
		self.SET_H00=self.SET_F | 0x00                            #H1=0 H0=0
		self.SET_H11=self.SET_F | 0x03                            #H1=1 H0=1
		self.SET_POWER_DOWN=self.SET_F | 0x04
		self.SOFTWARE_RESET=0x03
		self.SET_BIAS_9=0x12                         #BIAS=1/9  BS0=0  BS1=1 BS2=0
		self.SET_BIAS_10=0x11                        #BIAS=1/10 BS0=0  BS1=0 BS2=1
		self.SET_V0_LOWER_BITS=0x8f          #VOP0=VOP1=VOP2=VOP3=1 VOP4=VOP5=VOP6=0
		self.SET_V0_RANGE=0x05                       #PRS=1 => 9.198V(=8*0.042+8.862)
		self.SET_MSB=0x08                            #Bit de poids fort en haut (DO=0)
		self.SET_LSB=0x0c                            #Bit de poids fort en bas (DO=1)
		self.SET_VERTICAL_ADDRESSING=0x01
		self.SET_HORIZONTAL_ADDRESSING=0x00
		self.SET_NORMAL_DISPLAY=0x0c
		self.SET_DISPLAY_OFF=0x08
		self.SET_CHIP_DOWN=0x24
		self.SET_CHIP_ACTIVE=0x20
		self.SET_ALL_SEGMENTS_ON=0x09
		self.SET_INVERSE_VIDEO_MODE=0x0d
		self.SET_FRAME_50HZ=0x08
		self.SET_FRAME_73HZ=0x0b
		self.SET_FRAME_150HZ=0x0f
		self.SET_FULL_DISPLAY=0x04		
		self.SET_PARTIAL_DISPLAY=0x05
		
		Reset_Pin=4
		GPIO.setmode(GPIO.BCM)					#USELESS
		GPIO.setup(Reset_Pin,GPIO.OUT)			#USELESS
		GPIO.output(Reset_Pin,GPIO.LOW)			#USELESS
		time.sleep(0.05)
		GPIO.output(Reset_Pin,GPIO.HIGH)		#USELESS
		time.sleep(0.05)
		self.address=address
		if lib=="smbus":
			self.bus=smbus.SMBus(1)				        #smbus
		else:
			if lib=="smbus3":
				self.bus=SMBus(1)					    #smbus3
			else:
				self.i2c=busio.I2C(board.SCL,board.SDA) #busio
				while not self.i2c.try_lock():
					pass
		wrdata = [self.SET_H00]
		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
		time.sleep(0.05)
		wrdata = [self.SET_DISPLAY_OFF]
		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
		time.sleep(0.01)
		wrdata = [self.SET_H01]
		self.i2c_write (self.address,self.SEND_COMMAND,wrdata)
		time.sleep(0.001)
		wrdata = [self.SET_LSB|self.SET_HORIZONTAL_ADDRESSING]
		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
		wrdata = [self.SET_BIAS_9]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		time.sleep(0.001)
		wrdata = [self.SET_V0_LOWER_BITS]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		time.sleep(0.01)
		wrdata = [self.SET_H00]
		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
		time.sleep(0.01)
		wrdata = [self.SET_V0_RANGE]
		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
		time.sleep(0.05)
		wrdata = [self.SET_H11]
		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
		time.sleep(0.02)
		wrdata = [self.SET_FRAME_150HZ]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		time.sleep(0.01)
		wrdata = [self.SET_H10]
		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
		wrdata = [0x04]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		wrdata = [self.SET_H00]
		self.i2c_write(self.address,self.SEND_COMMAND,wrdata)
#		wrdata = [self.SET_ALL_SEGMENTS_ON]
#		self.i2c_write(self.address,self.SEND_COMMAND,wrdata)
#		wrdata = [self.SEND_COMMAND,self.SET_FULL_DISPLAY]
#		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
		wrdata = [self.SET_NORMAL_DISPLAY]
#		time.sleep(0.01)
		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
	
	def i2c_write (self,devaddr,regdata1,regdata2):
		attempt=False
		s=[]
		for i in range(len(regdata2)):
			s.append(regdata2[i])
		while not(attempt==True):
			try:
				if lib=="busio":
					self.i2c.writeto(devaddr,bytes([regdata1,s[0]]))
#					self.i2c.writeto(devaddr,bytes([regdata[0],regdata[1]]))	
				else:
#					self.bus.write_i2c_block_data(devaddr,0,regdata)	
#					self.bus.write_byte_data(devaddr,regdata[0],regdata[1])	
					self.bus.write_i2c_block_data(devaddr,regdata1,s)
#					msg=i2c_msg.write(devaddr,s)
#					self.bus.i2c_rdwr(msg)

				attempt=True
				return True
			except IOError:
				attempt=False
				return None

	def draw_pixel(self,x,y):
######### x colonne, y ligne  ####################################
		wrdata = [self.SET_H00]
		self.i2c_write(self.address,self.SEND_COMMAND,wrdata)
		wrdata = [self.SET_DISPLAY_OFF]
		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
		x=min(x,131)
		xlow=x & 0x0f
		xhigh=(0xf0 & x) >> 4
		wrdata = [0xe0|xlow]
		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
		wrdata = [0xf0|xhigh]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		ypage=y//10
		wrdata = [0x40|ypage]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		ysegment=2**(y%10)
		wrdata = [ysegment]
		self.i2c_write (self.address, self.SEND_DATA,wrdata)
		time.sleep(0.01)
		wrdata = [self.SET_NORMAL_DISPLAY]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)

	def draw_vert_segment(self,x,y):
######### x colonne, y ligne  ####################################
		wrdata = [self.SET_H00]
		self.i2c_write(self.address,self.SEND_COMMAND,wrdata)
		wrdata = [self.SET_DISPLAY_OFF]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		x=min(x,131)
		xlow=x & 0x0f
		xhigh=(0xf0 & x) >> 4
		wrdata = [0xe0|xlow]
		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
		wrdata = [0xf0|xhigh]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		ypage=y//10
		wrdata = [0x40|ypage]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		ysegment=2**(y%10)
		wrdata = [0xff]
		self.i2c_write (self.address,self.SEND_DATA, wrdata)
		time.sleep(0.01)
		wrdata = [self.SET_NORMAL_DISPLAY]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)

	def draw_area(self,map,x1,x2,y1,y2):
######### x colonne, y page  ####################################
		wrdata = [self.SET_H00]
		self.i2c_write(self.address,self.SEND_COMMAND,wrdata)
		wrdata = [self.SET_DISPLAY_OFF]
#		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		for j in range(y2-y1):
			for i in range(x2-x1):
				x=min(i+x1,131)
				xlow=x & 0x0f
				xhigh=(0xf0 & x) >> 4
				wrdata = [0xe0|xlow]
				self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
				wrdata = [0xf0|xhigh]
				self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
				ypage=(j+y1)
				wrdata = [0x40|ypage]
				self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
				ysegment=map[ypage*132+x]
				wrdata = [ysegment]
				self.i2c_write (self.address, self.SEND_DATA,wrdata)
		wrdata = [self.SET_NORMAL_DISPLAY]
#		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)

	def display_map(self,map):
		wrdata = [self.SET_H00]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		wrdata = [self.SET_DISPLAY_OFF]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		wrdata = [0xe0|0x00] #SET X ADDRESS (L)  0000
		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
		wrdata = [0xf0|0x00] #SET X ADDRESS (H)  0000
		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
		wrdata = [0x40|0x00] #SET Y ADDRESS      0000
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		wrdata = [0x07]      #READ / MODIFY / WRITE
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
#		for j in range(40):
#			wrdata=[]
#			for i in range(32):
#				wrdata.append(map[i+(j-1)*31])
#			self.i2c_write (self.address, self.SEND_DATA,wrdata)
		for i in range(1320):
			wrdata=[map[i]]
			self.i2c_write (self.address, self.SEND_DATA,wrdata)
		wrdata = [0x06]      #END
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		wrdata = [self.SET_NORMAL_DISPLAY]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)

	def display_submap(self,map,i_inf,i_max):
		wrdata = [self.SET_H00]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		wrdata = [self.SET_DISPLAY_OFF]
		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
		wrdata = [0xe0|0x00] #SET X ADDRESS (L)  0000
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		wrdata = [0xf0|0x00] #SET X ADDRESS (H)  0000
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		wrdata = [0x40|i_inf] #SET Y ADDRESS      0000
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)
		wrdata = [0x07]      #READ / MODIFY / WRITE
		self.i2c_write (self.address,self.SEND_COMMAND, wrdata)
		for i in range((i_max-i_inf)*132):
			wrdata = [map[i+i_inf*132]]
			self.i2c_write (self.address, wrdata)
		wrdata = [self.SEND_COMMAND,0x06]      #END
		self.i2c_write (self.address, self.SEND_DATA,wrdata)
		wrdata = [self.SET_NORMAL_DISPLAY]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)


	def clean_display(self):
		self.FRAME_BUFFER=Image.new('1',(132,80))
		
	def set_intensity(self,s):
		self.pwm.start(0)
		intensity=int(s*100)
		self.pwm.ChangeDutyCycle(intensity)

	def set_normal_display(self):
		wrdata = [self.SET_NORMAL_DISPLAY]
		self.i2c_write (self.address, self.SEND_COMMAND,wrdata)

	def tohex(self,image):
		res=[]
		for n in range(0,10):
			for x in range(0, 132):
				byte=""
				for y in range(8*n, 8*(n+1)):
					bit = "0"
					if  image.getpixel((x,y)) != 0:
						bit = "1"
					byte=byte+bit
					if y % 8 == 7:
						res.append(int(byte,2))
		return res

	def load_image(self,image):
		self.FRAME_BUFFER=image

	def update_display(self):
		map=self.tohex(self.FRAME_BUFFER)
		self.display_map(map)
		
	def update_submap(self,i_inf,i_max):
		map=self.tohex(self.FRAME_BUFFER)
		self.display_submap(map,i_inf,i_max)
		
	def update_area(self,i_inf,i_max,j_inf,j_max):
		map=self.tohex(self.FRAME_BUFFER)
		self.draw_area(map,i_inf,i_max,j_inf,j_max)

	def draw_rectangle(self,x1,y1,x2,y2, param_fill, param_outline, param_width):
	#param_outline=None or 1; Color to use for the outline
	#param_fill=None or 1; Color to use for the fill.
		draw=ImageDraw.Draw(self.FRAME_BUFFER)
		draw.rectangle([(x1,y1),(x2,y2)],fill=param_fill, outline=param_outline, width=param_width)		

	def draw_text(self,x,y,param_text,param_fill,font_file,font_size,param_anchor,param_spacing,param_align):
        #align must be “left”, “center” or “right”.
	#param_fill=None or 1; Color to use for the text.
        #spacing number of pixels between lines
		draw=ImageDraw.Draw(self.FRAME_BUFFER)
		police=ImageFont.truetype(font_file, font_size)
		draw.text((x,y),param_text,font=police,fill=param_fill,anchor=param_anchor,spacing=param_spacing,align=param_align)

	def draw_multiline_text(self,x,y,param_text,param_fill,font_file,font_size,param_anchor,param_spacing,param_align):
        #param_text contains all lines in one string. Line separator is \n
        #align must be “left”, “center” or “right”.
	#param_fill=None or 1; Color to use for the text.
        #spacing number of pixels between lines
		draw=ImageDraw.Draw(self.FRAME_BUFFER)
		police=ImageFont.truetype(font_file, font_size)
		draw.multiline_text((x,y),param_text,font=police,fill=param_fill,anchor=param_anchor,spacing=param_spacing,align=param_align)


