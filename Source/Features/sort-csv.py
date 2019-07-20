# -*- coding: utf-8 -*-
import random
import sys

#*****************************************************
#Sort CSV
#Usage: sort-csv.py [path/file_name]
#*****************************************************

file_name = sys.argv[1]

fr1 = open(file_name, 'r')
examples = []
lines = fr1.readlines()
for example in lines:
	examples.append(example)
heading = examples[0]
del examples[0]
random.shuffle(examples)
examples.insert(0, heading)

fw1 = open(file_name + "sorted.csv", 'w')
for example in examples:
	fw1.write(example)

fr1.close()
fw1.close()


