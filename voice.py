#!/usr/bin/python

import os
import random
import string

def nameGen(s=32, c=string.ascii_uppercase):
	return ''.join(random.choice(c) for _ in range(s))

if __name__ == '__main__':
	os.system('cd')
	tempDir = '.' + nameGen() 
	os.system('mkdir ' + tempDir)
	os.chdir(tempDir)
	os.system('xsel > text.txt')
	os.system('espeak -p 0 -s 450 -f text.txt -w text.wav')
	os.system('sox text.wav text2.wav speed 1.2')
	os.system('mv text2.wav text.wav')
	os.system('mocp -cap text.wav')
	os.system('mocp')
	os.chdir('..')
	os.system('rm -rf ' + tempDir)

