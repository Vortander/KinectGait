# -*- coding: utf-8 -*-
import itertools
import sys

args = len(sys.argv)

if args == 1:
	print "*********************************************************************************************************"
	print "Join all attributes                    "
	print "Usage: join_attributes [path/file_name_1] [path/file_name_2] "
	print " "
	print "*********************************************************************************************************"

else:

	file1 = sys.argv[1]
	file2 = sys.argv[2]

	f1 = open(file1, 'r')
	f2 = open(file2, 'r')

	fw = open('all_attributes.csv', 'w')

	f1_lines = f1.readlines()
	f2_lines = f2.readlines()

	if len(f1_lines) == len(f2_lines):
		print "running...", "\n"

		counter = 0
		for f1_line, f2_line in itertools.izip(f1_lines, f2_lines):
			f1_line = f1_line.replace('\n', '')
			f2_line = f2_line.replace('\n', '')

			f1_list = f1_line.split(',')
			f2_list = f2_line.split(',')

			f1_list.pop(0)
			f1_list.pop(len(f1_list)-1)
			name = f2_list.pop(0)
			#genero = f2_list.pop(len(f2_list) - 1)

			if counter > 0:
				values_f1 = str([float(n) for n in f1_list])
				values_f2 = str([float(n) for n in f2_list])
				values_f1 = values_f1.replace('[', '')
				values_f1 = values_f1.replace(']', '')
				values_f2 = values_f2.replace('[', '')
				values_f2 = values_f2.replace(']', '')
				#fw.write(name + ',' + values_f1 + ',' + values_f2 + ',' + genero + '\n')
				fw.write(name + ',' + values_f1 + ',' + values_f2 + '\n')
			else:
				f1_list = str(f1_list)
				f2_list = str(f2_list)

				f1_list = f1_list.replace('[', '')
				f1_list = f1_list.replace(']', '')
				f2_list = f2_list.replace('[', '')
				f2_list = f2_list.replace(']', '')
				f1_list = f1_list.replace('\'', '')
				f2_list = f2_list.replace('\'', '')

				#fw.write(name + ',' + f1_list + ',' + f2_list + ',' + genero + '\n')
				fw.write(name + ',' + f1_list + ',' + f2_list + '\n')

			counter+=1

	else:
		print "Halting - Input files do not have same number of lines: read README.1ST", "\n"


	f1.close()
	f2.close()
	fw.close()
