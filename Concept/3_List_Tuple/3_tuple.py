# A built in data type that lets us create immutable sequence of values\
# So Strings and tuple are imutable

tup = (1,23,4,5,45,13,22)
print(tup)
print("type of tuple",tup)

print(tup[0])
# tup[0] = 5 - this wont work as its value can't be changed (making it immutables)

#assignment
tupple = () #empty tuple
#NOTE: You cannot write like this 
# as here python will think like it if type int or float
tpl = (2) #<class 'int'> #or tpl = (2.0) <class 'float'>

# so better to write like
tpl = (2,)

#TUPLE SLICING
print(tup[:2]) #same ending index is excludeds