#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
import time
import Adafruit_CharLCD as LCD

class lcd_display: 
    def __init__(self):
        lcd_rs = 2
        lcd_en = 3
        lcd_d4 = 4
        lcd_d5 = 17
        lcd_d6 = 27
        lcd_d7 = 22
        lcd_backlight = 2
    
        # Define LCD column and row size for 16x2 LCD.
        lcd_columns = 16
        lcd_rows = 2
    
        # Define LCD Object
        self.lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
    
    def display(self, text):
        self.lcd.clear()
        self.lcd.message(text)
