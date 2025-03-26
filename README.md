# driver-ST7588Ti
driver I2C for LCD 132 x 80 ST7588Ti

Please find a driver for ST7588Ti LCD and use in python.
What you must know before about these devices.
They have 15 pins.
They have no Backlight embedded. In general the Backlight device is added on the PCB. It is modulated with PWM.
It is powered on pin 11 with 3.3V
But pin 10 must also be powered with 16.5 V

![Capture d’écran 2025-03-26 152000](https://github.com/user-attachments/assets/6cd2a72b-ea2e-445a-938e-f9e54f03b725)

the RESET pin is useless in fact as the initialization is managed by hardware on the PCB (pin 15).
Then 2 channels for data transfers SDA and SDL on pins 16 and 14.

![AW-60i ](https://github.com/user-attachments/assets/036c5a92-7612-4f3e-97da-e4067c2e1561)

![Image1](https://github.com/user-attachments/assets/c55281dd-b286-48ab-beda-7a2a8743ba99)

The data sheets may be found here :
https://www.datasheetbank.com/pdf-view/ST7588TI-SITRONIX
and there :
https://www.digimax.it/media_import/DISPLAY/BOLYMIN/LCD%20GRAFICI/BO12864GGPHH$/BO12864GGPHH$_DS_001.pdf
