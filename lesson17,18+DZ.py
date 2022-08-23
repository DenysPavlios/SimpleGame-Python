# x = 10
# print(x, id(x))
# x = 20
# print(x, id(x))

# s = 'hello'
# print(s, id(s))
# s += ' world'
# print(s, id(s))

# l = [1, 2, 3]
# print(l, id(l))
# l.append(5)
# print(l, id(l))

# x = 10
# y = x
#
# print(x, id(x))
# print(y, id(y))
#
# x = 15
# print(x, id(x))
# print(y, id(y))

# l1 = [1, 2, 3]
# l2 = l1
# l2 = l1.copy()
# l2 = l1[:]
#
# print(l1, id(l1))
# print(l2, id(l2))
#
# l1.append((5))
# print(l1, id(l1))
# print(l2, id(l2))

# x = 10
# print(x)
# del x
# print(x)

# x = 10
# print(x, id(x))
#
# x = 20
# print(x, id(x))

# x = 10
# print(x)
# del x
# print(x)
#

x = [1,2,3]
s = [i * 2 for i in x]
print(s)


for i in range(len(x)):
        x[i] *= 2
print(x)
print('------------------')

# ---------------------------
import math
#
z = [1,2,3]
for i in range(len(z)):
         z[i]**= 2
# print(z)
print(sum(z))
print('------------------')

k = [1,2,3]
xx = 0
for i in k:
    xx+= i**2
print(xx)


print('------------------')

time = 3 * 0.5
print(math.floor(time))
time1 = 6.7 * 0.5
print(math.floor(time1))
time2 = 11.8 * 0.5
print(math.floor(time2))
print('------------------')

s = 'Hello world'
if ' ' in s:
    print(s.upper())
elif ' ' not in s:
    print(s.lower())
else:
    pass
print('--------11111111')



# time = 3 * 0.5
# print(math.floor(time))
# time1 = 6.7 * 0.5
# print(math.floor(time1))
# time2 = 11.8 * 0.5
# print(math.floor(time2))

def time(a,b):
    return math.floor(a * b)

print(time(3,0.5))
print(time(6,0.5))
print(time(11.8,0.5))





