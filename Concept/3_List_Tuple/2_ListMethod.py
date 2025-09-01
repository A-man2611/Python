#There are couple of list method
list1 = [1,2,3,4,1,2,3]

list1.append(4) #adds 4 at end
print(list1)

list1.sort() #will make the list in ascending order
print(list1)

list1.sort(reverse=True) #will make the list in descending(by default reverse is False making it ascending)
print(list1)

list1.reverse() #it will reverse the element in list
print(list1)

list_Str= ["akshay","raman","kripa"]
list_Str.reverse()
print("string:",list_Str)

list_Str.sort()
print(list_Str)

list1.insert(3,8) #index 3 element 8
print(list1)

list1.remove(8) # delete the occurenece of 8's first occurenece 
print(list1)

list2=[9,8,6,0,6]
list2.pop(3) #delete third index
print(list2) 

copy_list= list2.copy()#copy the list
print("Copy the list",copy_list)