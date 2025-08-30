str1= "I am a coder"

#endswith
print(str1.endswith("er")) #returns true if ends with er

#Capatalize
a = "abc"
print(a.capitalize())# Abc

#replace
str1 = "I am studying c++"
print(str1.replace("c++","python"))

#find - finding the occurence of first index 
str1 = "Cool dude aman"
print(str1.find("d"))
print(str1.find("aman"))

#count - the occurnces in the substr
str2 = "I am studying python from AMAN and from is used again."
print("Count of from",str2.count("from"))
print("Count of m",str2.count("m"))
