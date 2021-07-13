
import I2C_LCD_driver
import time


mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hello World!", 1)
time.sleep(1)




while True:
    mylcd.lcd_display_string("Time: %s" %time.strftime("%H:%M:%S"), 1)
    mylcd.lcd_display_string("Date: %s" %time.strftime("%m/%d/%Y"), 2)
