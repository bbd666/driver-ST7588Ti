# driver-ST7588Ti
driver I2C for LCD 132 x 80 ST7588Ti

Please find a driver for ST7588Ti LCD for use with Raspberry in python.
What you must know before using these devices :

They have 15 pins.
![Capture](https://github.com/user-attachments/assets/61439a8d-942d-42b4-a002-9dabcbb25eeb)
They have no Backlight embedded. In general the Backlight is mounted apart from the display onto the PCB. It is modulated with PWM.
It is powered on pin 11 (J2.GPIO 18) with 3.3V
But pin 1 and pin 10  (J2.GPIO 16) must also be powered with 12 V through PCB resistors.
![427439347-cea4614f-9ed3-4670-bb34-7aa08d37259c](https://github.com/user-attachments/assets/1c405e9e-23ca-4046-baca-3e314ba76796)

the RESET pin is useless in fact as the initialization is managed by hardware on the PCB (pin 15 (J2.GPIO 9)).
Then 2 channels for data transfers SDA and SDL on pins 13 (J2.GPIO 4) and pin 14 (J2.GPIO 6).

![Image1](https://github.com/user-attachments/assets/c55281dd-b286-48ab-beda-7a2a8743ba99)

The data sheets may be found here :
https://www.datasheetbank.com/pdf-view/ST7588TI-SITRONIX

and there :
https://www.digimax.it/media_import/DISPLAY/BOLYMIN/LCD%20GRAFICI/BO12864GGPHH$/BO12864GGPHH$_DS_001.pdf

# HOW TO INSTALL


This driver needs the PILLOW library to be present on the raspberry first. I think it's pre-installed by default on recent Raspbian packages. 
Otherwise, just run in a command prompt:

`python3 -m pip install --upgrade Pillow`

Complete information here :

https://pillow.readthedocs.io/en/stable/installation/basic-installation.html#basic-installation

It also requires the SMBUS3 library :

`pip install smbus3`

https://pypi.org/project/smbus3/

and the rpi hardware pwm lib :

pip install rpi-hardware-pwm

Then just copy the python script driver_ST5788Ti.py in your folder.
