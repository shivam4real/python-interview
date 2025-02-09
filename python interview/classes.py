from abc import ABC, abstractmethod

# class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.

class Person:
    # __init__ is a reserved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f'''Hello my name is {self.name} and I am {self.age} years old''')

p1 = Person("John", 36)
p1.myfunc()

# Core onecpts of OOP are:
# Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Encapsulation is the concept of restricting access to methods and variables in a class.
# Abstraction is the concept of hiding the real implementation of an application from the user and emphasizing only on usage of it.


# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationyear = year

    def welcome(self):
        print(f'''Welcome {self.name} to the class of {self.graduationyear}''')

s1 = Student("Mike", 22, 2020)
s1.myfunc()
s1.welcome()


# Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
# Polymorphism allows methods to do different things based on the object that calls them.
# Polymorphism is useful when the same method name is used for different classes.
class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

def func(obj):
    obj.capital()
    obj.language()
    obj.type()

ind = India()
usa = USA()

func(ind)
func(usa)

# polymorphism Example 2
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Dog(Animal):
    def speak(self):
        return self.name + " says Woof!"
    
class Cat(Animal):
    def speak(self):
        return self.name + " says Meow!"
    
fido = Dog("Fido")
isis = Cat("Isis")

print(fido.speak())
print(isis.speak())



# Encapsulation is the concept of restricting access to methods and variables in a class.
# This can prevent the data from being modified by accident and is known as encapsulation.
# Encapsulation can be achieved by using private methods and private attributes in a class.
# In Python, private attributes and methods are defined by prefixing the attribute or method name with double underscores.
# Python does not have a mechanism that effectively restricts access to any instance variable or method.
# Python uses name mangling to effectively make a variable or method private.
# Python performs name mangling by adding a prefix _<class-name> to the attribute or method name.
class Car:
    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print("Driving")

    def __updateSoftware(self):
        print("Updating software")

redcar = Car()
redcar.drive()
redcar.__updateSoftware() # AttributeError: 'Car' object has no attribute '__updateSoftware'
# Accessing the private method using name mangling
redcar._Car__updateSoftware()

# Abstraction is the concept of hiding the real implementation of an application from the user and emphasizing only on usage of it.
# Abstraction is achieved by using abstract classes and interfaces in Python.
# Python does not have any built-in abstract class or interface.
# Python comes with a module which provides the base for defining Abstract Base classes(ABC) and that module name is ABC.
# ABC works by decorating methods of the base class as abstract
# Abstract class is a class that contains one or more abstract methods.
# Abstract method is a method that is declared, but contains no implementation.
# Abstract class cannot be instantiated and it is designed to be subclassed.
# Abstract class can have both normal methods and abstract methods.
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Instantiate objects of Dog and Cat
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow


# Abstarction Example 2

from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    # Create abstract method      
    @abstractmethod
    def printDetails(self):
        pass
  
    # Create concrete method
    def accelerate(self):
        print("Speed up ...")
  
    def break_applied(self):
        print("Car stopped")

# Create a child class
class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Not having this feature")

# Create a child class
class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Available")

# Create an instance of the Hatchback class
car1 = Hatchback("Maruti", "Alto", "2022")

# Call methods
car1.printDetails()
car1.accelerate()
car1.sunroof()



# Python also allows to create a class without any content, using the pass statement.
class MyClass:
    pass

# Python allows to delete a property or method of an object using del keyword.
# del object_name.property_name
# del object_name.method_name
# del object_name
del s1.graduationyear
s1.myfunc()
# print(s1.graduationyear) # AttributeError: 'Student' object has no attribute 'graduationyear'

# Python allows to delete objects using del keyword.
del s1
# print(s1) # NameError: name 's1' is not defined

# Python allows to delete a class using del keyword.
del MyClass
# print(MyClass) # NameError: name 'MyClass' is not defined

# Python allows to delete a property or method of a class using del keyword.
# del class_name.property_name
# del class_name.method_name
# del class_name
del Student.welcome
s1.myfunc()
# s1.welcome() # AttributeError: 'Student' object has no attribute 'welcome'


# class variables are shared by all instances of a class.
# Instance variables are unique to each instance of a class.

class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

obj1 = MyClass("Instance 1")
obj2 = MyClass("Instance 2")

print(obj1.class_variable)  # Output: I am a class variable
print(obj1.instance_variable)  # Output: Instance 1
print(obj2.instance_variable)  # Output: Instance 2


# class method and static method
# class method takes cls as the first parameter
# static method does not take any parameter
# class method can modify the class state
# static method cannot modify the class state


class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        return cls.class_variable

    @staticmethod
    def static_method():
        return "I am a static method"
    
obj1 = MyClass("Instance 1")
obj2 = MyClass("Instance 2")

print(obj1.class_method())  # Output: I am a class variable
print(obj1.static_method())  # Output: I am a static method


# property decorator allows to define a method that can be accessed like an attribute
# property decorator allows to define a getter, setter, and deleter for a method
# property decorator can be used to define a read-only attribute
# property decorator can be used to define a write-only attribute
# property decorator can be used to define a delete-only attribute

class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @value.deleter
    def value(self):
        del self._value

obj = MyClass(10)
print(obj.value)  # Output: 10
obj.value = 20
print(obj.value)  # Output: 20
del obj.value

# method overiding

class Parent:
    def method(self):
        print("Parent method")

class Child(Parent):
    def method(self):
        print("Child method")

obj = Child()
obj.method() 


# MRO (Method Resolution Order) is the order in which methods should be inherited in the presence of multiple inheritance.

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

