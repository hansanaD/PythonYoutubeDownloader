# Clear the previous output from the terminal.
import os 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')