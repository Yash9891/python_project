#set is collection of unique elements
# s=set()
# print(type(s))

# s={23,45,67,89,23,45} #it will give set because {} is used for set in python
# print(type(s)) 

# print(s) #it will print the set without duplicates


#Using sets in list   
# list=[45,56,78,89,78,89]
# s=set(list)
# print(s)

# nums={1,2,3,5,5,6,6,90,1}#it will print the set without duplicates
# print(nums)

# s.add(900)
# print(s) #it will add 900 to the set

# s.discard(4775) #it will remove 45 from the set
# # s.remove(4545) #it will remove 45 from the set
# print(s)

#how to find an element in set
# find=456 in s
# print(find) #it will return True if 45 is present in set otherwise False


#Set operations
s1={1,2,3,4,5,8,9}
s2={4,5,6,7,8}

# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2)) #it will give the difference of s1 and s2

c1={1,2,8,9}
# print(c1.issubset(s1)) #it will return True if c1 is subset of s1 otherwise False

print(s1.issuperset(c1)) #it will return True if s1 is superset of c1 otherwise False







