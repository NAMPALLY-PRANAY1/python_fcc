print('Local Variables:\n')
#Local Variable
def f():
    a = 'I am Local'
    print(a)

f()
#print(a) # NameError: name 'a' is not defined

#===============================================================================================

print('')
print('')
print('Global Variable:')
print('')
print('')
#Global Variable
b = 'I am Global' #variables assigned outside of fn is a global variable
def f():
    b = 'I am Local'
    print(b)
f() # I am Local from fn exec() pov
print(b) #I am global from global pov

#===============================================================================================

print('')
c = 'Global' #variables assigned outside of fn is a global variable
def f():
    global c 
    '''defining that b variable is a gloabl variable inside the function 
    so that changes made to the variable inside the function
    will change the values in the variable globally'''
    
    c = 'Modified Global'
    print(c)

print(c) #global from global pov before fn call
f() # Modified Global from fn exec() pov
print(c) #global from modified global variable after fn changes pov
