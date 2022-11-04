from morsecd import main

# TODO This code is broken! Can you find out what one replacement to make to this function below?
# Hint: think about commands for generator functions in Python

def myMorseEncoder(msg_str):
	""" function to create a generator to yield each letter in morse code"""

	if len(msg_str) == 0: #nothing to do!
		print("\tNothing to do...")
		exit(1)

#	print("\n\t Encoding ...\n")
	mesg_str = main.printWithColour(main.BICyan, "\n\tEncoding ... \n")
	print(mesg_str)

	out_str = ""
	for i in msg_str:
		try:
			tmp1_str = main.printWithColour(main.BIGreen, f"\t {i}")
			tmp2_str = main.printWithColour(main.BIRed, "->")
			tmp3_str = main.printWithColour(main.BIBlue, f"{main.morse_dict[i.upper()]}")
			print(f"{tmp1_str} {tmp2_str} {tmp3_str}")
			out_str = out_str + main.morse_dict[i.upper()] + " "
		except KeyError:
			print(f"\t [-] Skipping: {i}")
	return out_str
#end of myMorseEncoder()

