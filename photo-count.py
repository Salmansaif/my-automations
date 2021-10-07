import os

ld = os.listdir(path='.')

fo = open("log.txt", "w+")
total_files_count = 0
for i in ld:
	if os.path.isdir(i):
		# os.chdir(i)
		browse = os.listdir(i)
		files_count = 0
		for file in browse:
			if file.endswith('.jpeg') or file.endswith('.jpg') or file.endswith('.png'):
				print(file)
				fo.write(file+'\n')
				files_count += 1
				total_files_count += 1
		file_count = '> File count in folder ' + str(i) + ': ' + str(files_count) + '\n' + '------' + '\n'
		print(file_count)
		fo.write(file_count)
		# print('------')

total_files = 'Total Files: ' + str(total_files_count)
print(total_files)
fo.write(total_files)
fo.close()