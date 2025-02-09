# https://www.edureka.co/blog/interview-questions/python-interview-questions/#WhatisthedifferencebetweenlistandtuplesinPython?


# Q37. What is pickling and unpickling?
# Ans:Pickle module accepts any Python object and converts
# it into a string representation and dumps it into a file by using dump function, this process is called pickling. While the process of retrieving original Python objects from the stored string representation is called unpickling.


# need more understanding on shallow copy and deep copy

# sallow copy and deep copy
# sallow copy is copy of object but not the object itself
# deep copy is copy of object and object itself
# sallow copy is done by copy.copy() and deep copy is done by copy.deepcopy()


# shallow copy
import copy
list1 = [1, 2, 3]
list2 = copy.copy(list1)
print(list1)
print(list2)
list2.append(4)
print(list1)
print(list2) 

# deep copy
list3 = [1, 2, 3]
list4 = copy.deepcopy(list3)
print(list3)
print(list4)
list3.append(4)
print(list3)
print(list4)  # this will not change

