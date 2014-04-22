#!/usr/local/bin/env python

import sys

FrameofChange = open('.temp.fnord.data/cutframe.txt').read().split(';\n')
SubsequentCuts = []
Previous = '1'
while len(FrameofChange) > 2:
	if int(sys.argv[1]) > int(FrameofChange[0]) - int(Previous):
		SubsequentCuts.append(Previous)
	Previous = FrameofChange.pop(0)
print SubsequentCuts
subliminals = open('.temp.fnord.data/subliminals.txt','w')
for FrameNumber in SubsequentCuts:
	subliminals.write(FrameNumber + ";\n")
subliminals.close()
