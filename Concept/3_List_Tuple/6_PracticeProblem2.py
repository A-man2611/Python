# WAP to check if a list contains a palindrome of elements.
list = ["1","2","3","2","1"]
list_cp = list.copy()
list_cp.reverse()
if(list == list_cp):
    print("palindrome")
else:
    print("Not Palindrome")


    
