# list comprehensions - генераторы списков

# list comprehensions - упрощенный подход к созданию списков, который задействует 
# в себе цикл for, также конструкцию
# if для определения того, что в итоге попадет в наш список

# list -> 0 -200 -> num % 2 == 0

# ls = []
# for x in range(0, 201):
#     if x % 2 == 0:
#         ls.append(x)

# ls = [x for x in range(0, 201) if x % 2 == 0]
# print(ls)

# list: 0 - 300 -> num % 2 == 0, num % 3 == 0

# ls = []
# for x in range(0, 300):
#     if x % 2 and x % 3 == 0:
#         ls.append(x)
# print(ls)

# ls = [i for i in range(0, 301) if i % 2 == 0 and i % 3 == 0]
# print(ls)

# list: 0 - 100 -> x % 2 == 0 : x ** 2, x % 3 == 0: x ** 3

# ls = []
# for x in range(0, 101):
#     if x % 2 == 0:
#         ls.append(x ** 2)
#     elif x % 3 == 0:
#         ls.append(x ** 3)
# print(ls)
# print(5 if input() == 'yes' else 7)

# ls = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(0, 101) if x % 2 == 0 or x % 3 ==0]
# print(ls)

# -----------------------------------------------------

# newlist = [expression for item in iterable <if condition == True>]

# ls = [str(i * 2) for i in range(0, 11)]
# print(ls)

# res = []
# for x in res:
#     for item in res:
#         res.append(item)

# print(res)

# ls = [[1,2,3], [4,5,6], [7,8,9]]
# res = [item for x in ls for item in x]
# print(res)

# ------------------------------------------------------

# from datetime import datetime

# start = datetime.now() # 19.55.43
# ls = [x for x in range(0, 100_000_000)]
# # ls = []
# # for x in range(0, 1_000_000):
# #     ls.append(x)
# finish = datetime.now() # 19.57.46
# print(finish - start)

# --------------------------------------------------------

# set compehensions
# set_ = {x for x in range(1, 100)}
# print(set_, type(set_))
# set1 = {1, 'b',2,3,4, 'a', True}
# print(set1)

# ---------------------------------------------------------
# dict comprehensions
# dict_ = {x: x ** 2 for x in range(0, 16)}
# print(dict_)

# names = ['John', 'Tirion', 'Eygan', 'Sansa', 'Ramsi']
# dict_ = {x: len(x) for x in names}
# print(dict_)

# ---------------------------------------------------------

dict1 = {
    'Soke': {'history': 99, 'Physics': 95, 'math': 95},
    'Omoke': {'history': 84, 'Physics': 68, 'math': 86},
    'John':  {'history': 100, 'Physics': 90, 'math': 87},
}
# res = {'soke': 'history', 'omoke': 'math', 'john': 'history'}


# for student in dict1:                                  1 способ
#     print(f"Highest scores for {student}:")
#     for subject, score in dict1[student].items():
#         if score == max(dict1[student].values()):
#             print(f"{subject}: {score}")

# res = {}
# for key, value in dict1.items():
#     for inner_key, inner_value in value.items():         2 способ
#         if max(value.values()) == inner_value:
#             res[key] = inner_key
# print(dict1)
# print(res)

# res = {key: inner_key for key, value in dict1.items()                           #3 способ
#         for inner_key, inner_value in value.items()
#         if inner_value == max(value.values())}
# print(res)



















