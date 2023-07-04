'''
# Introduction to Python for Data Analysis 

print('hello world!')
print('Fundamentals of Python for Data Analysis')

# Python enumerate function

l1 = ['eat', 'sleep', 'repeat']
s1 = 'geek'

# Create enumerate objects 

obj1 = enumerate(l1)
obj2 = enumerate(s1)


# print("Return type:", type(obj1))
# print(type(obj1))
# print(type(obj2))

print(list(obj1))
print(list(enumerate(l1)))
print(list(enumerate(s1,2)))
print(list(enumerate(s1)))

'''
"""
l1 = ['eat', 'sleep', 'repeat']
s1 = "mystring"

obj1 = enumerate(l1)
obj2 = enumerate(s1)

for x in obj1:
    print(x)
    
for x in obj2:
    print(x)

print("Return type: ", type(obj1))
print(list(enumerate(l1)))
print(list(enumerate(s1, 1)))

"""
# printing the tuples in object directly

l1 = ['eat', 'sleep', 'repeat']

for ele in enumerate(l1):
    print(ele)

# New Series to print
for count, ele in enumerate(l1, 100):
    print(count, ele)
    
for count, ele in enumerate(l1):
    print(count)
    print(ele)
    
    
