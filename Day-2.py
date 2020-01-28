# r = range(1,100,2)
# print(r)

# L = list(r)
# print(L)

 #d = {'a': [1,2,3,....50],'b': [1,2,3,....20]}. this doesnt recognized by python. it should be changed 
 #into the following form. ra and rb represents range of a and b. then do the set d.
# ra = list(range(1,50))
# rb = list(range(1,20))
# d = {'a': ra, 'b': rb}
#d = {'a': list(range(1,50)),'b':blist(range(1,20))}
#print(d)

# for k,v in d.items():
#     if k == 'a':
#         for i in v:
#             if i > 25:
#                 print(i)
#             else:
#                 print('no values')
#     if k=='b':
#         for i in v:
#             if i < 10:
#                 print(i)


# print(d['a'])

# L = []

# for i in d['a']:
#     if i > 25:
#         L.append(i)

# print(L)


# def my_function():
#     print("Hi python")

# my_function()

# def my_function2(s):
#     print(s)
# my_function2('Addisu')

# def my_function3(name,age = 31):
#     print(name, age)
# my_function3('Addisu')

def multiply(x, y):
    result = x*y
    print(result)
# multiply(10,35)

L = [10, 2, 3, 50]
# multiply(L[0], L[2])
def multiply2(*args):
    v = 1

    for i in args:
        v = v * i
        return v
    print(v)
# multiply2(1,30,90,4,3)
multiply2(L)
mynumber = multiply2(*L)
print(mynumber)

# Area Calculation example
def rect_area(Width, height):
    calculation = Width * height

    return calculation
my_area = rect_area(100,40)
print(my_area)

# Volume calculation

def shape_area(shape, width, height):
    if shape == 'rectangle':
        calculation = width * height
    if shape == 'triangle':
        calculation = width * height/2
    else:
        print('I do not know the shape')
    return calculation   
area = shape_area('triangle', 100,5)
# print(area)
area = shape_area('rectangle', 100,5)
print(area)
# fahrenheit = (celsius * 9/5) + 32


# def fahrenheit(celsius):
#     f = (celsius * 9/5) + 32
#     return f
# a = fahrenheit(100)

# define the following Lc
Lc = [100, 0, 100, 50]

# def fahrenheit2(*args):
#     Lf = []
#     for c in args:

#         calculation = (c*9/5)+32
#         Lf.append(calculation)
#     return Lf

# my_f = fahrenheit2(10,0,100, 33)
# print(my_f)
# my_f2 = fahrenheit2(*Lc)
# print(my_f2)




