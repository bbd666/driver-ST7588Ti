# driver-ST7588Ti
driver I2C for LCD 132 x 80 ST7588Ti

Please find a driver for ST7588Ti LCD and use for Raspberry in python.
What you must know before using these devices :

They have 15 pins.
They have no Backlight embedded. In general the Backlight device is added on the PCB. It is modulated with PWM.
It is powered on pin 11 (J2.GPIO 18) with 3.3V
But pin 1 and pin 10  (J2.GPIO 16) must also be powered with 16.5 V through PCB resistors.

![Capture d’écran 2025-03-26 152000](https://github.com/user-attachments/assets/6cd2a72b-ea2e-445a-938e-f9e54f03b725)

the RESET pin is useless in fact as the initialization is managed by hardware on the PCB (pin 15 (J2.GPIO 9)).
Then 2 channels for data transfers SDA and SDL on pins 13 (J2.GPIO 4) and pin 14 (J2.GPIO 6).

![AW-60i ](https://github.com/user-attachments/assets/036c5a92-7612-4f3e-97da-e4067c2e1561)

![Image1](https://github.com/user-attachments/assets/c55281dd-b286-48ab-beda-7a2a8743ba99)

The data sheets may be found here :
https://www.datasheetbank.com/pdf-view/ST7588TI-SITRONIX

and there :
https://www.digimax.it/media_import/DISPLAY/BOLYMIN/LCD%20GRAFICI/BO12864GGPHH$/BO12864GGPHH$_DS_001.pdf

# HOW TO INSTALL

This driver needs the PILLOW library to be present on the raspberry first. I think it's pre-installed by default on recent Raspbian packages. 
In case not,  just run

python3 -m pip install --upgrade Pillow

in a command prompt. Complete information here :
https://pillow.readthedocs.io/en/stable/installation/basic-installation.html#basic-installation

Then just copy the python script driver_ST5788Ti.py in your folder
