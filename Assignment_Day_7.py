'''Assignemnt : 1     Use the dictionary, port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}, 
and make a new dictionary in which keys become values and values become keys, as shown:
 Port2 = {“FTP":21, "SSH":22, “telnet":23,
"http": 80}'''



dict1 = {21:"ftp",22:"ssh",23:"telnet",80:"http"}
dict2 ={value:key for key,value in dict1.items()}
print("The output:",dict2)


'''Assignment 2 : 
Take a list of tuple as shown below.
[(1,2), (3,4), (5,6),(4,5)]
Make a new list which contains sum of number of tuples. 
For example 
Input 
[(1,2), (3,4), (5,6)]
Out put 
[3, 7, 11]'''

list1=[(1,2),(3,4),(5,6),(4,5)]
list2=[]
len1=len(list1)
for each in range(len1):
    a,b=list1[each]
    list2.append(a+b)
print(list2)


'''Assignment 3 :

Take a list as shown below 
[(1,2,3), [1,2], ['a','hit','less']]
The List contains tuple and lists. Make the elements of inner lists and tuples to outer list'''


list_1=[(1,2,3), [1,2], ['a','hit','less']]
list_2=[]

for each in list_1:
    for i in each:
        list_2.append(i)
print(list_2)











