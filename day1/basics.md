# Python Basics

## 1. Integer/Float

```py
a = 100.199
print(f"The data type of a is '{type(a)}' and the value is '{a}'")
a = int(a)
print(f"after type casting data type of a is '{type(a)}' and the value is '{a}'")
a = str(a)
print(f"Now data type of a is '{type(a)}' and the value is '{a}'")
```
## 2. List
**Lists are used to store multiple items in a single variable.**
```py
# List can contain multiple data types
a = [1,1,2,3,4,'abc', 1.43]
print(a)

# Adding and deleting data from list

a.append(123)
print(a)
a.remove(1)
print(a)
# List Slicing
# list[start:end:steps]
a[:6:2]

# For loop in list
for i in a:
    print(a)
```
## 3. Dictionaries
**Dictionaries are used to store data values in key:value pairs.**
```py
d = {
    "40110122": {
            "name": "Aryan Amish",
            "roll": "20S115893",
            "branch": "CSE",
            "batch": "2020-2024",
    },
        "40110123": {
            "name": "xyz",
            "roll": "13314212",
            "branch": "CSE",
            "batch": "2020-2024",
    }
}

# Acessing a Value in Dict
d["40110122"]["name"]

# For loop in dict
for i, j in d.items():
    print(f"Key: {i}, \n\tValue: {j}")
```
## 4. Sets
**Sets are used to store multiple items in a single variable. It has O(1) search time complexity**
```py
s = {1,2,3,4,"hi there", 12.4}
print(s)
# adding items in sets
s.add("hello")
# removing item in sets
s.remove("hi there")
print(s)

# Search Items in sets
print(1 in s)
print('hello' in s)
print(12341 in s)
```
## 5. Bool
**bool is a data type which stores only True and False value**
    
```py
b = False
```

## 6. Tuple
**Tuple is just like list but you cannot change the value of tupe once it is defined**
```py
t = (1,2,34)
print(t)
```

## 7. For Loop

**For Loop is used for Looping over some data type or looping over a interval**
```py
# this will print the number from 0-9
for i in range(10):
    print(i)

# this will print the items of the list
for i in [1,2,3,4,5]:
    print(i)

# this will print each character of the string
for i in "hi there":
    print(i)
```

## 8. While Loop
**With the while loop we can execute a set of statements as long as a condition is true.**
```py
# this loop will print from 0 to 10
a = 0
while a<=10:
    print(a)
    a += 1
```