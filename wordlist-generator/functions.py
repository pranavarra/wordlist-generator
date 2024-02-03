import userdata
import json
import tkinter.filedialog
import datetime

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