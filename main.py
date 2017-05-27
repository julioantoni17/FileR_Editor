#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from os.path import exists
import read as r
import create as cr
import delete as d
import copy as c
import write as w
import os

PROMPT = "> "

print "\n\n\t\t\tPYTHON FILE READING & EDITOR\n"
print "\n\t\t\t* Press ^C if you want to exit while running the programm!!!\n"

opt = raw_input("\t\t\tDo you want read, create, delete content, copy content to other file,\n\t\t\twrite in a file or exit? (R, C, D, CY, W, E) \n\t\t\t" + \
				PROMPT)

if opt == "R" or opt == "r":
	try:
		# CHANGE DIRECTORY
		print "\n\n* Files and directories of the current route: %r\n" % os.listdir(os.getcwd())
		chd = raw_input("\n\t\t\tDo you want to change directory? (y/n)" + PROMPT)
		if chd == "Y" or chd == "y":
			while True:
				dirc = raw_input("Enter directory " + PROMPT)
				while exists(dirc) == False:
					print "\n\t\t\tEntered directory does not exists!!!"
					dirc = raw_input("Enter directory " + PROMPT)
					if exists(dirc) == True:
						print "Working on directory %r" % os.getcwd()
						break
					else:
						continue
				os.chdir(dirc)
				break
		else:
			print "Working on directory %r" % os.getcwd()
		#################

		r.read(raw_input("\n--> Enter a file " + PROMPT))
	except KeyboardInterrupt:
		print "\n\t\t\tStopped by the user!"

elif opt == "C" or opt == "c":
	try:
		# CHANGE DIRECTORY
		print "\n\n* Files and directories of the current route: %r\n" % os.listdir(os.getcwd())
		chd = raw_input("\n\t\t\tDo you want to change directory? (y/n)" + PROMPT)
		if chd == "Y" or chd == "y":
			while True:
				dirc = raw_input("Enter directory " + PROMPT)
				while exists(dirc) == False:
					print "\n\t\t\tEntered directory does not exists!!!"
					dirc = raw_input("Enter directory " + PROMPT)
					if exists(dirc) == True:
						print "Working on directory %r" % os.getcwd()
						break
					else:
						continue
				os.chdir(dirc)
				break
		else:
			print "Working on directory %r" % os.getcwd()
		#################

		cr.create(raw_input("\n--> Enter a file name " + PROMPT))
	except KeyboardInterrupt:
		print "\n\t\t\tStopped by the user!"

elif opt == "D" or opt == "d":
	try:
		# CHANGE DIRECTORY
		print "\n\n* Files and directories of the current route: %r\n" % os.listdir(os.getcwd())
		chd = raw_input("\n\t\t\tDo you want to change directory? (y/n)" + PROMPT)
		if chd == "Y" or chd == "y":
			while True:
				dirc = raw_input("Enter directory " + PROMPT)
				while exists(dirc) == False:
					print "\n\t\t\tEntered directory does not exists!!!"
					dirc = raw_input("Enter directory " + PROMPT)
					if exists(dirc) == True:
						print "Working on directory %r" % os.getcwd()
						break
					else:
						continue
				os.chdir(dirc)
				break
		else:
			print "Working on directory %r" % os.getcwd()
		##################

		d.delete(raw_input("\n--> Enter a file " + PROMPT))
	except KeyboardInterrupt:
		print "\n\t\t\tStopped by the user!"

elif opt == "CY" or opt == "cy":
	try:
		# CHANGE DIRECTORY
		print "\n\n* Files and directories of the current route: %r\n" % os.listdir(os.getcwd())
		chd = raw_input("\n\t\t\tDo you want to change directory? (y/n)" + PROMPT)
		if chd == "Y" or chd == "y":
			while True:
				dirc = raw_input("Enter directory " + PROMPT)
				while exists(dirc) == False:
					print "\n\t\t\tEntered directory does not exists!!!"
					dirc = raw_input("Enter directory " + PROMPT)
					if exists(dirc) == True:
						print "Working on directory %r" % os.getcwd()
						break
					else:
						continue
				os.chdir(dirc)
				break
		else:
			print "Working on directory %r" % os.getcwd()
		##################

		c.copy(raw_input("\n--> Enter the file to be copied " + PROMPT), raw_input("\n--> Enter the other file " + PROMPT))
	except KeyboardInterrupt:
		print "\n\t\t\tStopped by the user!"

elif opt == "W" or opt == "w":
	try:
		# CHANGE DIRECTORY
		print "\n\n* Files and directories of the current route: %r\n" % os.listdir(os.getcwd())
		chd = raw_input("\n\t\t\tDo you want to change directory? (y/n)" + PROMPT)
		if chd == "Y" or chd == "y":
			while True:
				dirc = raw_input("Enter directory " + PROMPT)
				while exists(dirc) == False:
					print "\n\t\t\tEntered directory does not exists!!!"
					dirc = raw_input("Enter directory " + PROMPT)
					if exists(dirc) == True:
						print "Working on directory %r" % os.getcwd()
						break
					else:
						continue
				os.chdir(dirc)
				break
		else:
			print "Working on directory %r" % os.getcwd()
		##################

		w.write(raw_input("\n--> Enter a file " + PROMPT))
	except KeyboardInterrupt:
		print "\n\t\t\tStopped by the user!"
else:
	exit()
