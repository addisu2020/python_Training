# intigers 
i=10
print(i)
ii = int(1.2)
print(ii)
# floating
f = 1.4
print(f) 
iif = i-f
#print(iif) 
s = 'my string'
ss = 'my other string'
print(s,ss) 
s = 'backslash \\'
print(s)
s = "Bob's cat and ALice's dog"
print(s)
x = 'My name is \n Addisu' # n indicates put the name on new line
print(x)
name = 'Addisu'
complete_name = 'My name is %s' % name
print(complete_name)


complete_name = 'My name is {}'. format (name)
print(complete_name)
complete_name = f'My name is {name}'
print(complete_name)
name = 'Addisu'
surname = 'Dagew'
age = '31'
Information= f'''My complete name is {name} {surname} and I am {age} years old'''
print(Information)

mybool = True
mybool2 = False
print(mybool,mybool2)

i = '1'
print(str(i))
s = 'False'
print(bool(s))


# lists 
L = [1,2,3,4,5,6]
print(type(L))
# print(L)
LL = [1, 'AA', 1.2, True]
print(LL)

print(L ==LL)
print(L != LL)
L1 = [1, 2, 3, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3]
print(L1)
s1 = set(L1)
print(s1)
print(type(s1))

#Lclean = list(s1)
#print(Lclean)
L1[0] = 'A'
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(L[0])
L1 = [1,2,3]
L2 = [4,5,6,7]
Lt = L1 + L2 
print(Lt)
Ltt = L1 * 4
print(Ltt)
L2[2] = 8
print(L2[2])
Lm = [L1, L2]
print(Lm)
del(Lm[0])
print(Lm)

#tuple 
t = (1, 2, 3)
#print(t)
#print(type(t))

#dictionaries 

d = {'name':'Addisu','age':'Addisu'}
print(d)
d['name'] = 'Addisu'
print(d['name']) 


#print(['name']) 

d = {'names': ['Addisu','Luis':'Assaye']}




































