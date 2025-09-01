#List - A built in data type that stores set of values 
# It can store elements of different types(int, float, string etc)
marks = [89.8,34.8,89.9,89.6]
print(marks)
print("Types of marks:",type(marks))
print("marks at 0",marks[0])
print("Length of list",len(marks))

# Also we can store like this - diffeerent data type 
student = ["Aman",28,"Python"]
print(student)

#NOTE - STRINGS are immutable
#NOTE - LIST are mutable
# so index changes are allowed in list but not in string
student[0] = "Akash"
print("New changes",student)

#List Slicing
# Similar to string slicing
# list_name[starting index: endingindx]
mk = [34,246,43,65,7]
print(mk[1:4])