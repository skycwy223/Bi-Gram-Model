#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import stdin, stdout

while True:
	#strip을 붙인이유는 readline하면 앤터까지 포함되서
	line = stdin.readline().strip()
	#print(line)
	if line=="":
		break
	words = line.split()

	for i in range(1, len(words)):
	#for word in words:
		stdout.write(words[i-1]+" "+words[i]+"\t1\n")	
	
