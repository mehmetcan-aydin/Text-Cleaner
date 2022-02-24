#!/usr/bin/env python

import sys
import os

unwanted_list = "ROOT BRANCH ENDROOT ENDBRANCH".split()  #list of elements to be cleaned

try:
	input_file = sys.argv[1]                              #this colon checks eligibility of
	if input_file in os.listdir():                        #parameter as it is a text file
		tmp = input_file.index(".")                       #and opens output file
		output_file = open(input_file[:tmp] + "_c" + input_file[tmp:], "w")

	with open(sys.argv[1], "r") as file_data:              
		lines = file_data.read().splitlines()             #this colon reads input file
		for i in lines:                                   #line by line and eliminates
			if i.split()[0] in unwanted_list:             #unwanted elements while it
				continue                                  #writes other lines into output
			else:
				output_file.write(i + "\n")
	print("Process done.")

except (FileNotFoundError, IndexError):
	print("Please specify a proper file.")