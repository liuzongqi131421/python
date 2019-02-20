# def printInfo():
#     print('----------------------')
#     print('          生命苦短，我用Python')
#     print('----------------------')
# printInfo()
# printInfo()

# def num_add(a,b):
#     c=a*b
#     print(c)
# num_add(3,5)
# num_add(4,6)

# def num_add(a,b):
#     c=a+b
#     return c
# print(num_add(3,5))

# import math
# # a=math.sqrt(3)
# # print(a)
# print(math.sqrt(16))

f=open('tst.txt','w')
f.write("asdasda")
f=open('tst.txt','r')
str1=f.read(1)
print(str1)
f=open('tst.txt','a')
f.write('asdasdfdsf')
f.close()