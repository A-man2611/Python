# Type Conversion - automatically done by python
a = 2
b = 4.2
sum = a+b

print(sum) #<class 'float'> so 2 will be treated as 2.0
print(type(sum))

#Type casting - done manually by dev

a = int("2") #<class 'int'>
b = 4.25 
c= a + b
print(type(a))
print(c)