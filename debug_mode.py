#!/usr/bin/python3

import os
import sys
import getopt
import shutil

def release_mode(file):

	comment_counter = 0

	with open(file, 'r+') as f:
		with open("copy" + file, 'w') as cpy:
			for line in f:
				if ('print' in line) and ('DEBUG' in line):
					newL = line.replace(line, "#" + line)
					cpy.write(newL)
					comment_counter += 1
				else:
					cpy.write(line)	

	shutil.copy("copy" + file, file)
	os.remove("copy" + file)

	print ("Sucessfully commented " + str(comment_counter) + " line(s) in " + file)
	return


def debug_mode(file):
	decomment_counter = 0

	with open(file, 'r+') as f:
		with open("copy" + file, 'w') as cpy:
			for line in f:
				if ('print' in line) and ('DEBUG' in line) and ('#' in line):
					newL = line.replace('#', '')
					decomment_counter += 1
					cpy.write(newL)
				else:
					cpy.write(line)	

	shutil.copy("copy" + file, file)
	os.remove("copy" + file)

	print ("Sucessfully decommented " + str(decomment_counter) + " line(s) in " + file)
	return

def usage():
	print("----- Auto-set DEBUG mode in scripts -----\n")
	print("Search for print instructions  using the 'DEBUG' string and comment or de-comment them")
	print("USAGE : ./debug_mode -m [MODE] [FILE(S)]")
	print("MODE = 'd' for DEBUG or 'r' for RELEASE")


def main():
	optlist, args = getopt.getopt(sys.argv[1:], 'm:')
	if (len(optlist) != 1):
		usage()
		exit(0)

	debug = False
		
	for o,a in optlist:
		if o == '-m':
			if a == 'd':
				debug = True
			elif a == 'r':
				debug == False
		else:
			assert False, "Unhandled option"

	files = args

	if debug:
		for file in files:
			debug_mode(file)
	else:
		for file in files:
			release_mode(file)



if __name__ == '__main__':
	main()