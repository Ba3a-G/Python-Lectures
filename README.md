# Python Lecture Notes

This page will automatically be updated to include all the Python concepts that have been taught in the class. To discuss any academic doubt, *or just rant about your day*, you can join **[our Discord server (group)](https://discord.lpucoders.club)**.

If you want to help me keep this page updated, or just talk, please message me on [Instagram](https://instagram.com/ba3a.gamzo) / [Discord](https://discordapp.com/users/585512479241666570).
*<p>-Ba3a</p>*

***

## Comments
It hides a part of the code from the interpreter. It can be used to provide documentation to other developers.
```python
# this is a comment
```

## Docstrings
To provide documentation to a Class or a Function.
```python
"""This is a multi
line Docstring."""
```

## Indentifiers
Indentifiers are variables, these can be variable names, class names, function names, or other objects.
```python
name = "Ba3a"

def exampleName():
    pass

class Name():
    pass

list = [example, listObject]
```
name, exampleName, and Name are valid identifiers.

## `type` Function
You can check the date type of a variable with `type()`, which is an inbuilt function.
```python
something = 56
print(type(something))

Response: int
```

## Binding
Assigning a value to a variable is done with the `=` operator.
```python
something = "this value is being stored"
```

If you try to access a variable that has not yet been assigned, you get `NameError: name '' is not defined`.

## Type Conversion
You can convert different data types by using following methods to their respective data type.

| To data type | Method |
|---|---|
| Integer | int() |
| String | str() |
| Float | float() |

```python
# If you want to convert "23", which is a string to an integer
int("23") # 23
# Similarly if you want to convert 56, which is an integer to a string
str(56) # "56"
int(5.9) # 5
float(5) # 5.0
```
Please note that the value you want to convert must be compatible (duh?). You can't convert some alphabet to integer using the `int()` method. You will get `ValueError`.

## Input
Takes input from the user. By default, the input is in `str` data type.
```python
myInput = input("What's your name: ")
```

## String Concatenation
String concatenation means add strings together. Use the + character to add a variable to another variable:
```python
x = "Python is "
y = "awesome"
z =  x + y
print(z) #Python is awesome
```
Or if you want to add some variable (str, int, or bool), you can use:
```python
age = 18
print("Hello! I am Ba3a and my age is ", age) # Hello! I am Ba3a and my age
```

## Operators
There are seven different types of operators.
### Arithmetic Operators
+, -, *, /, //, % <br>
_work in progress_

## If Else Statements
You can execute a block if a condition is true, or execute another block if the condition is false.
```python
if 4<5:
    print("It will execute this block.")
else:
    print("It won't execute this block.")

if 4>5:
    print("It won't execute this block.")
else:
    print("It will execute this block.")
```