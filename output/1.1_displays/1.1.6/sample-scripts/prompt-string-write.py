from RPLCD.i2c import CharLCD
import time

# Modify the I2C address (0x27) if necessary
lcd = CharLCD('PCF8574', 0x27)

def main():
    while True:
        # Prompt for user input
        user_input = input("Enter a string to display on the LCD (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        # Clear the display
        lcd.clear()

        # Write the user input to the LCD
        lcd.write_string(user_input)

        # Optionally, you can wait a bit before prompting again
        time.sleep(2)

    # Clear the display before exiting
    lcd.clear()

if __name__ == "__main__":
    main()
