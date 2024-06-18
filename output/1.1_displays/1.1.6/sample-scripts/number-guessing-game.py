from RPLCD.i2c import CharLCD
import time
import random

# Initialize the LCD with the I2C address (0x27). Modify the address if necessary.
lcd = CharLCD('PCF8574', 0x27, cols=27, rows=2)

def display_message(line1, line2='', delay=2):
    """
    Function to display a message on the LCD screen and wait for a specified delay.
    
    Args:
    line1 (str): The message to display on the first line.
    line2 (str): The message to display on the second line (optional).
    delay (int): The time in seconds to display the message. Default is 2 seconds.
    """
    lcd.clear()
    lcd.write_string(line1)
    if line2:
        lcd.crlf()  # Move to the second line
        lcd.write_string(line2)
    time.sleep(delay)

def main():
    # Set the range for the guessing game
    lower_bound = 1
    upper_bound = 100

    # Generate a random number between lower_bound and upper_bound
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    display_message("Guess a number", "between 1 and 100")
    time.sleep(3)  # Give the player some time to read the initial message

    while True:
        # Prompt the user for a guess
        user_input = input("Enter your guess (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        try:
            guess = int(user_input)
            attempts += 1

            if guess < lower_bound or guess > upper_bound:
                display_message("Out of range!", "Try again")
            elif guess < number_to_guess:
                display_message("Too low!", "Try again")
            elif guess > number_to_guess:
                display_message("Too high!", "Try again")
            else:
                display_message("Correct!", f"Attempts: {attempts}")
                break
        except ValueError:
            display_message("Invalid input!", "Try again")

    # Clear the display before exiting
    lcd.clear()

if __name__ == "__main__":
    main()
