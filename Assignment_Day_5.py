
'''Sort the given list in increasing order but all zeros must be at the end '''

list = [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
list.sort()
k=list.count(0);
print(list[k:]+list[:k])


'''Merge the given already sorted lists and sort the obtained list but without using sort function '''

list1 = [10,20,40,60,70,80]
list2 = [5,15,25,35,45,60]
list3 =list1+list2
SortedList=[]
for i in range(min(list3),max(list3)+1):
    if i in list3:
        SortedList.append(i)
print(SortedList)

