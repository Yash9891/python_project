
# Tuples are immutable in python
a=(10,23, 45)
# print(a)

# print(a.count(10)) #count the number of times 10 is present in tuple

# print(a[0])  #indexing does not work in dictionaries and sets

# print(a.index(23)) #gives the index of 23 in tuple

a[0]=100 #it will give error because tuple is immutable in python

print(a)