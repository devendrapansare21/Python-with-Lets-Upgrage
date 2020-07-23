'''Program to find number of 'we' in given string and their positions in string '''


str1="what we think we become ; we are Python pragrammers"
print("Total number of 'we' in given string are ", str1.count("we"))
print("position of first 'we'--> ",str1.find("we"))
print("position of last 'we'--> ",str1.rfind("we"))




'''Program to check whether the given string is in lower case or upper case'''
str1 = input("Enter the string --->")
while str1.isalpha()!=True:
    str1=input("Given string is not proper. Please enter again--->")
if str1.islower()==True:
    print("Given string is in Lower Case")  
elif str1.isupper()==True:
    print("Given string is in Upper Case")