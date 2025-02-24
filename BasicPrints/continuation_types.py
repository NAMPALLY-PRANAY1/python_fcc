'''
Implicit continuation:
    Python automatically allows code continuation using these symbols
    (),[],{}
'''

'''
explicit continuation in python:
    Backslashes are used for the seperation of 
    long statements into multiple lines 
'''

sentence = 'Hello World this is a very beautiful Flower in the Garden'\
            'It must be cherished I guess in 1-2 months mew flowers on the tree'\
           'will live'

print(sentence)

addition = 1+2+3+\
    4+5+6+\
    7+8+9\
    -12

print(addition)


result = (1+2+3+4
        +5+6+7+8)

print(result)

#[] is used for lists where collection goes on
mylist = [1,2,
        'Pranay','India',5.0,22323]
print(mylist)

#{}: is used for dicts or dictionary where mapping goes on
mydict = {'hi':'namaste',12:43,
          102:"Namaste",'Hyderabad':56.24}
print('')

print(mydict)
print(*mydict.items(),sep = '\n') 

'''
*pointer indicates that each value in the item to be operated here we use print 


mydict.items() returns:

dict_items([
    ('hi', 'namaste'),
    (12, 43),
    (102, 'Namaste'),
    ('Hyderabad', 56.24)
])

each and every values of the dict

'''