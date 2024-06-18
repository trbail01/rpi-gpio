# Import the CharLCD class from the RPLCD.i2c module to control the LCD display
from RPLCD.i2c import CharLCD
import time  # Import the time module to use the sleep function

# Initialize the LCD with the I2C address (0x27). Modify the address if necessary.
lcd = CharLCD('PCF8574', 0x27)

def main():
    # Infinite loop to continually prompt for user input
    while True:
        # Prompt the user to enter a string to display on the LCD
        user_input = input("Enter a string to display on the LCD (or 'exit' to quit): ")

        # Check if the user input is 'exit' (case-insensitive)
        if user_input.lower() == 'exit':
            break  # Exit the loop if the user wants to quit

        # Clear the LCD display before writing new content
        lcd.clear()

        # Write the user input to the LCD display
        lcd.write_string(user_input)

        # Wait for 2 seconds before prompting the user again
        time.sleep(2)

    # Clear the LCD display before exiting the program
    lcd.clear()

# Entry point of the program. Run the main function if this script is executed directly.
if __name__ == "__main__":
    main()
