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