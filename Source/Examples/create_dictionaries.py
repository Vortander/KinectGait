# -*- coding: utf-8 -*-

import os
import pickle

print("*************************************************")
print("* Pre-processes and generate pickle dictionaries *")
print("*************************************************")

# files.list is a list with all files in all persons directories. Each dictionary is generated from one raw walk file sample e.g. 01.txt
# place files.list in same directory of create_dictionaries.py

try:
	fls = open("files.list", 'r')
except:
	print "files.list not found: the file has to be placed in same directory"
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
	
	list = []
	list_segments = []
	segments = {}

	dir_input = file
	file_name = name[len(name)-1]
	file_name = file_name.replace('.txt', '')
	file_name = file_name.replace('\n', '')
	
	fr = open(dir_entrada,'r')
	linhas = fr.readlines()

	for joints in linhas:
		if joints.strip():
			joints = joints.replace('\xc3\xa3','a')
			joints = joints.replace('\xc3\xa7', 'c')
			joints = joints.replace('\xc3\xa9', 'e')
			joints = joints.replace('\n','')
			joints = joints.replace(',','.')
			pontos = joints.split(';')
			if len(pontos) !=4 :
				break
			list.append(pontos)

	cont = 1		
	for tupla in list:
		list_segments.append(tupla)
		if tupla[0] == "Foot-left":
			segments[cont] = list_segments
			cont+=1
			list_segments = []
			continue
	
	fw = open("Dicionaries/dicionary_" + name[len(name)-2] + '_' + file_name + ".pkl", "wb")
	print name[len(name)-2] + '_' + file_name
	pickle.dump(segments, fw)
				
	fr.close()
	fw.close()

fls.close()

#Creates a list with dictionary files

print("****************************************************")
print("* Creating list of dicionaries in dicionaries.list *")
print("****************************************************")

file_name = "dicionaries.list"

fw = open(file_name, 'w')

path = "Dicionaries"

for root, dirs, files in os.walk(path):
	files.sort()
	for file in files:
		if not file_name in file:
			temp = os.path.join(root, file)
			fw.write(temp + '\n')
fw.close()


