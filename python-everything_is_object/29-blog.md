# Python - Everything is object

![Everything is an object](pythonobject.png)

An object in Python is like a container that holds data and knows how it behaves. It's been interesting to see how Python works, and how it handles objects in memory. I now have an understanding of how everything in Python is an object. Rather than variables storing values, it actually points to the object in memory as a reference. Every list, string, number, and even functions themselves live in memory as objects that code interacts with. Understanding this idea has helped me see how variables, references, and object behaviour actually work behind the scenes.

## `type()`
There are mutliple different types of objects. To view the type, wrap the variable inside `type()`.

### Example 1 - Numbers:
```python
x = 10
print(type(x))
```
Output:
```bash
<class 'int'>
```
This tells you the object is an integer.
<br><br>

### Example 2 - String:
```python
name = "Carla"
print(type(name))
```
Output:
```
<class 'str'>
```
This tells you the object is a string.
<br><br>

### Example 3 - List:
```python
nums = [1, 2, 3]
print(type(nums))
```
Output:
```bash
<class 'list'>
```
This tells you the object is a list.
<br><br>

### Example 4 - Dictionary:
```python
person = {"name": "Carla"}
print(type(person))
```
Output:
```bash
<class 'dict'>
```


## `id()`
In Python, every object in Python has a unique identifier, which in CPython, is the object's memory address. To display this, you can wrap your variable inside `id()`.

For example:
```python
x = 10
print(id(x))
```
This will print the variable id:
```bash
140726794751328
```
<br><br>

If two variables point to the same object, their id's will be the same as both variables are pointing to the same memory address like this `a ─────────▶ [1, 2, 3] ◀──────── b`.

For example:
```python
a = [1, 2, 3]
b = a

print(id(a))    # example: 140805127282688
print(id(b))    # same number
```
<br><br>

If the variables are not linked, the objects are different, which means their id's will also be different.

Example:
```python
nums = [1, 2, 3]
other = [1, 2, 3]

print(id(nums))
print(id(other))
```
Each statement will print two different variable id's, as each variable is a unique list.


## Immutable Objects
An immunable object is a type of object you cannot change once it's created. If you try and change it, Python creates a new object.

**Immutable Types:**
- integers
- floats
- strings
- tuples
- bools
<br><br>

Example:
```python
name = "carla"
name = name.upper()
```
Here, it looks like `"carla"` is changed to `"CARLA"`. However, what Python actually did was create a new string `"CARLA"`, and `name` now points to this new object.

## Mutable Objects
A mutable object is a type of object you can change after its created. You can modify it in place, without creating a new object.

**Mutable Types:**
- lists
- dictionaries
- sets
- bytearrays
<br><br>

Example:
```python
nums = [1, 2, 3]
nums.append(4)
```

The same list in memory was changed. `nums` will be appended and the output will then be:
```bash
[1, 2, 3, 4]
```






