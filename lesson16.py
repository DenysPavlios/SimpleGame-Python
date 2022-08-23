# list.append(x) - Добавляет элемент в конец списка
# list.extend(L) - Расширяет список list, добавляя в конец все элементы списка L
# list.insert(i, x) - Вставляет на i-ый элемент значение x
# list.remove(x) - Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
# list.pop([i]) - Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
# list.index(x, [start [, end]]) - Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
# list.count(x) - Возвращает количество элементов со значением x
# list.sort([key=функция], [reverse=False]) - Сортирует список на основе функции
# list.reverse() - Разворачивает список
# list.copy() - Возвращает копию списка
# list.clear() - Очищает список

#
# l = [1, 2, 3, 'hello', ['test', 10], 'world', True]
# names = ['Ivanov', 'Petrov', 'Sidorov']

# print(l[4][0])
# l[2] = 'world'
# l[:2] = [10, 15]

# l.append('new')
# l.extend([5, 7])
# l2 = ['hi', 19]
# l += l2
# l.insert(1, 'test')
# # l.remove('world')
# # el = l.pop(1)
# # l.sort()
# l3 = ['hello', 'hi', 'David', 'world', 'test']
# # l3.sort()
# # l3 = sorted(l3)
# print(l, l.count('test'), l3, sep='\n')
# print('h' > 'a')
print('--------------------------------------')


l = [1, 2, 3, 'hello', 'test', ['ddd',333, 444],'world','test', True]
l2 = [2, 1, 3,5,0,4,9,6]
# print(len(l))
# print(l[4][0])
# l.append('NEW')
# l.extend([5,7,'8',4,568,75])
# l2 = ['1', 'rt']
# l += l2
# l.insert(0,'YYY')
# el = l.pop(0)
# l2.sort(reverse=True)
# print(l2)


l2.clear()
print(l2)

# list.copy()
# list.clear()















