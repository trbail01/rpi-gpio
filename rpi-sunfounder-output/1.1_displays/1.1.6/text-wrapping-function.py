from RPLCD.i2c import CharLCD
import time

# Modify the I2C address (0x27) if necessary
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

def wrap_text(text, line_length):
    lines = []
    while len(text) > line_length:
        # Find the last space within the line length limit
        wrap_at = text.rfind(' ', 0, line_length)
        if wrap_at == -1:
            wrap_at = line_length
        lines.append(text[:wrap_at])
        text = text[wrap_at:].strip()
    lines.append(text)
    return lines

def display_text(lcd, text):
    lcd.clear()
    lines = wrap_text(text, lcd.cols)
    for i, line in enumerate(lines[:lcd.rows]):
        lcd.cursor_pos = (i, 0)
        lcd.write_string(line)

def main():
    while True:
        # Prompt for user input
        user_input = input("Enter a string to display on the LCD (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        # Display the wrapped text on the LCD
        display_text(lcd, user_input)

        # Optionally, you can wait a bit before prompting again
        time.sleep(2)

    # Clear the display before exiting
    lcd.clear()

if __name__ == "__main__":
    main()
