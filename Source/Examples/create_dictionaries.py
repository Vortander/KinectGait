# -*- coding: utf-8 -*-

import os, sys
import pickle

print("*************************************************")
print("* Pre-processes and generate pickle dictionaries *")
print("*************************************************")

# files.list is a list with all files in all persons directories. Each dictionary is generated from one raw walk file sample e.g. 01.txt
# place files.list in same directory of create_dictionaries.py

if len(sys.argv) < 2:
	print("***************************************************")
	print("* Usage: create_dictionaries.py [files.list] *")
	print("****************************************************")
	print("\t ?_files.list file name needs to be provided ")
	exit(0)

files_list = sys.argv[1]

try:
	fls = open(files_list, 'r')
except:
	print files_list, " not found: the file has to be placed in same directory"
	exit(0)

try:
	os.mkdir("Dictionaries")
except:
	print "directory Dicitionaries already exists"
	exit(0)

files = fls.readlines()

for file in files:

	if os.name == 'posix':
		name = file.split('/')
		print name
	if os.name == 'nt':
		name = file.split('\\')
		print name

	file = file.replace('\n','')

	_list = []
	list_segments = []
	segments = {}

	dir_input = file
	file_name = name[len(name)-1]
	file_name = file_name.replace('.txt', '')
	file_name = file_name.replace('\n', '')

	fr = open(dir_input,'r')
	linhas = fr.readlines()

	for joints in linhas:
		if joints.strip():
			joints = joints.replace('\xc3\xa3','a')
			joints = joints.replace('\xc3\xa7', 'c')
			joints = joints.replace('\xc3\xa9', 'e')
			joints = joints.replace('\r', '')
			joints = joints.replace('\n','')
			joints = joints.replace(',','.')
			pontos = joints.split(';')
			if len(pontos) !=4 :
				break
			_list.append(pontos)

	cont = 1
	for tupla in _list:
		print(tupla)
		list_segments.append(tupla)
		if tupla[0] == "Foot-Left":
			segments[cont] = list_segments
			cont+=1
			list_segments = []
			continue

	fw = open("Dictionaries/dictionary_" + name[len(name)-2] + '_' + file_name + ".pkl", "wb")
	print name[len(name)-2] + '_' + file_name
	pickle.dump(segments, fw)

	fr.close()
	fw.close()

fls.close()

#Creates a list with dictionary files

print("****************************************************")
print("* Creating list of dicionaries in dicionaries.list *")
print("****************************************************")

file_name = "dictionaries.list"

fw = open(file_name, 'w')

path = "Dictionaries"

for root, dirs, files in os.walk(path):
	files.sort()
	for file in files:
		if not file_name in file:
			temp = os.path.join(root, file)
			fw.write(temp + '\n')
fw.close()
