import os
import sys

print("**********************")
print("* Create files.list  *")
print("**********************")

if(len(sys.argv) < 2):
	print("***************************************************")
	print("* Usage: create_files_list.py [main_directory_name] *")
	print("****************************************************")
	print("\t Returns [main_directory_name]_files.list and [main_directory_name]_persons.list")
else:
	#Create files.list and persons.list with the list of directories with walk files and a list of persons names (labels)
	#Use the main_diretory that contains all directories with persons walk files
	# MacOS Users: remove .DS_Store from list if added
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

	path = sys.argv[1]
	path = path.replace("/", "")
	print "Creating file and person list with name :", path , "_files.list", path , "_persons.list"

	fw = open(path + "_files.list", 'w')
	fw2 = open(path + "_persons.list", 'w')

	for root, dirs, files in os.walk(path):
		names = dirs
		files.sort()
		files = [f for f in files if not f.startswith('.')]
		for file in files:
			if not 'files.list' in file:
				temp = os.path.join(root, file)
				fw.write(temp + '\n')

		for p in names:
			fw2.write(p + '\n')

	fw.close()
	fw2.close()
