morse_code = {
    "A" : ".-","B" : "-...","C" : "-.-.","D" : "-..",
    "E" : ".","F" : "..-.","G" : "--.","H" : "....",
    "I" : "..","J" : ".---","K" : "-.-","L" : ".-..",
    "M" : "--","N" : "-.","O" : "---","P" : ".--.",
    "Q" : "--.-","R" : ".-.","S" : "...","T" : "-",
    "U" : "..-","V" : "...-","W" : ".--","X" : "-..-",
    "Y" : "-.--","Z" : "--..","1" : ".----","2" : "..---",
    "3" : "...--","4" : "....-","5" : ".....","6" : "-....",
    "7" : "--...","8" : "---..","9" : "----.","0" : "-----",
    "?" : "..--..","!" : "-.-.--","." : ".-.-.-","," : "--..--",
    ";" : "-.-.-.",":" : "---...","+" : ".-.-.","-" : "-....-",
    "/" : "-..-.","=" : "-...-","_": "..--.-",'"': ".-..-.",
    "$": "...-..-","@": ".--.-.","(": "-.--.",")": "-.--.-",
    "&": ".-..."}

import pyfiglet
import os
import sys
from termcolor import colored

# Colours

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[96m'

# Banner
banner = pyfiglet.figlet_format("Morse Link")
text = colored(banner, "blue")
print(text)
print("")

# warning
print(bcolors.YELLOW + "[-]Warning: Don't use spaces when typing the text")
print("")




def encrypt(message):
    cipher = ""
    for letter in message:
        if letter != " ":
            cipher += morse_code[letter] + " "
        else:
            cipher += " "
    return cipher


def decrypt(message):

    message += ""
    decipher = ""
    citext = ""
    for letter in message:
        if(letter != " "):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += " "
            else:
                decipher += list(morse_code.keys())[list(morse_code.values()).index(citext)]
                citext = ""
    return decipher

def main():
        
    # Functions
    print(bcolors.BLUE + "[Functions]")
    print(bcolors.GREEN + """Select a option

    1) Want To Translate Normal text Into Morse Code
    2) Want To Translate Morse Code Into Normal Text
    00) Exit The Program""")

    print("")
    user = int(input("Morse Link> "))
    text = input("Enter Text: ")
    if user == 1:
        print("")
        #message1 = input("Enter the Text you want to Translate into Morse code: ")
        result = encrypt(text.upper())
        print("")
        print(result)
        print("")

    elif user == 2:
        print("")
        #message2 = input("Enter the Morse code you want to Translate into Text: ")
        result = decrypt(text)
        print("")
        print(result)
        print("")

    elif user == 0 or user == 00:
        sys.exit()

    else:
        print("")
        print("Unidentified Option")
        print("")

if __name__ == "__main__":
    main()