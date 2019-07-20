import os
import sys

print("**********************")
print("* Create files.list  *")
print("**********************")

if(len(sys.argv) < 2):
	print("***************************************************")
	print("* Usage: create_files_list.py [main_directory_name]*")
	print("****************************************************")
else:
	#Create files.list and persons.list with the list of directories with walk files and a list of persons names (labels)
	#Use the main_diretory that contains all directories with persons walk files
	
	#main_directory
	#|
	#|--- Person1_directory
	#		|---- walk_sample_1.txt
	#		|---- walk_sample_2.txt
	#       |---- walk_sample_3.txt
	#|--- Person2_directory
	#		|---- walk_sample_1.txt
	#		|---- walk_sample_2.txt
	#       |---- walk_sample_3.txt
	#....

	fw = open("files.list", 'w')
	fw2 = open("persons.list", 'w')
	
	path = sys.argv[1]
	print path

	for root, dirs, files in os.walk(path):
		names = dirs
		files.sort()
		for file in files:
			if not 'files.list' in file:
				temp = os.path.join(root, file)
				fw.write(temp + '\n')
				
		for p in nomes:
			fw2.write(p + '\n')
			
	fw.close()
	fw2.close()