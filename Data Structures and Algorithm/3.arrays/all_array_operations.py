from array import *
# 1. create an array and traverse
my_array = array('i', [1, 2, 3, 4, 5])
print('step 1')
for i in my_array:
    print(i)

# 2. access individual elements thru index
print('step 2')
my_array[3]

# 3. append any value to the array using append() method
my_array.append(6)
print('step  3')
print(my_array)

# 4. insert value in array using insert()
print('step 4')
my_array.insert(3, 11)
print(my_array)

# 5.extend python array using extend() method
print('step 5')
new_arr = array('i', [45, 22, 112])
my_array.extend(new_arr)
print(my_array)

# 6.add items from list into array using fromlist() method
print('step 6')
templist = [21, 22, 23]
my_array.fromlist(templist)
print(my_array)

# 7. remove any element using remove() method
print('step 7')
my_array.remove(3)
print(my_array)

# 8. remove last array element using pop() method
print('step 8')
my_array.pop()
print(my_array)

# 9. fetch any element thru its index using index() method
print('step 9')
print(my_array[4])

# 10. reverse a python array using reverse() method
print('step 10')
print(my_array.reverse())

# 11. get array buffer information using buffer_info() method
print('step 11')
print(my_array.buffer_info())

# 12. check for number to occurences of an element using count() method
print('step 12')
print(my_array.count(5))

# 13. convert array to string using tobytes() method
print('step 13')
strtemp = my_array.tobytes()
print(strtemp)
ints = array('i')
ints.frombytes(strtemp)
print(ints)

# 14. convert array t a python list with same elements using tolist() method
print('step 14')
print(my_array.tolist())

# 15.append a string to char array using fromstring() method
print('step 15')
# ints.frombytes(strtemp)

# 16.slice elements from an array
print('step 16')
print(my_array[1:4])
