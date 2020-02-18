# "r" - Read

# "a" - Append

# "w" - Write

# "x" - Create

# "t" - Text

# "b" - Binary

# open & Read File

f = open('text.txt', 'r') # R - Read
# print(f.name)
# f.close()



# with open('text1.txt', 'a') as g:
# 	g.write('This is line number '+"\n")
# 	print(g,end='')


with open('text.txt', 'r') as f:

	f_text = f.readline()
	print(f_text,end='')

	for f_text in f:
		print(f_text,end='')

	# f_text = f.readline()
	# print(f_text,end='')

# 	f_text = f.readline()
# 	print(f_text,end='')

# 	for f_text in f:
# 		print(f_text,end='') 

	# f_text = f.read(70)
	# print(f_text,end='')


	# f_text = f.read(100)

	# while  100 > 0:
	# 	print(f_text,end='')