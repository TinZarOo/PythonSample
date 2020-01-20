#If Else Statements
If_Else_Statement.py

#Boolean Expression

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello Workd"))
print(bool(20))
print(20 > 10)
True
>>> print (20 == 10)
False
>>> print (bool("Hello World"))
True

Python Conditions

Equals          			 -> x == y
Not Equals					 -> x != y
Less than					 -> x < y
Less than or equal to 		 -> x <= y
Greater than 				 -> x > y
Greater than or equal to     -> x => y
Boolean OR                   -> x or y , x | y
Boolean AND                  -> x and y, x & y
Boolean NOT                  -> not x
x = 0
>>> if x == 0:
...     print ("Hello")
... else:
...     print ("world")
...
Hello
   x = 10
>>> if x == 0:
...     print ("Hello")
... elif x != 0:
...     print ("World")
... elif x >= 20:
...     print ("x is 20")
... else:
...     print ("x is 10")
...
World


x = 10
>>> if x == 0:
...     print ("x is zero")
... elif x != 0:
...     print ("x is equal zero")
... elif x < 20:
...     print ("x is 20")
... elif x == 10:
...     print ("x is 10")
... else:
...     print ("x is nothing")
...
x is equal zero


>>> x = 70
>>> y = 70
>>> if x > y:
...     print ("x is greater than y")
... elif x == y:
...     print ("x and y are equal")
...
x and y are equal

 x = 50
>>> y = 150
>>> if x > y:
...     print (" x is greater than y")
... elif x == y:
...     print ("x and y are equal")
... else:
...     print (" x is less than y")
...
 x is less than y

 x = 50
>>> y = 150
>>> print(x) if x > y else print (y)
150


#And is logical operator
x = 50
>>> y = 40
>>> z = 100
>>> if x > y and z > x:
...     print ("All Conditions are True")
...
All Conditions are True


#Or is logical operator
 x = 50
>>> y = 40
>>> z = 100
>>> if x > y or z < y:
...     print("one of the conditions is True")
... elif x > y and z > y:
...     print ("All conditions are True")
... else:
...     print ("nothing else")
...
one of the conditions is True

 x = 50
>>> y = 40
>>> z = 100
>>> if x > y and x > z:
...     print ("All Conditions are True")
... else:
...     print ("one condition is True")
...
one condition is True

 x = 50
>>> y = 40
>>> z = 100
>>> if x > y or x > z:
...     print ("All conditions are True")
... else:
...     print ("one condition is True")
...
All conditions are True

x = 50
>>> y = 40
>>> z = 100
>>> if x > y and z > y or x > z:
...     print (" All conditions are true")
... else:
...     print("one condition is True")
...
 All conditions are true

# Nested If is if statements in if statements
x = 50
>>> if x > 10:
...     print (" x is ten")
...     if x > 20:
...             print("x is greater than 20")
...     else:
...             print("No,x is not greater than 20")
...
 x is ten
x is greater than 20

 = 50
>>> if x < 10:
...     print (" x is ten")
...     if x > 20:
...             print ("x is greater than 20")
...     else:
...             print("No, x is not greater than 20")

int(input("Examination Result :"))
	100 - 90	- A
	89  - 70	- B
	69  - 60	- C
	59  - 40 	- D
	39  - 10  	-Fail

	int(input("Examination Result :"))
	100 - 90	- A
	89  - 70	- B
	69  - 60	- C
	59  - 40 	- D
	39  - 10  	-Fail

	if x >=70 and x < 90:
			print ("Grade B")


if x >= 70 and 90 :
		print("Grade B")
if x >= 100 and x<= 0:
		print("Grade A")
elif x >= 40 and x <= 0
