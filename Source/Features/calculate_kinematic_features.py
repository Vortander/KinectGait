# -*- coding: utf-8 -*-

import pickle, math
import numpy as np
import itertools
import sys

def peaks_and_valleys(a):
	original = a
	a = np.array(a,dtype=np.float)
	gradients=np.diff(a)

	print gradients

	maxima_num=0
	minima_num=0
	max_locations=[]
	min_locations=[]
	count=0
	for i in gradients[:-1]:
		count+=1

		if ((cmp(i,0)>0) & (cmp(gradients[count],0)<0) & (i != gradients[count])):
			if (len(min_locations) > 0):			
				#if (abs(original[count] - original[max_locations[-1]]) > 3):
				if (abs(original[count] - original[min_locations[-1]]) > 2):
					maxima_num+=1
					max_locations.append(count)
			elif (len(max_locations) == 0):			
				maxima_num+=1	
				max_locations.append(count)
				
		if ((cmp(i,0)<0) & (cmp(gradients[count],0)>0) & (i != gradients[count])):
			if (len(max_locations) > 0):			
				#if (abs(original[count] - original[min_locations[-1]]) > 1):
				if (abs(original[count] - original[max_locations[-1]]) > 2):
					minima_num+=1
					min_locations.append(count)
			elif (len(min_locations) == 0):
					minima_num+=1	
					min_locations.append(count)			
				

	turning_points = {'maxima_number':maxima_num,'minima_number':minima_num,'maxima_locations':max_locations,'minima_locations':min_locations}  
	# print ("peaks")
	# print turning_points['maxima_locations'], turning_points['maxima_number']
	# print ("valleys")
	# print turning_points['minima_locations'], turning_points['minima_number']
	# raw_input()
	return turning_points

	
#
# Separate high peaks from low peaks
def split_low_high(loc_peaks, loc_valleys, angles):
	values_peaks_valleys = {'peaks_low':[], 'peaks_high':[], 'valleys_low':[], 'valleys_high':[]}
	
	last_peak = -1
	last_valley = -1
	type_previous_peak = 'baixo'
	type_previous_valley = 'baixo'
						
	for p in loc_peaks:
		if(angles[p] < last_peak):
			values_peaks_valleys['peaks_low'].append(angles[p])
			type_previous_peak = 'baixo'
		elif(angles[p] > last_peak):
			values_peaks_valleys['peaks_high'].append(angles[p])
			type_previous_peak = 'alto'
		elif(angles[p] == last_peak):
			if(type_previous_peak == 'baixo'):
				values_peaks_valleys['peaks_low'].append(angles[p])
			else:
				values_peaks_valleys['peaks_high'].append(angles[p])
		last_peak = angles[p]
		
	for p in loc_valleys:
		if(angles[p] < last_valley):
			values_peaks_valleys['valleys_low'].append(angles[p])
			type_previous_valley = 'baixo'
		elif(angles[p] > last_valley):
			values_peaks_valleys['valleys_high'].append(angles[p])
			type_previous_valley = 'alto'
		elif(angles[p] == last_valley):
			if(type_previous_valley == 'baixo'):
				values_peaks_valleys['valleys_low'].append(angles[p])
			else:
				values_peaks_valleys['valleys_high'].append(angles[p])
		last_valley = angles[p]

	return values_peaks_valleys	

####

if(len(sys.argv) < 2 and len(sys.argv) > 2):
	print("**********************************************************************************")
	print("* Usage: calculate_kinematic_features.py [angles_file]							 *")
	print("**********************************************************************************")

