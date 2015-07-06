#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import stdin, stdout
library = {}

	# stdin이 끝날때 까지
while True:
	# stdin 에서 단어/횟수가 담긴 문장을 받아서
	line = stdin.readline().strip()
	if line == "":
		break
	# 이를 단어와 횟수로 쪼갠다음
	word, cnt = line.split('\t')
	#word_cnt = line.split('\t')
	#word = word_cnt[0]
	#cnt = word_cnt[1]
	#print word, cnt
	# 각 단어별 횟수를 합산해서(library[단어] += 횟수)
	if word in library:
		library[word] += int(cnt) # 있을때
	else:
		library[word] = int(cnt) #없을때
                
# 합산된 단어와 횟수를 STDOUT으로 출력합시다.(for 원소 in 딕셔너리: 딕(원소))
for word in library:
    stdout.write(word + "\t" + str(library[word]) + "\n")


