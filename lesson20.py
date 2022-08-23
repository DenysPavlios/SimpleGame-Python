# t1 = (1, 2, 3,)
# l1 = [1, 2, 3]
# t1 = 1, 2, 3
# t1 = tuple((1, 2, 3))
# t1 = ()
# t1 = (1,)
# t1 = (1, 2, 3)

# print(t1.__sizeof__())
# print(l1.__sizeof__())

# t1 = tuple('hello')
# t2 = tuple(' world')
# t3 = t1 + t2
#
# print(t3)
# print(t3.count('l'))
#
# if 'l' in t3:
#     print(t3.index('l'))
# else:
#     print('No')
#
# for i in t3:
#     if i == ' ':
#         continue
#     print(f'"{i}"', end=' ')


# t1 = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t1, id(t1))
# t1[4][0] = 'new'
# t1[4].append('hello')
# print(t1, id(t1))

# t1 = (1, 2, 3,)
# x, y, z = t1
#
# print(x, y, z)

# x = 1
# y = 2
#
# print(x, y)
# x, y = y, x
# print(x, y)

"""
Дан список words. Составьте из него список слов-палиндромов. Попробуйте это сделать двумя способами: произвольное решение и решение в одну строчку кода.
Дан список my_str со строками, часть из которых являются палиндромами. Составьте новый список строк-палиндромов.
"""

# words = ['мадам', 'топот', 'test', 'madam', 'word']
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
# a = [elem for elem in words if elem == elem[::-1]]
# print(a)
#
# for i in words:
#     if i == i[::-1]:
#         print(i,end=' ')

polind = []
for word in my_str:
    word_r = word.replace(' ', '').lower()
    if word_r == word_r[::-1]:
        polind.append(word)
print(polind)












# print('-------------------')
#
# t1 = (1,2,3)
# t2 = 1,2,3
# t3 = tuple((1,2,3))
# t4 = (1,)
#
# print(t1.__sizeof__())
# print(t2)
# print(t3)
# print(t4)
#
# a = ('hello world')
# for i in a:
#     if i == ' ':
#         continue
#     print(i, end=' ')
# print('')
#
#
# print('-------')
# x = 1
# y = 2
#
# print(x,y)
#
# x,y = y,x
# print(x,y)
#

d = [1,4,5]

s = list(map(str,d))   # map берет и каждый элемент в D пеерводит в str и обернули в список
print(s)

