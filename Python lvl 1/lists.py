#\\\\\\\\\\\\\\\\\\\\ List in python are similar to arrays
print('------------ Lists Examples ------------')
mylist = ['a','b','c','d','e']
other_list = [1, 2.25, True, 'b',  'I am a Python Developer'] # we can put almost any data type in list
print(mylist)
print(other_list)

print('------------ Lists length ------------')
print(len(mylist))


#\\\\\\\\\\\\\ Indexing & Slicing
print('------------ Indexing & Slicing ------------')
mylist = ['a','b','c','d','e']

print(mylist[0]) #Indexing
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])

print(mylist[-1])
print(mylist[1:]) #Slicing
print(mylist[:3])
print(mylist[:])

# Reassigning
print("-------------- Reassigning --------------- ")

print("Before Reassignment")
print(mylist)

mylist[0]= "New item"
print("after Reassignment")
print(mylist)

print("---------- appending ------------")
list_two = ['x','y','z']
mylist.append(list_two)#this item will be appended
print(mylist)

print("----------- extending -----------")
mylist.extend(list_two)
print(mylist)

print("----------- pop , to remove something-----------")
item = mylist.pop()
print(mylist) #last item is popped out

print("----------- reverse -----------")
mylist.reverse()
print(mylist)

print("----------- sortable-----------")
mylist = [1, 4, 3, 6, 5, 2, 4]
mylist.sort()
print(mylist) #it will sort the values


# \\\\\\\\\\\\\\ Nested List
print("----------- Nested List -----------")

mylist = [1, 2, 3, ['x','y','z'] ]
print(mylist[3])
print(mylist[3][2]) # to print item from list within list

print("----------- List Comprehension -----------")
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix)
first_col = [row[0] for row in matrix] #first item at index [0] from every nested list is printed
print(first_col)