#!/usr/bin/python3
""" 
Function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Summary:
        This function takes a string as input and prints it with 2 new lines
        after each of these characters: ., ?, and :

    Args:
        text (str): A string that is to be printed with 2 new lines
            after each of these characters: ., ?, and :

    Raises:
        TypeError: If the input is not a string, the function will raise
            a TypeError exception with the message "text must be a string".
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indent = False
    for char in text:
        if char in "?.:":
            print(char, end="\n\n")
            indent = True
        elif char == " " and indent:
            continue
        else:
            print(char, end="")
            indent = False
