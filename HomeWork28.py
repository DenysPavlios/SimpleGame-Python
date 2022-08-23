x = ["even",4,"even",7,"even",55,"even",6,"even",10,"odd",3,"even"]

c = 'odd'
index = x.index(c)
def f(x):
    if 'odd' in x and index in x:
        return True

print(f(x))


x1 = ["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"] # False
c = 'odd'
index = x.index(c)
def f(x1):
    if 'odd' in x1 and index in x1:
        print(True)
    else:
        print(False)
f(x1)

x2 = ["even",10,"odd",2,"even"]
index = x2.index('odd')

def f(x2):
    if 'odd' in x2 and index in x2:
        print(True)
    else:
        print(False)
f(x2)


#--------------------------------------
# def find_sum(n):
#     if list(range(n)) == 3 and list(range(n)) == 5:
#         return list(range(n))
#
# print(find_sum(1,11))


"""
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
"""
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"]

def get_names(names):
    return [i for i in names if len(i) == 4]
print(get_names(names))














