# with open('text.txt', 'r') as rf:
# 	with open('textCOPY.txt', 'w') as wf:

# 		for line in rf:
# 			wf.write(line)

with open('dog.jpg', 'rb') as rf:
	with open('dog_copy.png', 'wb') as wf:

		for line in rf:
			wf.write(line)


