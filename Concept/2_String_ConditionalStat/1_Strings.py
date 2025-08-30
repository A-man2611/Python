# Escape Sequence 
# new line = \n 

str1 = "Hello! \n My name is AMAN"
print(str1)

#Concatanation
str1 = "Aman"
str2 = "Upadhyay"
final = str1+ " " +str2 #AmanUpadhyay

#length of string
print("Lenth of string 1:",len(str1))
print("Lenth of string 2:",len(str2))
print("Lenth of final string:",len(final)) #13 because of 1 extra space 

#indexing
str = "Aman Upadhyay"
print(str[0])

#str[0] = 'B' 
# # X NOT ALLOWED - 'str' object does not support item assignment

#Slicing
#Syntax : str[strt_indx : endn_indx] 
# NOTE: Here ending index is not included
str = "KALUA KALIA"
print(str[2:5])
print(str[:6]) #[0:6]
print(str[6:]) #[6:len(str)]

# --->Negative Index
new_str = "APPLE"
# -5 -4 -3 -2 -1
# A  P  P  L  E
# 0  1  2  3  4
print("Negative Index:",new_str[-3:-1])