else:
	file_name = sys.argv[1]
	
	peaks_low = []
	peaks_high = []
	valleys_low = []
	valleys_high = []
	current_individual = ""
	current_walk = ""
	#parts = file_name.split('_')
	#fr = open(file_name, 'r');
	#print parts[2], file_name
	#fr = open("K:\\Mestrado\\Projeto\\angles\\angles"+str(parts[2])+"\\"+file_name, 'r')
	fr = open(file_name, 'r')
	#fw = open("atributtes_angles_" + parts[2] + "_" + parts[3], 'w');
	fw = open("atributtes_angles_" + file_name, 'w');
	fw.write("individual,sd_peaks_low_hip_right,average_peaks_low_hip_right,sd_peaks_high_hip_right,average_peaks_high_hip_right,sd_peaks_low_hip_left,average_peaks_low_hip_left,sd_peaks_high_hip_left,average_peaks_high_hip_left,"+
			  "sd_peaks_low_knee_right,average_peaks_low_knee_right,sd_peaks_high_knee_right,average_peaks_high_knee_right,sd_peaks_low_knee_left,average_peaks_low_knee_left,sd_peaks_high_knee_left,average_peaks_high_knee_left,"+
			  "sd_peaks_low_ankle_right,average_peaks_low_ankle_right,sd_peaks_high_ankle_right,average_peaks_high_ankle_right,sd_peaks_low_ankle_left,average_peaks_low_ankle_left,sd_peaks_high_ankle_left,average_peaks_high_ankle_left,"+
			  "sd_valleys_low_hip_right,average_valleys_low_hip_right,sd_valleys_high_hip_right,average_valleys_high_hip_right,sd_valleys_low_hip_left,average_valleys_low_hip_left,sd_valleys_high_hip_left,average_valleys_high_hip_left,"+
			  "sd_valleys_low_knee_right,average_valleys_low_knee_right,sd_valleys_high_knee_right,average_valleys_high_knee_right,sd_valleys_low_knee_left,average_valleys_low_knee_left,sd_valleys_high_knee_left,average_valleys_high_knee_left,"+
			  "sd_valleys_low_ankle_right,average_valleys_low_ankle_right,sd_valleys_high_ankle_right,average_valleys_high_ankle_right,sd_valleys_low_ankle_left,average_valleys_low_ankle_left,sd_valleys_high_ankle_left,average_valleys_high_ankle_left,"+
			  "sd_valleys_low_ankle_right_opening,average_valleys_low_ankle_right_opening,sd_valleys_high_ankle_right_opening,average_valleys_high_ankle_right_opening,sd_valleys_low_ankle_left_opening,average_valleys_low_ankle_left_opening,sd_valleys_high_ankle_left_opening,average_valleys_high_ankle_left_opening"+
			  "\n")	
	while True:
		l = fr.readline()
		l = l.replace('\n', '')
		if len(l) == 0:
			if(current_individual != "" or current_walk != ""):
				fw.write(current_individual + ',' + str(sd_peaks_low_hip_right)+ ',' + str(average_peaks_low_hip_right)+ ',' +str(sd_peaks_high_hip_right)+ ',' +str(average_peaks_high_hip_right)+ ',' +str(sd_peaks_low_hip_left)+ ',' +str(average_peaks_low_hip_left)+ ',' +str(sd_peaks_high_hip_left)+ ',' +str(average_peaks_high_hip_left)+ ',' +
						 str(sd_peaks_low_knee_right)+ ',' +str(average_peaks_low_knee_right)+ ',' +str(sd_peaks_high_knee_right)+ ',' +str(average_peaks_high_knee_right)+ ',' +str(sd_peaks_low_knee_left)+ ',' +str(average_peaks_low_knee_left)+ ',' +str(sd_peaks_high_knee_left)+ ',' +str(average_peaks_high_knee_left)+ ',' +
						 str(sd_peaks_low_ankle_right)+ ',' +str(average_peaks_low_ankle_right)+ ',' +str(sd_peaks_high_ankle_right)+ ',' +str(average_peaks_high_ankle_right)+ ',' +str(sd_peaks_low_ankle_left)+ ',' +str(average_peaks_low_ankle_left)+ ',' +str(sd_peaks_high_ankle_left)+ ',' +str(average_peaks_high_ankle_left) + ',' +
 						 str(sd_valleys_low_hip_right)+ ',' +str(average_valleys_low_hip_right)+ ',' +str(sd_valleys_high_hip_right)+ ',' +str(average_valleys_high_hip_right)+ ',' +str(sd_valleys_low_hip_left)+ ',' +str(average_valleys_low_hip_left)+ ',' +str(sd_valleys_high_hip_left)+ ',' +str(average_valleys_high_hip_left)+ ',' +
						 str(sd_valleys_low_knee_right)+ ',' +str(average_valleys_low_knee_right)+ ',' +str(sd_valleys_high_knee_right)+ ',' +str(average_valleys_high_knee_right)+ ',' +str(sd_valleys_low_knee_left)+ ',' +str(average_valleys_low_knee_left)+ ',' +str(sd_valleys_high_knee_left)+ ',' +str(average_valleys_high_knee_left)+ ',' +
						 str(sd_valleys_low_ankle_right)+ ',' +str(average_valleys_low_ankle_right)+ ',' +str(sd_valleys_high_ankle_right)+ ',' +str(average_valleys_high_ankle_right)+ ',' +str(sd_valleys_low_ankle_left)+ ',' +str(average_valleys_low_ankle_left)+ ',' +str(sd_valleys_high_ankle_left)+ ',' +str(average_valleys_high_ankle_left)+ ',' + 
						 str(sd_valleys_low_ankle_right_opening)+ ',' +str(average_valleys_low_ankle_right_opening)+ ',' +str(sd_valleys_high_ankle_right_opening)+ ',' +str(average_valleys_high_ankle_right_opening)+ ',' +str(sd_valleys_low_ankle_left_opening)+ ',' +str(average_valleys_low_ankle_left_opening)+ ',' +str(sd_valleys_high_ankle_left_opening)+ ',' +str(average_valleys_high_ankle_left_opening)+ ',' + genero[current_individual] + '\n')
			break
		else:
			linha = l.split(',')
			file_name = linha[0]
			
			title = file_name.split('-')
			next_walk = title[2]
			next_individual = title[0]
			if(next_individual != current_individual or next_walk != current_walk):
				if(current_individual != "" or current_walk != ""):
					fw.write(current_individual + ',' + str(sd_peaks_low_hip_right)+ ',' + str(average_peaks_low_hip_right)+ ',' +str(sd_peaks_high_hip_right)+ ',' +str(average_peaks_high_hip_right)+ ',' +str(sd_peaks_low_hip_left)+ ',' +str(average_peaks_low_hip_left)+ ',' +str(sd_peaks_high_hip_left)+ ',' +str(average_peaks_high_hip_left)+ ',' +
						 str(sd_peaks_low_knee_right)+ ',' +str(average_peaks_low_knee_right)+ ',' +str(sd_peaks_high_knee_right)+ ',' +str(average_peaks_high_knee_right)+ ',' +str(sd_peaks_low_knee_left)+ ',' +str(average_peaks_low_knee_left)+ ',' +str(sd_peaks_high_knee_left)+ ',' +str(average_peaks_high_knee_left)+ ',' +
						 str(sd_peaks_low_ankle_right)+ ',' +str(average_peaks_low_ankle_right)+ ',' +str(sd_peaks_high_ankle_right)+ ',' +str(average_peaks_high_ankle_right)+ ',' +str(sd_peaks_low_ankle_left)+ ',' +str(average_peaks_low_ankle_left)+ ',' +str(sd_peaks_high_ankle_left)+ ',' +str(average_peaks_high_ankle_left) + ',' +
 						 str(sd_valleys_low_hip_right)+ ',' +str(average_valleys_low_hip_right)+ ',' +str(sd_valleys_high_hip_right)+ ',' +str(average_valleys_high_hip_right)+ ',' +str(sd_valleys_low_hip_left)+ ',' +str(average_valleys_low_hip_left)+ ',' +str(sd_valleys_high_hip_left)+ ',' +str(average_valleys_high_hip_left)+ ',' +
						 str(sd_valleys_low_knee_right)+ ',' +str(average_valleys_low_knee_right)+ ',' +str(sd_valleys_high_knee_right)+ ',' +str(average_valleys_high_knee_right)+ ',' +str(sd_valleys_low_knee_left)+ ',' +str(average_valleys_low_knee_left)+ ',' +str(sd_valleys_high_knee_left)+ ',' +str(average_valleys_high_knee_left)+ ',' +
						 str(sd_valleys_low_ankle_right)+ ',' +str(average_valleys_low_ankle_right)+ ',' +str(sd_valleys_high_ankle_right)+ ',' +str(average_valleys_high_ankle_right)+ ',' +str(sd_valleys_low_ankle_left)+ ',' +str(average_valleys_low_ankle_left)+ ',' +str(sd_valleys_high_ankle_left)+ ',' +str(average_valleys_high_ankle_left)+ ',' + 
						 str(sd_valleys_low_ankle_right_opening)+ ',' +str(average_valleys_low_ankle_right_opening)+ ',' +str(sd_valleys_high_ankle_right_opening)+ ',' +str(average_valleys_high_ankle_right_opening)+ ',' +str(sd_valleys_low_ankle_left_opening)+ ',' +str(average_valleys_low_ankle_left_opening)+ ',' +str(sd_valleys_high_ankle_left_opening)+ ',' +str(average_valleys_high_ankle_left_opening)+ ',' + genero[current_individual] + '\n')

			current_individual = next_individual
			current_walk = next_walk
			angles = [float(i) for i in linha[1:len(linha)]]
			tp = peaks_and_valleys(angles)
			loc_peaks = tp['maxima_locations']
			loc_valleys = tp['minima_locations']
			
			dtemp = split_low_high(loc_peaks, loc_valleys, angles)

			#neck, balance and external not included
			if(file_name.find('neck') == -1 or file_name.find('balance') == -1 or file_name.find('external') == -1 or file_name.find('opening') == -1):
			# TODO: Parei aqui!
				if(file_name.find('knee_right') != -1):
					sd_peaks_low_knee_right = np.std(dtemp['peaks_low'])
					average_peaks_low_knee_right = np.mean(dtemp['peaks_low'])
					sd_peaks_high_knee_right = np.std(dtemp['peaks_high'])
					average_peaks_high_knee_right = np.mean(dtemp['peaks_high'])
					
					sd_valleys_low_knee_right = np.std(dtemp['valleys_low'])
					average_valleys_low_knee_right = np.mean(dtemp['valleys_low'])
					sd_valleys_high_knee_right = np.std(dtemp['valleys_high'])
					average_valleys_high_knee_right = np.mean(dtemp['valleys_high'])

				if(file_name.find('knee_left') != -1):
					sd_peaks_low_knee_left = np.std(dtemp['peaks_low'])
					average_peaks_low_knee_left = np.mean(dtemp['peaks_low'])
					sd_peaks_high_knee_left = np.std(dtemp['peaks_high'])
					average_peaks_high_knee_left = np.mean(dtemp['peaks_high'])
					
					sd_valleys_low_knee_left = np.std(dtemp['valleys_low'])
					average_valleys_low_knee_left = np.mean(dtemp['valleys_low'])
					sd_valleys_high_knee_left = np.std(dtemp['valleys_high'])
					average_valleys_high_knee_left = np.mean(dtemp['valleys_high'])

				if(file_name.find('hip_right') != -1):
					sd_peaks_low_hip_right = np.std(dtemp['peaks_low'])
					average_peaks_low_hip_right = np.mean(dtemp['peaks_low'])
					sd_peaks_high_hip_right = np.std(dtemp['peaks_high'])
					average_peaks_high_hip_right = np.mean(dtemp['peaks_high'])
					
					sd_valleys_low_hip_right = np.std(dtemp['valleys_low'])
					average_valleys_low_hip_right = np.mean(dtemp['valleys_low'])
					sd_valleys_high_hip_right = np.std(dtemp['valleys_high'])
					average_valleys_high_hip_right = np.mean(dtemp['valleys_high'])

				if(file_name.find('hip_left') != -1):
					sd_peaks_low_hip_left = np.std(dtemp['peaks_low'])
					average_peaks_low_hip_left = np.mean(dtemp['peaks_low'])
					sd_peaks_high_hip_left = np.std(dtemp['peaks_high'])
					average_peaks_high_hip_left = np.mean(dtemp['peaks_high'])
					
					sd_valleys_low_hip_left = np.std(dtemp['valleys_low'])
					average_valleys_low_hip_left = np.mean(dtemp['valleys_low'])
					sd_valleys_high_hip_left = np.std(dtemp['valleys_high'])
					average_valleys_high_hip_left = np.mean(dtemp['valleys_high'])
					
				if(file_name.find('ankle_right') != -1 and file_name.find('opening') == -1):
					sd_peaks_low_ankle_right = np.std(dtemp['peaks_low'])
					average_peaks_low_ankle_right = np.mean(dtemp['peaks_low'])
					sd_peaks_high_ankle_right = np.std(dtemp['peaks_high'])
					average_peaks_high_ankle_right = np.mean(dtemp['peaks_high'])
					
					sd_valleys_low_ankle_right = np.std(dtemp['valleys_low'])
					average_valleys_low_ankle_right = np.mean(dtemp['valleys_low'])
					sd_valleys_high_ankle_right = np.std(dtemp['valleys_high'])
					average_valleys_high_ankle_right = np.mean(dtemp['valleys_high'])
					
				if(file_name.find('ankle_left') != -1 and file_name.find('opening') == -1):
					sd_peaks_low_ankle_left = np.std(dtemp['peaks_low'])
					average_peaks_low_ankle_left = np.mean(dtemp['peaks_low'])
					sd_peaks_high_ankle_left = np.std(dtemp['peaks_high'])
					average_peaks_high_ankle_left = np.mean(dtemp['peaks_high'])
					
					sd_valleys_low_ankle_left = np.std(dtemp['valleys_low'])
					average_valleys_low_ankle_left = np.mean(dtemp['valleys_low'])
					sd_valleys_high_ankle_left = np.std(dtemp['valleys_high'])
					average_valleys_high_ankle_left = np.mean(dtemp['valleys_high'])
					
				if(file_name.find('ankle_right_opening') != -1):
					sd_peaks_low_ankle_right_opening = np.std(dtemp['peaks_low'])
					average_peaks_low_ankle_right_opening = np.mean(dtemp['peaks_low'])
					sd_peaks_high_ankle_right_opening = np.std(dtemp['peaks_high'])
					average_peaks_high_ankle_right_opening = np.mean(dtemp['peaks_high'])
					
					sd_valleys_low_ankle_right_opening = np.std(dtemp['valleys_low'])
					average_valleys_low_ankle_right_opening = np.mean(dtemp['valleys_low'])
					sd_valleys_high_ankle_right_opening = np.std(dtemp['valleys_high'])
					average_valleys_high_ankle_right_opening = np.mean(dtemp['valleys_high'])
							
			
				if(file_name.find('ankle_left_opening')!=-1):
					sd_peaks_low_ankle_left_opening = np.std(dtemp['peaks_low'])
					average_peaks_low_ankle_left_opening = np.mean(dtemp['peaks_low'])
					sd_peaks_high_ankle_left_opening = np.std(dtemp['peaks_high'])
					average_peaks_high_ankle_left_opening = np.mean(dtemp['peaks_high'])
					
					sd_valleys_low_ankle_left_opening = np.std(dtemp['valleys_low'])
					average_valleys_low_ankle_left_opening = np.mean(dtemp['valleys_low'])
					sd_valleys_high_ankle_left_opening = np.std(dtemp['valleys_high'])
					average_valleys_high_ankle_left_opening = np.mean(dtemp['valleys_high'])
				
				dtemp.clear()
					
	fr.close()
	fw.close()
			
			

			
