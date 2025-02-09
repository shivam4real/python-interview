#python variable are dynamically typed
# Means we dont need to define them .
n = 0 
print(n)

# type is determine at run time
n= 'abc'

print(n)


#muliple aignment 

n,m = 0 , 'abc'
print(n , m )

# incremnet 
# good way to increment
n = n + 1
print(n)
# good way to increment
n +=1
print(n)
# this is not valid in python# this is not valid in python
# n++ 
# print(n)



# None is null in python
n = 4
n = None
print(n)

# logical operators
# intstead of && , || , ! we use and , or , not


# Loops
# while loop
n = 0
while n < 5:
    print(n)
    n += 1

# for loop start from 0 to 5
for i in range(5):
    print(i)

# for loop start from 2 to 5
for i in range(2,5):
    print(i)

# for loop start from 2 to 5 with step 2
for i in range(2,5,2):
    print(i)

# for loop start from 5 to 3 with step -1
for i in range(5,2,-1):
    print(i)


# division
# demical division by default
print(5/2)


# integer division
print(5//2)


# negative division
print(-5/2)
# negative integer division will round to -3
print(-5//2)


# modulo operator
print(5%2)
print(5%3)

# negative modulo operator 
print(-10%3)


# neagtive modulo operator can ause issue in some cases so use math.fmod
import math
print(math.fmod(-10,3))

# power operator
print(2**3)

# power operator    
print(2**0.5)


# math functions
import math
print(math.ceil(2.3))
print(math.floor(2.3))
print(math.factorial(5))
print(math.sqrt(4))
print(math.exp(2))
print(math.log(10))
print(math.log10(10))
print(math.sin(30))


# max and min infinite values
float('inf')
float('-inf')

