# driver-ST7588Ti
driver I2C for LCD 132 x 80 ST7588Ti

Please find a driver for ST7588Ti LCD for use with Raspberry in python.
What you must know before using these devices :

They have 15 pins.
![Capture](https://github.com/user-attachments/assets/61439a8d-942d-42b4-a002-9dabcbb25eeb)
They have no Backlight embedded. In general the Backlight is mounted apart from the screen onto the PCB. It is modulated with PWM.
It is powered on pin 11 (J2.GPIO 18) with 3.3V
But pin 1 and pin 10  (J2.GPIO 16) must also be powered with 9 V through PCB resistors. 9 V is the rated value, but I found 11 V gives better results (9 V wasn't enough to display things).

![436679464-1c405e9e-23ca-4046-baca-3e314ba76796](https://github.com/user-attachments/assets/7119a3b1-2e64-4b75-80e4-691998e042da)

the RESET pin is useless in fact as the initialization is managed by hardware on the PCB (pin 15 (J2.GPIO 9)).
Then 2 channels for data transfers SDA and SDL on pins 13 (J2.GPIO 4) and pin 14 (J2.GPIO 6).
the SDA and SCL pins must be pulled-up :
![Capture d’écran 2025-06-30 095724](https://github.com/user-attachments/assets/426a993b-69a4-4408-a071-da047552ef11)


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

It also requires the smbus library which should be present by default. In case it isn't :

`sudo apt-get install python3-smbus`


Then just copy the python script driver_LCD.py in your folder.
