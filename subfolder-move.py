import os, shutil

ld = os.listdir(path='.')

total_folders_moved = 0
for i in ld:
	if os.path.isdir(i):
		# print(i)
		ld = os.listdir(path='./'+i)
		# print(ld)
		for x in ld:
			# print(os.getcwd()+'/'+i+'/'+x)
			if os.path.isdir(i+'/'+x):
				print(x)
				shutil.move(i+'/'+x, '.')
				total_folders_moved += 1



print(total_folders_moved, 'folders moved.')