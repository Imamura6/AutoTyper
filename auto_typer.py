"""
Basic code that implements pynput to auto type a pre defined text
"""

import time
from pynput.keyboard import Key, Controller


class AutoTyper():
    """
    Class that simulates the typing action of a pre defined text
    """

    def __init__(self, words_per_minute=1000):
        self.char_delay = 0
        self.calculate_typing_speed(words_per_minute)
        self.keyboard = Controller()

    def calculate_typing_speed(self, words_per_minute):
        """
        Function that calculates the delay between chars to achive the typing speed inputed
        """
        char_per_minute = words_per_minute*5
        self.char_delay = round(60/char_per_minute, 2)

    def type_sentence(self, sentence):
        """
        Function that types a sentence in the selected window
        """
        for char in sentence:
            if char in ('\r', '\n', '\r\n'):
                self.keyboard.press(Key.enter)
                self.keyboard.release(Key.enter)
            else:
                self.keyboard.press(char)
                self.keyboard.release(char)
            time.sleep(self.char_delay)

    def type_text_file(self, file_path):
        """
        Function that types all the content of a text file in the selected window
        """
        with open(file_path, 'r') as file:
            for line in file:
                self.type_sentence(line)


if __name__ == "__main__":
    time.sleep(3)
    AUTO_TYPER = AutoTyper()
    AUTO_TYPER.type_text_file("./test")
