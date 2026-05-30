#VARIABLES AND DATA TYPES

name = "Vivek Anand"                                                         #STRING DATATYPE - STR
age = 18                                                                     #INTEGER DATATYPE - INT
subject = "Physics"
print("My name is " + name + ". I am " + str(age) + " years old.")           #CONVERTING INT TO STR
print("I am very passionate about " + subject + ".")

#DETERMINES THE DATATYPE OF VARIABLES
print(type(age))
print(type(name))

a = 3.14159
print(type(a))
b = True
print(type(b))
c = ("Physics", "Chemistry", "Mathematics")
print(type(c))
d = ["Physics", "Chemistry", "Mathematics"]
print(type(d))
e = ({"Physics", "Chemistry", "Mathematics"})
print(type(e))
