#!/usr/bin/python

import sys

def main():

	# if the number of arguments is not what is expected, exit
	numArgs = 3
	if len(sys.argv) != numArgs:
		print "Expected", numArgs, "Arguments"
		sys.exit()

	print 'Argument List:', str(sys.argv)


if __name__ == "__main__": 
	# executed when script is called directly
	main()
else: 
	# executed when imported
	pass
