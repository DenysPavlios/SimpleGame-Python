# year = 1800
# while year <= 2019:
#     print(year)
#     year += 1
# else:
#     print('Done')


l = [1, 2, 3, 'hello', ['test', 10], 'world', True]
#
l2 = list('hello')
l3 = list((1, 2, 3))
#
l4 = [i for i in 'hello']
l5 = [i for i in 'hello world' if i != ' ' and i != 'e']
# l5 = [i for i in 'hello world' if i not in ['a', 'e', 'i', 'o', 'u', ' ']]
#
print(l, l2, l3, l4, l5, sep='\n')

l7 = list(range(1,3))
print(l7)
l8 = range(1,3)
print(l8)

# for i in range(1,3):
#     print(f'Vneshniy cikle,##{i}')
#     for j in range(1,3):
#         print(f'\tVnytrinniy cikle##{j}')
#
#
#
# for i in range(1,11):
#     for k in range(1,11):
#         print(f'{k} * {i} = {i*k}\t', end='')
#     print('')





l7 = list(range(1,10))
print(l7)



