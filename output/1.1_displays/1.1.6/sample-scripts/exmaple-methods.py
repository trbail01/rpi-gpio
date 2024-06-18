from RPLCD.i2c import CharLCD, CursorMode
import time

lcd = CharLCD('PCF8574', 0x27)

# Write a string
lcd.write_string('Hello, World!')

# Move cursor to the second row, first column
lcd.cursor_pos = (1, 0)
lcd.write_string('Raspberry Pi')

# Wait for 3 seconds
time.sleep(3)

# Clear the display
lcd.clear()

# Create a custom character (a smiley face)
smiley = [
    0b00000,
    0b01010,
    0b01010,
    0b00000,
    0b10001,
    0b01110,
    0b00000,
    0b00000
]
lcd.create_char(0, smiley)

# Display the custom character
lcd.write_string('\x00')

# Enable blinking cursor
lcd.cursor_mode = CursorMode.blink

# Wait for 3 seconds
time.sleep(3)

# Disable the cursor
lcd.cursor_mode = CursorMode.hide

# Turn off the backlight
lcd.backlight_enabled = False

# Turn on the backlight
lcd.backlight_enabled = True

# Clear the display before exit
lcd.clear()
