#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Designed to work in Poetry: A Program to using generator functions for encoding / decoding text into / from morse code."""

from collections import Counter
import sys, random
from morsecd import decode
from morsecd import encode

DATE = "3 Nov 2022"
VERSION = "0.3.0"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"
THISPROG = sys.argv[0].replace("./","")
WHATISTHIS_p1 = "\n\tA Morse encoder and decoder program."
WHATISTHIS_p2 = "\tUse option '-h' for more glorification about this amazing project!\n"


# Bold colour list
colour_list =['\033[1;30m',
'\033[1;31m',
'\033[1;32m',
'\033[1;33m',
'\033[1;34m',
'\033[1;35m',
'\033[1;36m',
'\033[1;37m',
'\033[1;90m',
'\033[1;91m',
'\033[1;92m',
'\033[1;93m',
'\033[1;94m',
'\033[1;95m',
'\033[1;96m']

BIYellow = '\033[1;93m'     # Yellow
BIGreen='\033[1;92m'      # Green
BIBlue='\033[1;94m'       # Blue
BICyan='\033[1;96m'       # Cyan
BIRed='\033[1;91m'        # Red
BIWhite='\033[1;97m'      # White
White='\033[0;37m'        # White


banner1_str = """
\t ███╗   ███╗ ██████╗ ██████╗ ███████╗███████╗ ██████╗██████╗ 
\t ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗
\t ██╔████╔██║██║   ██║██████╔╝███████╗█████╗  ██║     ██║  ██║
\t ██║╚██╔╝██║██║   ██║██╔══██╗╚════██║██╔══╝  ██║     ██║  ██║
\t ██║ ╚═╝ ██║╚██████╔╝██║  ██║███████║███████╗╚██████╗██████╔╝
\t ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚═════╝ 
"""                                                            

# banner ref: https://manytools.org/hacker-tools/ascii-banner/


# The dictionary of Morse code. keys = alphabet chars, values = code.
morse_dict = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	      'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',
              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',  ' ':'/'     ,  '.':'.-.-.-',
              ',':'--..--',  ':':'---...',  '?':'..--..',
              "'":'.----.',  '-':'-....-',  '/':'-..-.',
              '@': '.--.-.', '=':'-...-',   '(':'-.--.',
              ')':'-.--.-',  '+':'.-.-.',   '!':'-.-.--',
              ';':'-.-.-'
        }

def get_platformType():
	"""Function to dermine the OS type."""
	platforms = {
	'darwin' : 'OSX',
	'win32'  : 'Windows',
	'linux1' : 'Linux',
	'linux2' : 'Linux'}
	if sys.platform not in platforms:
		return sys.platform
	return platforms[sys.platform]
#end of get_platformType()

def printWithColour(colCode_str, myMessage_str):
	"""A function to print with colour for Unix and MacOS."""
	platform_str = get_platformType()
	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		myMessage_str = colCode_str + myMessage_str + BIWhite
		# print(colCode_str + myMessage_str + BIWhite)
	else: # Windows does not seem to like these colourcodes
		# print(myMessage_str)
		pass
	return myMessage_str
# end of printWithColour()


def bannerScreen(myCount_int):
	"""prints a charming and colourful little message for the user"""
	# report the perceived OS type
	platform_str = get_platformType()

	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		for i in range(myCount_int):
			randomColour_str = random.choice(colour_list) # choose a random colour to display the title screen.
			print(randomColour_str + banner1_str + BIWhite)
	else:
		print(banner1_str)
#end of bannerScreen()

def helper():
	""" Online help; how to use the program"""
	bannerScreen(1) # print up one banner screen
	print(WHATISTHIS_p1)
	h_str1 = "\t"+DATE+" | version: "+VERSION
	h_str2 = "\t"+AUTHOR +"\n\tmail: "+AUTHORMAIL
	print("\t"+len(h_str2) * "-")
	print(h_str1)
	print("\t"+len(h_str2) * "-")
	print(h_str2)
	print("\t"+len(h_str2) * "-")
	print(f"\t [+] \U0001f600  USAGE: poetry run  {THISPROG} --message")
	print("\n\t [+] You will then be asked to enter your message to convert to Morse code")
	print("\t     or you can enter your encoded message to convert back into text.\n\t     Wonderful, right!?")
#end of helper()


def isMorseCode(in_str):
	""" TODO: What does this function do?!"""
	# Are the only chars in text from Morse code?
	if len(Counter(in_str)) <= 4 and "-" in in_str and "." in in_str or "/" in in_str:
		return True
	else:
		return False
#end of isMorseCode()


def begin():
	"""Driver function"""
	msg_str = input('\tInput your message (either in text or in Morse code) : ')
	out_str = ""
	if isMorseCode(msg_str) != True:

		out_str = encode.myMorseEncoder(msg_str)

	else: # is morse code

		out_str = decode.myMorseDecoder(msg_str)
	mesg_str = printWithColour(BIYellow, "\n\tYour Message: ")
	print(mesg_str,next(out_str))
#end of begin()


from pathlib import Path
import typer
from rich.console import Console

cli = typer.Typer()
@cli.command()
def getArguments(
    bighelp: bool = False,
    # opt: str = "",
	message: bool = False
) -> None:
	"""New get arguments function"""
	if bighelp == True:  # print up some extra help about how to start a virtual env
		helper()
		exit()
	if message == True:
		begin()
# end of getArguments()


if __name__ == '__main__':
	getArguments(sys.argv[1:])
