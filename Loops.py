x = 1
while x < 7
	print(x)
	x+= 1

>>> x = 1
>>> while x < 7:
...     print(x)
...     x += 1
...
1
2
3
4
5
6

While loop require variable ready.
	x = 1
	while x < 7 :
		print(x)
		if x == 5:
			break 
		x += 1
>>> x = 1
>>> while x < 7 :
...     print(x)
...     if x == 5:
...             break
...     x += 1
...
1
2
3
4
5	
For Loops
#for loops is iterating over a sequence.

fruits = ["apple", "banana", "orange", "pineapple","coconut", "cucumber"]
for x in fruits:
	print(x
fruits = ["apple" , "banana" , "orange" , " pineapple" , " coconut" , " cucumber"]
>>> for x in fruits:
...     print(x)
...
apple
banana
orange
 pineapple
 coconut
 cucumber

#looping in a String
or x in "pineapple":
...     print(x)
...
p
i
n
e
a
p
p
l
e 

#The break Statement

#stop after condition

 for x in fruits:
...     print(x)
...     if x == "pineapple":
...             break
...
apple
banana
orange
 pineapple
 coconut
 cucumber

 >>> fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
>>> for x in fruits:
...     if x == "pineapple":
...             break
...     print(x)
...
apple
banana
orange
>>> for x in fruits:
...     if x == "pineapple" and " coconut":
...             break
...     print(x)
...
apple
banana
orange

for x in fruits:
...     print(x)
...     if x== "coconut":
...             break
...             print(x)
...
apple
banana
orange
pineapple
coconut

> for x in fruits:
...     print(x)
...     if x == "coconut":
...             break
...
apple
banana
orange
pineapple
coconut

# The continye Statement - stop the current iteration
for x in fruits:
...     if x == "orange":
...             continue
...     print(x)
...
apple
banana
pineapple
coconut
cucumber

#The range () Function  - a set of code a specified number of times

for x in [1,2,3,4,5,6,7,8,9,10]
  File "<stdin>", line 1
    for x in [1,2,3,4,5,6,7,8,9,10]
                                  ^
SyntaxError: invalid syntax
>>> for x in [1,2,3,4,5,6,7,8,9,10]:
...     print(x)
...
1
2
3
4
5
6
7
8
9
10

> for x in range (10,100,5):
...     print(x)
...
10
15
20
25
30
35
40
45
50
55
60
65
70
75
80
85
90
95

#Nested loops
NumberA = [1,2,3,4,5]
>>> NumberB = [1,2,3,4,5]
>>> for x in NumberA:
...     for y in NumberB:
...             print(x,y)
...
1 1
1 2
1 3
1 4
1 5
2 1
2 2
2 3
2 4
2 5
3 1
3 2
3 3
3 4
3 5
4 1
4 2
4 3
4 4
4 5
5 1
5 2
5 3
5 4
5 5

erA = [1,2,3,4,5]
>>> NumberB = [1,2,3,4,5]
>>> NumberC = [1,2,3,4,5]
>>> for x in NumberA:
...     for y in NumberB:
...             for z in NumberC:
...                     print(x,y,z)
...
1 1 1
1 1 2
1 1 3
1 1 4
1 1 5
1 2 1
1 2 2
1 2 3
1 2 4
1 2 5
1 3 1
1 3 2
1 3 3
1 3 4
1 3 5
1 4 1
1 4 2
1 4 3
1 4 4
1 4 5
1 5 1
1 5 2
1 5 3
1 5 4
1 5 5
2 1 1
2 1 2
2 1 3
2 1 4
2 1 5
2 2 1
2 2 2
2 2 3
2 2 4
2 2 5
2 3 1
2 3 2
2 3 3
2 3 4
2 3 5
2 4 1
2 4 2
2 4 3
2 4 4
2 4 5
2 5 1
2 5 2
2 5 3
2 5 4
2 5 5
3 1 1
3 1 2
3 1 3
3 1 4
3 1 5
3 2 1
3 2 2
3 2 3
3 2 4
3 2 5
3 3 1
3 3 2
3 3 3
3 3 4
3 3 5
3 4 1
3 4 2
3 4 3
3 4 4
3 4 5
3 5 1
3 5 2
3 5 3
3 5 4
3 5 5
4 1 1
4 1 2
4 1 3
4 1 4
4 1 5
4 2 1
4 2 2
4 2 3
4 2 4
4 2 5
4 3 1
4 3 2
4 3 3
4 3 4
4 3 5
4 4 1
4 4 2
4 4 3
4 4 4
4 4 5
4 5 1
4 5 2
4 5 3
4 5 4
4 5 5
5 1 1
5 1 2
5 1 3
5 1 4
5 1 5
5 2 1
5 2 2
5 2 3
5 2 4
5 2 5
5 3 1
5 3 2
5 3 3
5 3 4
5 3 5
5 4 1
5 4 2
5 4 3
5 4 4
5 4 5
5 5 1
5 5 2
5 5 3
5 5 4
5 5 5

#Pass

words = ['cat', ' window', 'defenstrate', 'hello world']
>>> for w in words:
...     print(w,len(w))
...
cat 3
 window 7
defenstrate 11

 words = ['cat', 'window', 'defenstrate', 'Hello world']
>>> for w in words:
...     print(w,len(w))
...
cat 3
window 6
defenstrate 11
Hello world 11

for n in range (2, 10):
...     for x in range (2, n):
...             if n % x == 0:
...                     print(n, 'equals', x, '*' , n //x)
...                     break
...     else:
#loop fell through without finding a factor
...             print(n, ' is a prime number')
...
2  is a prime number
3  is a prime number
4 equals 2 * 2
5  is a prime number
6 equals 2 * 3
7  is a prime number
8 equals 2 * 4
9 equals 3 * 3

>>>
>>> for num in range(2, 10):
...     if num % 2 == 0:
...             print("Found an event number" , num)
...             break
...     print("Found a number", num)
...
Found an event number 2

>>> for num in range(2,10):
...     if num % 2 == 0:
...             print ("Found an even number",num)
...             continue
...     print ("Found a number",num)
...
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9
>>>
>>>
>>> for n in range(2, 10):
...     if num % 2 == 0:
...             print("Found an even number", num)
...             pass
...     print("Found a number",num)
...
Found a number 9
Found a number 9
Found a number 9
Found a number 9
Found a number 9
Found a number 9
Found a number 9
Found a number 9
>>>


