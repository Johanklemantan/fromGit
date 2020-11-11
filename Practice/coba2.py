# def sum_double(a, b):
#   if a!=b:
#     return a+b
#   elif a==b:
#     return(a+b)*2
    

# a = 'hello'
# print(a.index('el'))

# c = a.replace('e','')
# print(c)

# def a(str,n):
#   b = str[n]
#   c = str.replace(b,'')
#   return c
# a('kitten',2)

# a = 'hello'
# b = a[1:-1] #ell --> huruf ke 2 awal sampe ke 2 terakhir
# print(b)
# c = a[-1:] #o --> huruf terakhir
# print(c)
# d = a[:1] #h --> huruf pertama
# print(d)
# # d = a.replace(c,b),(b,c)
# # print(d)

# def without_end(str):
#   str = str.replace(str[0],'')
#   str = str.replace(str[-1],'')
#   return str
# print(without_end('woohoo'))

# a='abcdefgh'
# d = a[::]
# print(f'd adalah {d}')
# e = a[::-1]
# print(f'e adalah {e}')
# b=(a.replace(a[0],''))
# c=(b.replace(a[-1],''))
# print(a[1:-1])
# print(a)
# print(b)
# print(c)
# for i in range(1,7):
#   print(i)
#   i+=1

# def a(name, age):
#   print(name,age)
# a('johan',25)

# def showEmployee(name,salary=9000):
#   print(f'Employee {name} salary is:{salary}')
# showEmployee('Ben', 10000000)
# showEmployee('Asu')

# d = 5
# print(factorial(d))

# def rec_factorial(n): # n = 5 // n = 4 // n = 3 // n = 2 // n = 1
#     if n == 0: # 5 == 0 False // 4 == 0 False // 3 == 0 False // 2 == 0 False // 1 == 0 False 
#         return 1
#     elif n == 1: # 5 == 1 False // 4 == 1 False // 3 == 1 False // 2 == 1 False // 1 == 1 True
#         return 1
#     elif n < 0: # 5 < 0 False // 4 < 0 False // 3 < 0 False // 2 < 0 False
#         return 'must be positive digit'
#     else:
#         return n*rec_factorial(n-1) # 5 * 24 = 120
# print(rec_factorial(d))

#https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php
#1.
# for i in range (1500,2700):
#   if i % 7 ==0 and i % 5 ==0 :
#     print(i)
#   else:
#     continue

#2.
# converter = input('Enter (C/F): ')
# def a(number):
#   if converter == 'C':
#     result = ((number*(9/5))+32)
#     print(f'{number} Celcius is {result} in Farenheit')
#   elif converter =='F':
#     result = ((number-32)*(5/9))
#     print(f'{number} Farenheit is {result} in Celcius')
#   else:
#     print('wrong input sir.')
# a(45)

#3.
# import random
# secret_number = random.randint(1,10)
# for i in range(1,10):
#   a = int(input('Enter the right number: '))
#   if a==secret_number:
#     print('Well guessed!')
#     break
#   else :
#     a
#   i +=1

#4.
# for i in range(1,6):
#     for j in range(0,i):
#       print(' * ',end= f'{i}')
#     print('')
# for k in range(1,5):
#     for l in range(0,5-k):
#       print(' * ',end= f'{k}')
#     print('')

# for i in range(1,6):
#     for j in range(0,i):
#       print(' * ',end= '')
#     print('')
# for k in range(1,5):
#     for l in range(0,5-k):
#       print(' * ',end= '')
#     print('')

# for i in range(0,10):
#   for j in range(0,10-i):
#     print(' ',end = '')
#   for k in range(0,2*i+1):
#     print('*',end = '')
#   print('')

# x = [6000, 34, 203, 3, 746, 200, 984, 198, 764, 9, 1]
# def bubbleSort(list) :
#   for i in range(len(list), 0, -1) :
#     for j in range(0,i-1) :
#       if (list[j] > list[j + 1]) :
#         temp = list[j]
#         list[j] = list[j + 1]
#         list[j + 1] = temp
#   return list
# print(bubbleSort(x))



# x = [6000, 34, 203, 3, 746, 200, 984, 198, 764, 9, 1]
# def sort(x):
#   for i in range(len(x)-1,0,-1):
#     for j in range(i): 
#       if x[j]>x[j+1]:
#         temp = x[j]
#         x[j] = x[j+1]
#         x[j+1] = temp

# sort(x)
# print(x)

# #3
from random import randint
a = randint(1,10)
def tebak():
    
    # a = randint(1,10)
    guess = int(input('masukkin nomer : '))
    if guess == a:
        print('well guessed')
    else:
        tebak()
tebak()