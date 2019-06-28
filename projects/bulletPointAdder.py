#! /usr/local/bin/env python3

# bulletPointAdder.py - Adda Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars

pyperclip.copy(text)
