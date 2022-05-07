import os

#path = 'test/0507_02/img'
path = 'img'

list = []
# Scan all file.jpg in img/
for (root, dirs, file) in os.walk(path):
	for f in file:
		if '.jpg' in f:
			f = f.replace('.jpg', '')
			list.append(f)

print(list)

for i in list:
	# cmd /k : remain after run
	# cmd /c : terminate after run
	os.system('cmd /c "python main.py -i img/%s.jpg"' %i)