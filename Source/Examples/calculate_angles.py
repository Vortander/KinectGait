# -*- coding: utf-8 -*-

import pickle, math
import numpy
import os
import sys
  
def euclidean_distance(p1, p2):
	return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1]) + (p1[2]-p2[2])*(p1[2]-p2[2]))
	
def calculate_angle(opposite, hypotenuse):
	return float(math.asin(opposite/ hypotenuse) * (180/math.pi))

def angle_inside(joint1, joint2, p3):
	if p3 == joint2:
		angle = 0.0
		return angle
	else:
		hypotenuse = euclidean_distance(joint1,joint2)
		opposite = euclidean_distance(joint2,p3)
		angle = calculate_angle(opposite,hypotenuse)
		return angle

# 


if(len(sys.argv) < 2):
	print("**********************************************************************************")
	print("* Uso: calculate_angles.py [dictionary_list_name]  								*")
	print("**********************************************************************************")
	sys.exit(0)



print("**********************************************************************************")
print("* Calculate angles                                   by Virginia O. Andersson     *")
print("**********************************************************************************")

splited = sys.argv[1].split("_")
angles_file = "angles_" + str(sys.argv[1]) + ".csv"

dictionary = {}

#angles
list_angles_hip_right = []
list_angles_hip_left = []
list_angles_knee_right = []
list_angles_knee_left = []
list_angles_ankle_right = []
list_angles_ankle_left = []
list_angles_hip_right_balanco = []
list_angles_hip_right_externo = []
list_angles_hip_left_balanco = []
list_angles_hip_left_externo = []
list_angles_ankle_right_opening = []
list_angles_ankle_left_opening = []
list_angles_neck = []

#angles_file = "angulos_weka_" + str(sys.argv[1]) + ".csv"
fw = open(angles_file, 'w')
list_name = str(sys.argv[1]) 
arqlst = open(list_name, 'r')

files = arqlst.readlines()

print files

