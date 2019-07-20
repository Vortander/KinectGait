# -*- coding: utf-8 -*-

import pickle, math
import os
import sys
import numpy

#def peaks_and_valleys(a):
def peaks_and_valleys(a):
	
	a = numpy.array(a,dtype=numpy.float)
	gradients=numpy.diff(a)

	maxima_num=0
	minima_num=0
	max_locations=[]
	min_locations=[]
	count=0
	for i in gradients[:-1]:
		count+=1

		if ((cmp(i,0)>0) & (cmp(gradients[count],0)<0) & (i != gradients[count])):
			maxima_num+=1
			max_locations.append(count)     

		if ((cmp(i,0)<0) & (cmp(gradients[count],0)>0) & (i != gradients[count])):
			minima_num+=1
			min_locations.append(count)


	turning_points = {'maxima_number':maxima_num,'minima_number':minima_num,'maxima_locations':max_locations,'minima_locations':min_locations}  
	return turning_points
#	
	
#def euclidean_distance(p1, p2):
def euclidean_distance(p1, p2):
	return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1]) + (p1[2]-p2[2])*(p1[2]-p2[2]))

#def soma_segmentos(seg_1, seg_2, seg_3, seg_4, seg_5, seg_6):
def sum_segments(seg_1, seg_2, seg_3, seg_4, seg_5, seg_6):
	return seg_1 + seg_2 + seg_3 + seg_4 + seg_5 + seg_6

#def mediana(lista):
def median(list):
	k = len(list)
	list = sorted(list)
	if k%2 == 0:
		middle =  float((list[(k-1)/2] + list[(k+1)/2])/2)
	else:
		middle = list[k/2]
	return middle

#def maior(lista):
def major(list):
	return max(list)
	
#def menor(lista):
def minor(list):
	return min(list)

#def media_a(lista):
def average_a(list):
	sum = 0
	for item in list:
		sum+= float(item)
	return sum/len(list)
	
#def alcance(lista):
def reach(list):
	list = sorted(list)
	minor = list[0]
	major = list[len(list)-1]
	return major - minor
	
	
# Desvio Padrao
# Standard Deviation

# lista são as amostras
def media(lista):
	soma = 0
	n = len(lista)
	for item in lista:
		soma+=item
	return soma/n

def desvios(valor, m):
	desvio = valor - m
	return desvio * desvio
	
# lista é os desvios calculados para cada amostra	
def variancia(lista):
	soma = 0
	n = len(lista) - 1
	for item in lista:
		soma+=item
	return soma/n

# v é a variancia calculada para cada amostra
def st_deviation(amostras):

	lista_desvios = []

	m = media(amostras)

	for item in amostras:
		d = desvios(item, m)
		lista_desvios.append(d)

	v = variancia(lista_desvios)

	return round(math.sqrt(v),2)	
	

# Function to check each segment value with the average or median
# Receives as arguments the list of averages or medians, the list of standard deviations, and
# Size of the segments in dictionary
# Returns a list of frames to discard
#def verifica_segmentss(list_m, list_sd, dictionary_walk):
def verify_segments(list_m, list_sd, dicionary_walk):
	
	black_list = []
	
	for frame in sorted(dictionary_walk.keys()):
		for i in range(len(list_m)):
			base_major = list_m[i] + 2 * list_sd[i]
			base_minor = list_m[i] - 2 * list_sd[i]
			
			if dictionary_walk[frame][i] > base_major:
				if frame in black_list:
					continue
				else:
					black_list.append(frame)
			if dictionary_walk[frame][i] < base_minor:
				if frame in black_list:
					continue
				else:
					black_list.append(frame)

	return black_list	
	
#

