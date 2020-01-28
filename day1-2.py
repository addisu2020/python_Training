# s = 'John'
# #print(dir(s))
# s = s.upper()

# print(s)

# #print(help(s.q))
# #help(s.upper)


# L = [1,2,3,4,5]
# print(dir(L))
#print(help(L.append))
# L.append(100)
# print(L)
# L = [2,1,4,6,7,12,345,55]
# L.sort(reverse=True)
# #print(L)

# d = {'Italy': 'Rome','Germany':'Berlin', 'Spain':'Madrid'}
# print(d)
# #print(dir(d))

# print(help(d.keys))
# print(d.keys())
# print(d.values())
# #print(d.items())
# #loops
# L = [1,2,3,4,5,6,7,8,9]
# for i in L:
#     print(i+10)
# L1 = [10,20,30,40]
# L2 = ['A','B','C','D']

# Lt = [L1,L2]
# print(Lt)


# L1 = [10,20,30,40,50,60]

# #if len(L1) < 5:
#  #   print('I am a long list')
# #elif 


# d = {'names': ['John','Maria','Anna'], 'age':[21, 25, 13]}
# for k, v in d.items():
#     if k == 'names':
#         for i in v: 
#             print(i)


# #    print(k, v)
# i = 10
# O = 0
# try:
#     result = i/O
# except ZeroDivisionError as e:
#     print('I cannot divide by 0',e)
# L1 = [1,2,3]
# print(L1)

# food ='spam'
# if food =='spam':
#     print('Ummmm, my favorite!')
#     print('I feel like saying it 100 times...')
#     print(100 * (food + '!'))
#     print(3 * 'its fantastic!')

# # if BOOLEAN EXPRESSION:
# # STATEMENTS_1    # executed if condition evaluates to True
# # else:
# #    STATEMENTS_2   # executed if condition evaluates to False
# if food == 'spam':
#     print('Ummmm, my favorite!')
# else:
#     print("No, I won't have it. I want spam")

#  # chained conditional. each condition is checked in order. if the first flase, the nextis checked, and so on. if one of them is true,
#  # the next corresponding branch excecutes, and the statement ends. even if more than one condition is true, only the first true branch 
#  # executes.      
# choice = 'a'
# if choice == 'a':
#     print("You chose 'a'.")
# elif choice == 'b':
#     print("You chose 'b'.")
# elif choice == 'c':
#     print("You chose 'c'.")
# else:
#     print("Invalid Choice.")

# # Netsed conditionals
# x = 9
# if 0 < x:
#     if x < 10:
#         print("x is a positive single digit.")
# if 0 < x and x < 10:
#     print("x is a positive single digit.")
# if 0 < x <10:
#     print("x is a positive single digit.")


# Iteration: repeated ececution of a set of statements

# bruce = 5
# print(bruce)
# bruce = 7
# print(bruce)

# n = 5
# n = 3 * n+1
# print(n)
# n = n*n+1
# print(n)
# # The for Loop. 
# for friend in ['Margot', 'Kathryn', 'Prisila']:
#     invitation = "Hi" + friend + ". please come to my party on Saturday !"
#     print(invitation)

# for i in range(5):
#     print('i is now:', i)

# # Tables: using the character ('\t') makes the output align nicely
# for x in range(13):
#     print(x,'\t', 2**x)

# # The while statement
# name = 'Harrison'
# guess = input("So I'm thinking of person's name. Try to guess it:")
# pos = 0

# while guess != name and pos < len(name):
#     print("Nope, that's not it ! Hint: Letter", end='')
#     print(pos + 1, "name",[pos] + "-", end='')
#     guess = input("Guess again:")
#     pos = pos + 1
# if pos == len(name) and name != guess:
#     print("Too bad, you couldn't get it. the name was", name +"-")
# else:
#     print("\nGreat, you got it in", pos + 1, "guesses!")

# # Another while example: Guessing game

# import random
# number = random.randrange(1, 1000)
# guesses = 0
# guess = int(input("Guess my number between 1 and 1000:"))
# while guess != number:
#     guesses += 1
#     if guess > number:
#         print(guess, "is to high.")
#     elif guess > number:
#         print(guess, "is too low.")
#     guess = int(input("Guess again:"))
#     print("\n\nGreat, you got it in", guesses, "guesses!")    

# # The Break Statement: is used to immediately leave the body of its loop.
# for i in [12, 16, 17, 24, 29]:
#     if i % 2 == 1:
#         break
#     print(i)
# print("done")

# for i in [12, 16, 17, 24, 29]:
#     if i % 2 == 1:
#         continue
#     print(i)
# #print("done")

# sentence = input('Please enter a sentence:')
# no_spaces = ''

# for letter in sentence:
#     if letter != '':
#         no_spaces += letter
# print("You sentence with spaces removed:")
# print(no_spaces)





class Employee:
    def __init__(self, name, paycheck):
        self.name = name
        self.paycheck = paycheck

    def raise__paycheck(self,number):
        self.paycheck = self.paycheck+(self.paycheck*number)

mario = Employee('Mario', 1000)
print(mario.name)
print(mario.paycheck)

mario.raise__paycheck(0.9)
print(mario.paycheck)











   



    




















    



