for line in files:
	line = line.replace('\r','')
	line = line.replace('\n','')
	#line = "Dados/dictionarys/" + line
	try:
		fr = open(line, 'rb')
	except:
		continue
	dictionary = pickle.load(fr)
	file_name = line.split('_')
	individual = file_name[1]
	
	for key in dictionary.keys():
		print key
				
		#12 = hip_right, 14 = knee_right, p3 = (x from hip, y from knee, z from hip)
		joint1 = (float(dictionary[key][12][1]), float(dictionary[key][12][2]), float(dictionary[key][12][3]))
		joint2 = (float(dictionary[key][14][1]), float(dictionary[key][14][2]), float(dictionary[key][14][3]))
		p3 = (float(dictionary[key][12][1]), float(dictionary[key][14][2]), float(dictionary[key][12][3]))
		angle_hip_right = angle_inside(joint1, joint2, p3)
		
		#13 = hip_left, 15 = knee_left, p3 = (x from hip, y from knee, z from hip)
		joint1 = (float(dictionary[key][13][1]), float(dictionary[key][13][2]), float(dictionary[key][13][3]))
		joint2 = (float(dictionary[key][15][1]), float(dictionary[key][15][2]), float(dictionary[key][15][3]))
		p3 = (float(dictionary[key][13][1]), float(dictionary[key][15][2]), float(dictionary[key][13][3]))
		angle_hip_left = angle_inside(joint1, joint2, p3)
				
		#14 = knee_right, 16 = ankle_right, p3 = (x from knee, y from ankle, z from knee)
		joint1 = (float(dictionary[key][14][1]), float(dictionary[key][14][2]), float(dictionary[key][14][3]))
		joint2 = (float(dictionary[key][16][1]), float(dictionary[key][16][2]), float(dictionary[key][16][3]))
		p3 = (float(dictionary[key][14][1]), float(dictionary[key][16][2]), float(dictionary[key][14][3]))
		angle_knee_right = angle_inside(joint1, joint2, p3)
		
		#15 = knee_left, 17 = ankle_left, p3 = (x from knee, y from ankle, z from knee)
		joint1 = (float(dictionary[key][15][1]), float(dictionary[key][15][2]), float(dictionary[key][15][3]))
		joint2 = (float(dictionary[key][17][1]), float(dictionary[key][17][2]), float(dictionary[key][17][3]))
		p3 = (float(dictionary[key][15][1]), float(dictionary[key][17][2]), float(dictionary[key][15][3]))
		angle_knee_left = angle_inside(joint1, joint2, p3)
		
		#16 = ankle_right, 18 = foot_right, p3 = (x from ankle, y from foot_right, z from ankle)
		joint1 = (float(dictionary[key][16][1]), float(dictionary[key][16][2]), float(dictionary[key][16][3]))
		joint2 = (float(dictionary[key][18][1]), float(dictionary[key][18][2]), float(dictionary[key][18][3]))
		p3 = (float(dictionary[key][16][1]), float(dictionary[key][18][2]), float(dictionary[key][16][3]))
		angle_ankle_right = angle_inside(joint1, joint2, p3)
		
		#17 = ankle_left, 19 = foot_left, p3 = (x from ankle, y from foot_left, z from ankle)
		joint1 = (float(dictionary[key][17][1]), float(dictionary[key][17][2]), float(dictionary[key][17][3]))
		joint2 = (float(dictionary[key][19][1]), float(dictionary[key][19][2]), float(dictionary[key][19][3]))
		p3 = (float(dictionary[key][17][1]), float(dictionary[key][19][2]), float(dictionary[key][17][3]))
		angle_ankle_left = angle_inside(joint1, joint2, p3)
		
		#16 = ankle_right, 18 = foot_right, p3 = (x from ankle, y from foot_right, z from ankle)
		joint1 = (float(dictionary[key][16][1]), float(dictionary[key][16][2]), float(dictionary[key][16][3]))
		joint2 = (float(dictionary[key][18][1]), float(dictionary[key][18][2]), float(dictionary[key][18][3]))
		p3 = (float(dictionary[key][18][1]), float(dictionary[key][18][2]), float(dictionary[key][16][3]))
		angle_ankle_right_opening = angle_inside(joint1, joint2, p3)
		
		#17 = ankle_left, 19 = foot_left, p3 = (x from ankle, y from foot_left, z from ankle)
		joint1 = (float(dictionary[key][17][1]), float(dictionary[key][17][2]), float(dictionary[key][17][3]))
		joint2 = (float(dictionary[key][19][1]), float(dictionary[key][19][2]), float(dictionary[key][19][3]))
		p3 = (float(dictionary[key][19][1]), float(dictionary[key][19][2]), float(dictionary[key][17][3]))
		angle_ankle_left_opening = angle_inside(joint1, joint2, p3)		
		
		list_angles_hip_right.append(angle_hip_right)
		list_angles_hip_left.append(angle_hip_left)
		list_angles_knee_right.append(angle_knee_right)
		list_angles_knee_left.append(angle_knee_left)
		list_angles_ankle_right.append(angle_ankle_right)
		list_angles_ankle_left.append(angle_ankle_left)
		list_angles_ankle_right_opening.append(angle_ankle_right_opening)
		list_angles_ankle_left_opening.append(angle_ankle_left_opening)
         
	# end of frame reading
	
	fw.write(individual + "-Angles_hip_right-" + file_name[2])
	for item in list_angles_hip_right:
		fw.write(',' + str(item))
	fw.write('\n')
		
	fw.write(individual + "-Angles_hip_left-" + file_name[2])
	for item in list_angles_hip_left:
		fw.write(',' + str(item))
	fw.write('\n')
	
	fw.write(individual + "-Angles_knee_right-" + file_name[2])
	for item in list_angles_knee_right:
		fw.write(',' + str(item))
	fw.write('\n')
	
	fw.write(individual + "-Angles_knee_left-" + file_name[2])
	for item in list_angles_knee_left:
		fw.write(',' + str(item))		
	fw.write('\n')
	
	fw.write(individual + "-Angles_ankle_right-" + file_name[2])
	for item in list_angles_ankle_right:
		fw.write(',' + str(item))
	fw.write('\n')
	
	fw.write(individual + "-Angles_ankle_left-" + file_name[2])
	for item in list_angles_ankle_left:
		fw.write(',' + str(item))	
	fw.write('\n')

	fw.write(individual + "-Angles_ankle_right_opening-" + file_name[2])
	for item in list_angles_ankle_right_opening:
		fw.write(',' + str(item))
	fw.write('\n')
	
	fw.write(individual + "-Angles_ankle_left_opening-" + file_name[2])
	for item in list_angles_ankle_left_opening:
		fw.write(',' + str(item))	
	fw.write('\n')
	
	list_angles_hip_right = []
	list_angles_hip_left = []
	list_angles_knee_right = []
	list_angles_knee_left = []
	list_angles_ankle_right = []
	list_angles_ankle_left = []
	list_angles_ankle_right_opening = []
	list_angles_ankle_left_opening = []
	
	fr.close()

fw.close()
