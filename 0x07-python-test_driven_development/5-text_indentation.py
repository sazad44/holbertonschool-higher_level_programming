#!/usr/bin/python3
"""Text Indentation Module

This module prints the lines of a string with two newlines following ., :, ?.
Attributes: text_indentation(text)
"""


def text_indentation(text):
    flag = 1
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        text = text.strip()
        for i in text:
            if flag == 1 and i == " ":
                continue
            else:
                flag = 0
            print(i, end="")
            if i in ['.', ':', '?']:
                print("\n")
                flag = 1
