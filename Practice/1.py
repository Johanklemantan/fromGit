# a = [1,2,3]
# b = [4,5,6]
# a,b = b,a
# print(a,b)

# print(isinstance(a, int)) # apakah a adalah integer ? --> False. A adalah list
# print(issubclass(class,subclass)) #apakah suatu subclass bagian dari suatu class ?
# x = 'Halo Dunia LainH'
# y = list(x)
# print(y)
# z = []
# for i,j in enumerate (x):
#     if j == 'a':
#         z.append(i)
# print(z)

# y.pop(y.index('a'))
# print(y)

# aa = ['Honda','Ferrari','Toyota']
# aa =([*'Honda','Ferrari','Toyota'])
# # print(aa.append(['Honde']))
# print(aa)


# b = [1,2,3,4,5]
# # c = *b
# # print(c)
# print(*b)
# print(type(b))

def power2(x):
    # print('dari dalam',x**2)
    # print(x**2)
    return x**2
# print('a',power2(4))
power2(4)