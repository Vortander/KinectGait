# -*- coding: utf-8 -*-

import pickle
import sys
import os
import numpy as np


def arma(past_values, future_values, ai):
	values= []
	for v in future_values:
		values.append(v)

	for v in past_values:
		values.append(v)

	avgmean = 0

	for v in values:
		avgmean = float(ai * v) + avgmean

	return avgmean
#

def arma3D(past_values, future_values, ai):
	values= []

	for v in future_values:
		values.append(v)

	for v in past_values:
		values.append(v)

	avgmeanX = 0
	avgmeanY = 0
	avgmeanZ = 0

	for x,y,z in values:
		avgmeanX = float(ai * x) + avgmeanX
		avgmeanY = float(ai * y) + avgmeanY
		avgmeanZ = float(ai * z) + avgmeanZ

	return [avgmeanX, avgmeanY, avgmeanZ]

#

if(len(sys.argv) < 3):
	print("*******************************************************************************************************")
	print("* Usage: apply_arma_filter.py [dictionaries_files_list_file] [number_of_frames(1 N value both for past and future)]*")
	print("*******************************************************************************************************")
	sys.exit(0)


print("**********************************************************************************")
print("* ARMA FILTER                                        by Virginia O. Andersson    *")
print("**********************************************************************************")

#nome_arquivo = sys.argv[1]

#dictionaries list name example: dictionaries_Nvalue_group1.list
#dictionaries_10_grupo0.list
try:
	group_files =  sys.argv[1].split("_")
	group_files[2] = group_files[2].replace(".list",'')
	use_groups = True
except:
	print(group_files)
	group_file = group_files[0].replace(".list", '')
	use_groups = False

past_values = []
future_values = []
frame = []
p = []

descriptors = ['Head', 'Shoulder-center', 'Shoulder-right', 'Shoulder-left', 'Elbow-right', 'Elbow-left', 'Wrist-right', 'Wrist-left',
			   'Hand-right', 'Hand-left', 'Spine', 'Hip-center', 'Hip-right', 'Hip-left', 'Knee-right', 'Knee-left',
			   'Ankle-righ', 'Ankle-left', 'Foot-right', 'Foot-left']


filtered = {}

#N value = past and future number of frames to look backwards and aftwards
value = int(sys.argv[2])
ai = 1/float(2*value)

#Open file with dictionary list
#Create a dictionaries' files list

print "Reading 3D points dictionaries:"
#if os.name == 'posix':
#	filelst = open("Data/dictionaries.list", 'r')
#if os.name == 'nt':

filelst = open(sys.argv[1], 'r')
dict_files = filelst.readlines()

for lines in dict_files:
	lines = lines.replace('\n','')

	fr = open(lines, 'rb')
	dictionary = pickle.load(fr)
	name_of_file = lines.split('_')
	individual = name_of_file[1]

	print name_of_file, individual

	for key in sorted(range(value+1, len(dictionary.keys()) + 1)):
		print(key, len(dictionary.keys()))
		for segment in range(0,20):
			for i in range(value,0,-1):
				past_values.append([float(dictionary[key-i][segment][1]), float(dictionary[key-i][segment][2]), float(dictionary[key-i][segment][3])])
			for i in range(1,value+1,1):
				print( key, key + i )
				if key + i <= len(dictionary.keys()):
					future_values.append([float(dictionary[key+i][segment][1]), float(dictionary[key+i][segment][2]), float(dictionary[key+i][segment][3])])

			c = arma3D(past_values, future_values, ai)

			past_values =[]
			future_values =[]

			p.append(descriptors[segment])
			[p.append(str(i)) for i in c]

			frame.append(p)
			filtered[key] = frame

			p = []
		frame = []

	#Original
	#Change file path to save arma filtered files, as needed

	if use_groups == True:
		fw = open( group_files[1] + "\\ARMA" + group_files[2] + "\\dictionary_" + individual + '_' + name_of_file[2], "wb")

	elif use_groups == False:
		try:
			os.mkdir("ARMADicts")
		except:
			pass

		fw = open( os.path.join( "ARMADicts",  group_file + "-ARMAdictionary_" + individual + '_' + name_of_file[2]) , "wb" )

	pickle.dump(filtered, fw)

	filtered.clear()

	fw.close()

fr.close()
