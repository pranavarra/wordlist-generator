import json
import tkinter.filedialog
import datetime

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
characters = ["!", "@", "#", "$", "%", "&"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

special_payloads = ["123", "00", "11", "!123", "@123", "#123", "&&", "!@#", "321", "@321", "!321", "abc", "xyz", "@abc", "!abc", "@xyz", "!xyz", "$123", "$321"]

payloads = special_payloads + characters + numbers

word_comb_limit = 2

yes_key = "Y"
no_key = "N"

def print_break():
    print("\n---------------------------------------\n")

def boolean_check(prompt):
    boolean_input = input(prompt + " [Y/N] ")
    if(boolean_input.upper() != yes_key and boolean_input.upper() != no_key):
        print_break()
        print("Invalid input. The input must either be a Y for Yes and N for No.")
        boolean_check(prompt)
    if(boolean_input.upper() == "Y"):
        return True
    else:
        return False