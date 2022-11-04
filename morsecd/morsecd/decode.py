from morsecd import main

# TODO This code is broken! Can you find out what one replacement to make to this function below?
# Hint: think about commands for generator functions in Python

def myMorseDecoder(msg_str):
	""" function to decode the morse code into the original text characters"""

	if len(msg_str) == 0: #nothing to do!
		print("\tNothing to do...")
		exit(1)
	mesg_str = main.printWithColour(main.BICyan, "\n\tDecoding ... \n")
	print(mesg_str)

	msg_list = msg_str.split() # make a list from the string. seperate by spaces
	out_str = "" # build the text string on this
	for i in msg_list:
		for letter in main.morse_dict:
			if main.morse_dict[letter] == i: # is this a char of Morse code?
				tmp1_str = main.printWithColour(main.BIBlue, f"\t{main.morse_dict[letter]}")
				tmp2_str = main.printWithColour(main.BIRed, "--->")
				tmp3_str = main.printWithColour(main.BIGreen, f"{letter}")
				print(f"{tmp1_str} {tmp2_str} {tmp3_str}")
				out_str += letter
	return out_str
#end of myMorseDecoder()