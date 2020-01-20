Tuple - ()

t = 12345, 54321, 'hello!'
t[0]

t
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)

# Tuples are immutable:

C:\Users\User>python
Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> t =12345, 54321, 'hello!'
>>> t
(12345, 54321, 'hello!')
>>> t[0]
12345
>>> t[2]
'hello!'
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> u[0]
(12345, 54321, 'hello!')
>>> u[1]
(1, 2, 3, 4, 5)
>>> t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

>>> fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
>>> print(fruits[2:5])
('cherry', 'orange', 'kiwi')

#change Tuples Value (tuple to list -> list to Tuple)

x = ("apple", "banana", "cherry", "orange")
y = list(x)
y[1] = "mango"
x = tuple(y)
x

> x = ("apple", "banana", "cherry", "orange")
>>> y = list(x)
>>> y[1] = "mango"
>>> x = tuple(y)
>>> x
('apple', 'mango', 'cherry', 'orange')

 y[2] = "kiwi"
>>> x = tuple(y)
>>> x
('apple', 'mango', 'kiwi', 'orange')


int , string , bool , float 
5.0

>>>Set - {}