# # Set() - Множества
# # Это изменяемые неупорядочные, интерируемый неиндексируемый тип данных

# # множества хранят в себе только не изменяемые типы данных
# a = ['febw']
# print(hash(a))

# 1 -> set()
# a = set([1,2,3,4])
# print(a)

# a = set ({1:2, 3:4})
# print(a)

# 2 - {}
# set2 = {1, 2, 4}
# print(set2)

# set1 = {1,2,2,2,3}
# print(set1)

# set1 = {1,}
# print(type(set1))

# set1  = {1,0, True, False}
# print(set1)
# a = 0
# print(bool(a))
 
# методы SET

# add -> для добавления

# set1 = {1,2,3}
# # set1.add(a)
# # print(set1)
# # set1.add((1,2,3,4,5))
# # print(set1)

# # update - он может добавлять но не повторять имеющийся 
# # добавляет все интерируемые

# set1.update({3 :'1', 4:'5'})
# print (set1)
# set1.update('string, {1,2,3,4,5,6,7}')
# print(set1)
# set1.update({1,2,3,45,6})
 
#  Удаление строк set 
# clear -очищает все множества
# remove(element) - удаляет элемент
# если его ету выдает ошибку

# discard(element) - Если элемента нету ничего не происходить
# pop() - удаляет из set (FIFO) First In First Out

# set1 = {1,2,3,4,5}
# set1.remove(2)
# set1.clear()
# set1.discard(5)
# print(set1.pop())
# print(set1)

# difference - выводит отличие
# set1 = {1,2,3,4}
# set2 = {2,3,5,7}
# print(set1.difference(set2))
# print(set1 - set2)
# (set2.difference(set1))

# a = set1.symmetric_difference(set2)
# print(set1^set2)
# print(a)
# print.set1.symmetric_difference_update(set2)
# print(set1)

# print(set1.intersection(set2))
# print(set1 and set2)

# print(set1.union(set2))
# print(set1 | set2)

# set_1 = set(['White', 'Black', 'Red'])
# set_2 = set(['Red', 'Green'])
# print(set_1 ^ set_2)


# num = list(input())
# print(len(num) == len(set(num)))

# frozenset неизменяемое множество
# a = frozenset({1,2,3,4,5})
# a.add(7)
# print(a)                                                                                                            

# tuple - неизменяемыйб индексируемый, итерируемый,
# упорядоченный тип данных.
# index(element) - возвращает индекс этого элемента в кортеж 
#  литералы ()
# a = (True, 'a', 1,1,2,1)
# print(a, type(a))
# b = tuple()
# c = 1,2
# print(type(c))
# # count(elem) - возвращает число вхождений
# # этого элемента в кортеж
# print(a.count(True)) 
























































