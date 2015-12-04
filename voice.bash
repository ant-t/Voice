#!/bin/bash

cd ~/Desktop
xsel > text.txt
espeak -p 0 -s 450 -f text.txt -w text.wav
sox text.wav text2.wav speed 1.1111
mv text2.wav text.wav
mocp -cap text.wav

