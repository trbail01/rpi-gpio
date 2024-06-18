from RPLCD.i2c import CharLCD
import time
import random

# Initialize the LCD with the I2C address (0x27). Modify the address if necessary.
lcd = CharLCD('PCF8574', 0x27)


def display_message(message, delay=2):
    """
    Function to display a message on the LCD screen and wait for a specified delay.

    Args:
    message (str): The message to display.
    delay (int): The time in seconds to display the message. Default is 2 seconds.
    """
    lcd.clear()
    lcd.write_string(message)
    time.sleep(delay)


def main():
    # Set the range for the guessing game
    lower_bound = 1
    upper_bound = 100

    # Generate a random number between lower_bound and upper_bound
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    display_message("Guess a number\nbetween 1 and 100")
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
                display_message("Out of range!\nTry again")
            elif guess < number_to_guess:
                display_message("Too low!\nTry again")
            elif guess > number_to_guess:
                display_message("Too high!\nTry again")
            else:
                display_message(f"Correct! {attempts}\nattempts")
                break
        except ValueError:
            display_message("Invalid input!\nTry again")

    # Clear the display before exiting
    lcd.clear()


if __name__ == "__main__":
    main()
