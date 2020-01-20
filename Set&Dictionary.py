# Sets

#includes a data type for sets.
#Curly braces or the set() function can be used to create sets.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)
{'orange', 'pear', 'apple', 'banana'}

#show that duplicates have been removed
 'orange' in basket       # fast membership testing
 'orange' in basket
True
>> 'crabgrass'in basket
False

#Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam') 

a = set('abracadabra')
>>> b = set('alacazam')
>>> a
{'r', 'd', 'a', 'c', 'b'}
>>> a | b
{'r', 'd', 'a', 'c', 'b', 'm', 'l', 'z'}
>>> a & b
{'c', 'a'}
>>> a ^ b
{'r', 'd', 'm', 'l', 'z', 'b'}
>>> b - a
{'m', 'z', 'l'}

a - b             #unique letters in a
a | b             #letters in a but not in b
a & b             #letters in a or b or both
a ^ b             #letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
>>> a = {x for x in 'abracadabrad' if x not in 'abc'}
>>> a
{'r', 'd'}

fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)

fruits.add("cucumber")
fruits
>>> fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
>>> print("cherry" in fruits)
True
>>>
>>> fruits.add("cucumber")
>>> fruits
{'melon', 'cucumber', 'cherry', 'orange', 'kiwi', 'mango', 'apple', 'banana'}
>>> fruits.append("pineapple")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'set' object has no attribute 'append'

>> fruits.update("grape")
>>> fruits
{'r', 'a', 'p', 'melon', 'cucumber', 'g', 'cherry', 'orange', 'kiwi', 'mango', 'apple', 'e', 'banana'}

>> fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
>>> fruits.remove("banana")
>>> fruits
{'melon', 'cherry', 'orange', 'kiwi', 'mango', 'apple'}
>>>

fruits.discard("kiwi")

>>> fruits.discard("kiwi")
>>> fruits
{'melon', 'cherry', 'orange', 'mango', 'apple'}

>>>Dictionaries

#Dictionaries

#Another useful data type built into Python is the dictionary

tel = {'jack': 4098, 'scape': 4139}
tel['scape']

>>> tel = {'jack': 4098, 'scape': 4139}
>>> tel['scape']
4139
>>> tel[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 1
>>> tel['jack']
4098

>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'scape': 4139, 'guido': 4127}
>>> del tel['scape']
>>> tel
{'jack': 4098, 'guido': 4127}

>>> tel['irv'] = 4137
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4137}

>>> list(tel)              #Change to list
['jack', 'guido', 'irv']
>>> sorted(tel)            #Alphabet Sorting
['guido', 'irv', 'jack']

>>> 'guido' in tel
True
>>> 'jack' not in tel
False

dict([('scape', 4139), ('guido', 4127), ('jack', 4098)])   #change to dict
dict(scape=4139, guido=4127, jack=4098)

>>> dict([('scape', 4139), ('guido', 4127), ('jack', 4098)])
{'scape': 4139, 'guido': 4127, 'jack': 4098}
>>> dict(scape=4139, guido=4127, jack=4098)
{'scape': 4139, 'guido': 4127, 'jack': 4098}

{x: x**2 for x in (2, 4, 6)}

for x in 2, 4, 6:
	print(x:x**2)
2 : 4
4 : 16
6 : 36


>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}

{x: x**3 for x in (1, 2, 3, 4, 5)}
1 : 1
2 : 8
3 : 27
4 : 64
5 : 125

>>> {x: x**3 for x in (1, 2, 3, 4, 5)}
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

#When looping through dictionaries

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():

knights = {'gallahad': 'the pure', 'robin': 'the brave', 'scape' : 4355}
>>> for x, y in knights.items():																								

>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
        print(k, v)
...
gallahad the pure
robin the brave
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave', 'scape' : 4355}
>>> for x, y in knights.items():
...     print(x,y)
...
gallahad the pure
robin the brave
scape 4355


for i, v in enumerate(['tic', 'tac', 'toe']):

>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe

>>> for x, y in enumerate([1000, 2000, 3000]):
...     print(x, y)
...
0 1000
1 2000
2 3000

>>> questions = ['name', 'quest', 'favourite colour']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}? It is {1}.'.format(q, a))

>>> questions = ['name', 'quest', 'favourite colour']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}? It is {1}.'.format(q, a))
...
What is your name? It is lancelot.
What is your quest? It is the holy grail.
What is your favourite colour? It is blue.


>>> questions = ['name', 'quest', 'favourite colour']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> results = ['1', '2', '3']
>>> for q, a, i in zip(questions, answers, results):
...     print('What is your {0}? It is {1}. It is No.{2}'.format(q, a, i))
...
What is your name? It is lancelot. It is No.1
What is your quest? It is the holy grail. It is No.2
What is your favourite colour? It is blue. It is No.3
>>> print('{0} and {1}, {2}'.format('spam', 'eggs', 'colour'))
spam and eggs, colour
>>> print('{0} and {1}, {2} and {3}'.format('spam', 'eggs', 'colour','food'))
spam and eggs, colour and food



>>>If_Else_statement












































































