#def time_of_cycle(list_step_size):
def cycle_time(list_step_size):
	p_v = peaks_and_valleys(list_step_size)
	peeks_positions = p_v['maxima_locations']
	list_of_ranges = []
	black_list = []

	before = 0
	next = 0
	for current_position in peeks_positions:
		next = current_position
		range = next - beforeaveragePeakRange
		list_of_ranges.append(range)
		before = next

	averagePeakRange = average_a(list_of_ranges)
	sdPeakRange = st_deviation(list_of_ranges)

	for difference in list_of_ranges:
		if difference > averagePeakRange + (sdPeakRange):
			black_list.append(difference)
		if difference < averagePeakRange - (sdPeakRange):
			black_list.append(diferencasdPeakRange

	return average_a(list(set(list_of_ranges) - set(black_list)))

#	

print sys.argv
if(len(sys.argv) < 2):
	print("**********************************************************************************")
	print("* Usage: calculate_antropometric_features.py [dicionary_list_name] 				*")
	print("**********************************************************************************")
	sys.exit(0)	

#dictionary com os pontos originais - Frames com valores faltando foram descartados
dictionary = {}

labels = ("Head,", "Shoulder-center,", "Shoulder-right,", "Shoulder-left,", "Elbow-right,", "Elbow-left,", "Wrist-right,", "Wrist-left,",
			   "Hand-right,", "Hand-left,", "Spine,", "Hip-center,", "Hip-right,", "Hip-left,", "Knee-right,", "Knee-left,",
			   "Ankle-righ,", "Ankle-left,", "Foot-right,", "Foot-left,", "Height,", "Cycle_time,", "Stride_size,", "Step_size,","velocity\n")

fw = open("attributes_with_average.csv", 'w')
for name in labels:
	fw.write(name)
fw.write('\n')
	
fw2 = open("attributes_with_median.csv", 'w')
for name in labels:
	fw2.write(name)
fw2.write('\n')

fw3 = open("step_size.csv", 'w')

#Open file with dictionary DOS path list
print "Reading dictionaries:"
if os.name == "posix":
	list_name = str(sys.argv[1]) 
	arqlst = open(list_name, 'r')
	
if os.name == "nt":
	list_name = str(sys.argv[1]) 
	arqlst = open(list_name, 'r')
	
files = arqlst.readlines()

for line in files:
	line = line.replace('\n','')
	print line
	fr = open(line, 'rb')
	dictionary = pickle.load(fr)
	file_name = line.split('_')
	individual = file_name[1]
	
	print "Calculating size of body segments from ", individual
	
	#dictionary da walk
	#contem todos os frames do individual
	#cada frame possui todos os sizes dos membros - ver Index[x]
	walk = {}
	step_size = {}
	height = {}
	
	for key in sorted(dictionary.keys()):
	
		print "Frame [",key,"]"
		
		#Listas - size = [0...18]
		#Contém as medias, medianas e desvio padrao dos sizes de membros calculados para o individual em questao
		list_average = []
		list_median = []
		list_sd_deviation = []
		list_step_size = []
		list_height = []
	
		walk[key] = []
		step_size[key] = []
		height[key] = []

			
		#Indexes 3D coordinates:
		#1 = x, 2 = y, 3 = z
		
		# Neck, shoulders, arms and hands
		
		#Index [0] - size neck
		#0 = head, 1 = shoulder_center
		p1 = (float(dictionary[key][0][1]), float(dictionary[key][0][2]), float(dictionary[key][0][3]))
		p2 = (float(dictionary[key][1][1]), float(dictionary[key][1][2]), float(dictionary[key][1][3]))
		neck = euclidean_distance(p1,p2)
		walk[key].append(euclidean_distance(p1,p2))
		
		#Index [1] - size shoulder_right
		#1 = shoulder_center, 2 = shoulder_right
		p1 = (float(dictionary[key][1][1]), float(dictionary[key][1][2]), float(dictionary[key][1][3]))
		p2 = (float(dictionary[key][2][1]), float(dictionary[key][2][2]), float(dictionary[key][2][3]))
		shoulder_right = euclidean_distance(p1,p2)
		walk[key].append(euclidean_distance(p1,p2))
		
		#Index [2] - size shoulder_left
		#1 = shoulder_center, 3 = shoulder_left
		p1 = (float(dictionary[key][1][1]), float(dictionary[key][1][2]), float(dictionary[key][1][3]))
		p2 = (float(dictionary[key][3][1]), float(dictionary[key][3][2]), float(dictionary[key][3][3]))
		shoulder_left = euclidean_distance(p1,p2)
		walk[key].append(euclidean_distance(p1, p2))
		
		#Index [3] - size arm_right
		#2 = shoulder_right, 4 = elbow_right (RIGHT)
		p1 = (float(dictionary[key][2][1]), float(dictionary[key][2][2]), float(dictionary[key][2][3]))
		p2 = (float(dictionary[key][4][1]), float(dictionary[key][4][2]), float(dictionary[key][4][3]))
		walk[key].append(euclidean_distance(p1, p2))
		
		#Index [4] - size arm_left
		#3 = shoulder_left, 5 = elbow_left (LEFT)
		p1 = (float(dictionary[key][3][1]), float(dictionary[key][3][2]), float(dictionary[key][3][3]))
		p2 = (float(dictionary[key][5][1]), float(dictionary[key][5][2]), float(dictionary[key][5][3]))
		walk[key].append(euclidean_distance(p1, p2))
		
		#Index [5] - size FOREarm_right
		#4 = elbow_right, 6 = wrist_right (RIGHT)
		p1 = (float(dictionary[key][4][1]), float(dictionary[key][4][2]), float(dictionary[key][4][3]))
		p2 = (float(dictionary[key][6][1]), float(dictionary[key][6][2]), float(dictionary[key][6][3]))
		walk[key].append(euclidean_distance(p1, p2))
		
		#Index [6] - size FOREarm_left
		#5 = elbow_left, 7 = wrist_left (LEFT)
		p1 = (float(dictionary[key][5][1]), float(dictionary[key][5][2]), float(dictionary[key][5][3]))
		p2 = (float(dictionary[key][7][1]), float(dictionary[key][7][2]), float(dictionary[key][7][3]))
		walk[key].append(euclidean_distance(p1, p2))
		
		#Index [7] - size hand_right
		#6 = wrist_right, 8 = hand_right (RIGHT)
		p1 = (float(dictionary[key][6][1]), float(dictionary[key][6][2]), float(dictionary[key][6][3]))
		p2 = (float(dictionary[key][8][1]), float(dictionary[key][8][2]), float(dictionary[key][8][3]))
		walk[key].append(euclidean_distance(p1, p2))
		
		#Index [8] - size hand_left
		#7 = wrist_left, 9 = hand_left (LEFT)
		p1 = (float(dictionary[key][7][1]), float(dictionary[key][7][2]), float(dictionary[key][7][3]))
		p2 = (float(dictionary[key][9][1]), float(dictionary[key][9][2]), float(dictionary[key][9][3]))
		walk[key].append(euclidean_distance(p1, p2))
		
		# spine and hip
		
		#Index [9] - size spine_superior		
		#1 = shoulder_center, 10 = spine
		p1 = (float(dictionary[key][1][1]), float(dictionary[key][1][2]), float(dictionary[key][1][3]))
		p2 = (float(dictionary[key][10][1]), float(dictionary[key][10][2]), float(dictionary[key][10][3]))
		spine_superior = euclidean_distance(p1,p2)
		walk[key].append(euclidean_distance(p1, p2))
		
		#Index [10] - size spine_inferior
		#10 = spine, 11 = hip_center
		p1 = (float(dictionary[key][10][1]), float(dictionary[key][10][2]), float(dictionary[key][10][3]))
		p2 = (float(dictionary[key][11][1]), float(dictionary[key][11][2]), float(dictionary[key][11][3]))
		spine_inferior = euclidean_distance(p1,p2)
		walk[key].append(euclidean_distance(p1, p2))
		
		#Index [11] - size hip_right
		#11 = hip_center, 12 = hip_right (RIGHT)
		p1 = (float(dictionary[key][11][1]), float(dictionary[key][11][2]), float(dictionary[key][11][3]))
		p2 = (float(dictionary[key][12][1]), float(dictionary[key][12][2]), float(dictionary[key][12][3]))
		hip_right = euclidean_distance(p1,p2)
		walk[key].append(euclidean_distance(p1, p2))
		
		#Index [12] - size hip_left
		#11 = hip_center, 13 = hip_left (LEFT)
		p1 = (float(dictionary[key][11][1]), float(dictionary[key][11][2]), float(dictionary[key][11][3]))
		p2 = (float(dictionary[key][13][1]), float(dictionary[key][13][2]), float(dictionary[key][13][3]))
		hip_left = euclidean_distance(p1,p2)
		walk[key].append(euclidean_distance(p1, p2))
		
		# Legs and Feets
		
		#Index [13] - size femur_right
		#12 = hip_right, 14 = knee_right (RIGHT)
		p1 = (float(dictionary[key][12][1]), float(dictionary[key][12][2]), float(dictionary[key][12][3]))
		p2 = (float(dictionary[key][14][1]), float(dictionary[key][14][2]), float(dictionary[key][14][3]))
		femur_right = euclidean_distance(p1,p2)
		walk[key].append(euclidean_distance(p1, p2))
		
		#Index [14] - size femur_left
		#13 = hip_left, 15 = knee_left (LEFT)
		p1 = (float(dictionary[key][13][1]), float(dictionary[key][13][2]), float(dictionary[key][13][3]))
		p2 = (float(dictionary[key][15][1]), float(dictionary[key][15][2]), float(dictionary[key][15][3]))
		femur_left = euclidean_distance(p1,p2)
		walk[key].append(euclidean_distance(p1, p2))
	
		#Index [15] - size_leg_right
		#14 = knee_right, 16 = ankle_right (RIGHT)
		p1 = (float(dictionary[key][14][1]), float(dictionary[key][14][2]), float(dictionary[key][14][3]))
		p2 = (float(dictionary[key][16][1]), float(dictionary[key][16][2]), float(dictionary[key][16][3]))
		leg_right = euclidean_distance(p1,p2)
		walk[key].append(euclidean_distance(p1, p2))
		
		#Index [16] - size_leg_left
		#15 = knee_left, 17 = ankle_left (LEFT)
		p1 = (float(dictionary[key][15][1]), float(dictionary[key][15][2]), float(dictionary[key][15][3]))
		p2 = (float(dictionary[key][17][1]), float(dictionary[key][17][2]), float(dictionary[key][17][3]))
		leg_left = euclidean_distance(p1,p2)
		walk[key].append(euclidean_distance(p1, p2))
		
		#Index [17] - size_foot_right
		#16 = ankle_right, 18 = foot_right (RIGHT)
		p1 = (float(dictionary[key][16][1]), float(dictionary[key][16][2]), float(dictionary[key][16][3]))
		p2 = (float(dictionary[key][18][1]), float(dictionary[key][18][2]), float(dictionary[key][18][3]))
		walk[key].append(euclidean_distance(p1, p2))
		
		#Index [18] - size_foot_left
		#17 = ankle_left, 19 = foot_left (LEFT)
		p1 = (float(dictionary[key][17][1]), float(dictionary[key][17][2]), float(dictionary[key][17][3]))
		p2 = (float(dictionary[key][19][1]), float(dictionary[key][19][2]), float(dictionary[key][19][3]))
		walk[key].append(euclidean_distance(p1, p2))

		#size step

		#step size: ankle_right[16] - foot_right[18] - ankle_left[17] - foot_left[19]
		p1 = (float(dictionary[key][16][1]), float(dictionary[key][16][2]), float(dictionary[key][16][3]))
		p2 = (float(dictionary[key][17][1]), float(dictionary[key][17][2]), float(dictionary[key][17][3]))
		
		p3 = (float(dictionary[key][16][1]), float(dictionary[key][18][2]), float(dictionary[key][16][3]))
		p4 = (float(dictionary[key][17][1]), float(dictionary[key][19][2]), float(dictionary[key][17][3]))
		
		heel_right = euclidean_distance(p1, p3)
		heel_left = euclidean_distance(p2, p4)

		step_size[key].append(euclidean_distance(p3, p4))


		#height
		#neck, spine superior, spine inferior, 
		#(qudril direito + hip esquerdo)/2 , (femur direito + femur esquerdo)/2, (perna direito + perna esquerda)/2
		height[key].append(float(neck + spine_superior + spine_inferior + ((hip_right + hip_left)/2) + ((femur_left + femur_right)/2) + ((leg_left + leg_right)/2) + ((heel_right + heel_left)/2)))
		
	
	# end of frame reading
	fr.close()
	
	#For each walk, the average, median and standard deviation of the size of each segment of the body
	#The List of index indicates the segment 0-18 (see above)
	for segments in range(19):
		list_average.append(media([walk[key][segments] for key in sorted(walk.keys())]))
		list_sd_deviation.append(media([walk[key][segments] for key in sorted(walk.keys())]))

	list_step_size.append([step_size[key][0] for key in sorted(step_size.keys())])
	list_height.append([height[key][0] for key in sorted(height.keys())])

	print "Numero de frames: ", len(walk.keys())
	print sorted(walk.keys())
	
	#Exclui frames fora da media + 2dps ou - 2dps
	frame_lista_negra = verifica_segmentss(list_average, list_sd_deviation, walk)
	for frame in frame_lista_negra:
		del walk[frame]
	print "Sobraram ", len(walk.keys()), " frames."
	print sorted(walk.keys())
	
	#Recalcula as medias e medianas para cada walk
	list_average = []
	list_median = []
	
	for segments in range(19):
		list_average.append(media([walk[key][segments] for key in sorted(walk.keys())]))
		list_median.append(media([walk[key][segments] for key in sorted(walk.keys())]))

	fw.write(individual)
	for i in range(len(list_average)):
		fw.write(','+ str(list_average[i]))
 
 #"Cycle_time,", "Stride_size,", "Step_size,","velocity"
	cycle_time = time_of_cycle([float(n) for n in list_step_size[0]]) / 30
	velocity = 2*average_a(max(list_step_size)) / cycle_time
	
	fw.write(',' + str(average_a(max(lista_altura))))
	fw.write(',' + str(cycle_time))
	fw.write(',' + str(2*(average_a(max(list_step_size)))))
	fw.write(',' + str(average_a(max(list_step_size))))
	fw.write(',' + str(velocity))
	#fw.write(',' + gender[individual])
	fw.write('\n')
	
	#Attributes with median
	fw2.write(individual)
	for i in range(len(list_median)):
	 	fw2.write(','+ str(list_median[i]))

	fw2.write(',' + str(median_a(max(list_step_size))) + ',' + str(2*median_a(max(list_step_size))) + ',' + str(median_a(max(lista_altura)))
	 		     + str(2*median_a(max(list_step_size)) / (time_of_cycle(list_step_size)/30)) + ',' + str(time_of_cycle(list_step_size)/30))
	fw2.write('\n')

	#Step values
	fw3.write(individual)
	for i in range(len(list_step_size)):
		fw3.write(',' + str(list_step_size[i]))
	fw3.write('\n')

fw.close()
fw2.close()
fw3.close()
