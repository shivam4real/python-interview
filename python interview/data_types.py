1#---------------------------------------------------------------------   LIST METHODS  ---------------------------------------------------------------

# Arrays are called list in python
# list are defined by []
# list are 0 based index
# list can have duplicate values
# list can have multiple types
#list are mutable


arr = [1,2,3,4,5]

# reverse the list
print(arr[::-1])
print(arr)
# list are dynamic in python
arr.append(6)
print(arr)

arr.pop()
print(arr)

# insert at specific index
arr.insert(2,10)
print(arr)
# list can have multiple types
# list can have list inside list


# initialize list with value 1 of size 5
n= 5
arr = [1]*5

print(arr)

# slicing a list
arr = [1,2,3,4,5]
print(arr[1:3])

# print all elemete except first
print(arr[1:])

# print first n elements
print(arr[:3])

# print all elements
print(arr[:])

# print last element
print(arr[-1])

# print last 2 element
print(arr[-2:])

# loop through list
for i in arr:
    print(i)

# loop through list with index
for i in range(len(arr)):
    print(arr[i])

# loop with enumerate
for i, val in enumerate(arr):
    print(i,val)

# sorting a list ascending
arr = [5,4,3,2,1]
arr.sort()
print(arr)

# sorting a list descending
arr = [8,4,5,10,1]
arr.sort(reverse=True)
print(arr)

# reverse a list
arr.reverse()

# sort a string list
arr = ['apple', 'orange', 'banana', 'grape']
arr.sort()
print(arr)

# sort a string list based on length
arr.sort(key=lambda x: len(x))
print(arr)

# sort a string list based on length descending
arr.sort(key=lambda x: len(x), reverse=True)
print(arr)

# sort a string list based on last character
arr.sort(key=lambda x: x[-1])
print(arr)

# list comprehension
arr = [i for i in range(5)] 

print(arr)

# list comprehension with condition
arr = [i for i in range(10) if i%2==0]  
print(arr)

# list comprehension with condition

arr = [i if i%2==0 else i*2 for i in range(10)]
print(arr)




# ---------------------------------------------------------------------   String  ---------------------------------------------------------------

# string are immutable
s = 'abc'
print(s)
print(s[1])
print(s[1:3])
print(s[-1])
print(s[:-1])
# this gives errors[0] = 'd'
# this will reate new string
s += 'd'
print(s)

# combine list string using join
arr = ['a','b','c']
s = ''.join(arr)
print(s)

#----------------------------------Set--------------------------------------------
# set are defined by {}
# set are unordered
# set are unique
# set are mutable
# set are dynamic
# set are not index based
# set can have multiple types

s = {1,2,3,4,5}
print(s)
s.add(6)
print(s)
s.remove(6)
print(s)

s = {1,2,3,4,5, 'abc'}  
print(s)

s.add('abc')
print(s)

# set operations
s1 = {1,2,3,4,5}    
s2 = {4,5,6,7,8}

# union
print(s1|s2)
print(s1.union(s2))

# intersection
print(s1&s2)
print(s1.intersection(s2))

# difference
print(s1-s2)
print(s1.difference(s2))

# set comprehension
s = {i for i in range(5)}
print(s)

# list to set
arr = [1,2,3,3,4,5]
s = set(arr)
print(s)


#----------------------------------Dictionary--------------------------------------------

# dictionary are defined by {}
# dictionary are key value pair
# dictionary are unordered
# dictionary are mutable
# dictionary are dynamic
# dictionary are not index based
# dictionary can have multiple types

myDict = {'a':1, 'b':2, 'c':3}
print(myDict)

# add new key value pair

myDict['d'] = 4
print(myDict)

# remove key value pair
del myDict['d']
print(myDict)

# get value by key
print(myDict['a'])

# get value by key
print(myDict.get('a'))

# get all keys
print(myDict.keys())

# get all values
print(myDict.values())

# dictionary comprehension
myDict = {i:i**2 for i in range(5)}
print(myDict)

# loop through dictionary
for key in myDict:
    print(key, myDict[key])

# loop through dictionary
for key, val in myDict.items():
    print(key, val)




#----------------------------------Tuple--------------------------------------------
# tuple are defined by ()
# tuple are ordered
# tuple are immutable
# tuple are not dynamic
# tuple are index based
# tuple can have multiple types

t = (1,2,3,4,5,5)
print(t)
print(t[1])
print(t[1:3])
print(t[-1])
print(t[:-1])

#loop through tuple
for i in t:
    print(i)

# ----------------------------------Heapq--------------------------------------------

# heapq is a min heap
# heapq is a binary tree
# heapq is a complete binary tree
# heapq is a binary heap
# heapq is a priority queue
# heapq is implemented as a list
# heapq is 0 based index
# heapq is mutable
# heapq is dynamic
# heapq is not index based

import heapq
arr = [5,4,3,2,1]
heapq.heapify(arr)
print(arr)

# push element to heap
heapq.heappush(arr, 6)
print(arr)

# pop element from heap
print(heapq.heappop(arr))
print(arr)

# get smallest element from heap
print(arr[0])