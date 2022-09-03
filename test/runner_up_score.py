# # import random
# import math
# # n = int(input())
# # arr = map(int, input().split())
# # array = list(arr)
# # max = 0
# # second_max = array[0]
# # for i in array:
# #     if max < i:
# #         max = i
# # for i in array:
# #     if second_max < i and i < max:
# #         second_max = i
# #
# # print(second_max)
# # # a = list(set(arr))
# # # a = sorted(a)
# # # print(a[-2])
# # list = []
# # min = 99999999999999999
# # second_min = 9999999999999999
# # for _ in range(int(input())):
# #     name = input()
# #     score = float(input())
# #     students = [name, score]
# #     list.append(students)
# # for i in range(0, len(list)):
# #     if min > list[i][1]:
# #         min = list[i][1]
# #     elif second_min > list[i][1] and list[i][1] > min:
# #         second_min = list[i][1]
# # print(second_min)
# # def binarysearch(arr, k):
# #     if k in arr:
# #         return arr.index(k)
# #     else:
# #         return -1
# # array = [1, 2, 3, 4, 5]
# # removed = []
# # list1 = []
# # binarysearch(array, 4)
# # def reverseInGroups(arr, K):
# #     for i in range(K):
# #         list1.append(arr[i])
# #         list1.reverse()
# #     for j in range(K, len(arr)):
# #         list1.append(arr[j])
# #     arr.clear()
# #     arr = list1
# #
# #
# #     print(arr)
# # reverseInGroups(array, 3)
# # print("-"*40)
# # print("VERSION: 1.0.1")
# # print("-"*40)
# # print("summer", "time", "holiday", sep="#")
# # price = 12
# # print('This costs', price)
# # pi = 3.1415926535
# # pi = round(pi, 2)
# # print(pi)
# # pi = 3.14
# # radius = 5
# # area = pi * radius ** 2
# # print(area)
# # p = 1000
# # r = .03
# # t = 5
# # area = p*(1+r)**t
# # print("The future value of the investment:", area)
# # a = 3
# # b = -4
# # c = 1
# # delta = b ** 2 - 4 * a * c
# # print("Delta:", delta)
# import math
#
# # n = 10
# # a = 10 + 4 * 1
# # l = 10 + 4 * n
# # sum = n / 2 * (a + l)
# # print("The sum of the first 10 elements in a sequence:", sum)
# # n = 6
# # a = 8 * (2 ** n - 1)
# # print("The sum of the first 6 elements of the sequence is:", a)
# # a = 1
# # b = 5
# # c = 4
# # sum = b/a
# # product = -c/a
# # print(sum)
# # print(product)
# # A = (2, 4), B = (-4, 6)
# # a1 = 2
# # b1 = 4
# # a2 = -4
# # b2 = 6
# # mid_x = (a1 + a2)/2
# # mid_y = (b1 + b2)/2
# # print(f"{(mid_x, mid_y)}")
# #  A = (3, 2), B = (- 1, -1)
# # a1 = 3
# # b1 = 2
# # a2 = -1
# # b2 = -1
# # distance = math.sqrt((a1-a2)**2 + (b1-b2)**2)
# # print(distance)
# # a = 1
# # b = 5
# # c = 4
# # delta = (b**2 - 4*a*c)**(1/2)
# # root1 = (-b + delta)/2*a
# # root2 = (-b - delta)/2*a
# # print(root1)
# # print(root2)
# # gm = (4*3*4.5*5)**(1/4)
# # a, b, c, d = 1, 1/2, 1/4, 1/8
# # r = c/b
# # sum = a*(1-r**4)/(1-r)
# # print(round(sum, 2))
# # a, b, c = 10, 11, 9
# # mean = (a+b+c)/3
# # dev = ((a-mean)**2 + (b-mean)**2 + (c-mean)**2)/3
# # deviation = dev ** (1/2)
# # print(deviation)
# # filename = 'view.jpg'
# # sliced = filename[-3:]
# # print(sliced)
# # string = 'PKV-89415-PLN'
# # first_three = string[:3]
# # last_three = string[-3:]
# # print(first_three,last_three)
# # string = '1 0 0 1 0 1'
# # s = slice(0,10,2)
# # print(string[s])
# # text = 'Python Course'
# # s = slice(12, 0, -1)
# # print(text[s])
# # var1 = ''
# # var2 = ' '
# # var3 = '\n'
# # print(type(var1), type(var2), type(var3))
# # var1 = None
# # var2 = False
# # var3 = 'True'
# # print(type(var1), type(var2), type(var3))
# # flag = False
# # print(isinstance(flag, bool))
# # text = 'python is a popular programming language.'
# # print(text[0].title() + text[1:])
# # print(text.capitalize())
# # text = 'python is a popular programming language.'
# # print(text.count("p"))
# # code1 = 'FVNISJND-XX-2020'
# # code2 = 'FVNISJND-XY-2019'
# # print(code1.endswith("2020"))
# # print(code2.endswith("2020"))
# # path1 = 'youtube.com/watch?v=5EhRztVxums'
# # path2 = 'google.com/search?q=car'
# # print(path1.startswith("youtube"))
# # print(path2.startswith("youtube"))
# path1 = (
#     "https://e-smartdata.teachable.com/p/"
#     "sciezka-data-scientist-machine-learning-engineer"
# )
# path2 = (
#     "https://e-smartdata.teachable.com/p/"
#     "sciezka-data-scientist-deep-learning-engineer"
# )
# path3 = (
#     "https://e-smartdata.teachable.com/p/"
#     "sciezka-bi-analyst-data-analyst"
# )
# # print(path1.find("scientist"))
# # print(path2.find("scientist"))
# # print(path3.find("scientist"))
# # code1 = 'FVNISJND-20'
# # code2 = 'FVNISJND20'
# # print(code1.isalnum())
# # print(code2.isalnum())
# # text = 'Google Colab'
# # print(text.lower())
# # text = '  Google Colab   '
# # print(text.strip(" "))
# # code = 'FVNISJND-XX'
# # print(code.replace("-", " "))
#
# # code1 = ""
# # for i in range(0, len(code)):
# #     if code[i] == "-":
# #         code1 += ""
# #     else:
# #         code1 += code[i]
# # print(code1)
# # text = '340-23-245-235'
# # print(text.replace("-", ""))
# # text = 'Open,High,Low,Close'
# # print(text.split(","))
# # text = """Python is a general-purpose language.
# # Python is popular."""
# # print(text.split(".\n"))
#
# # num = 34
# # print(str(num).zfill(6))
# # url = (
# #     "https://e-smartdata.teachable.com/p/"
# #     "sciezka-data-scientist-machine-learning-engineer"
# # )
# # name = url.split("/")
# # print(name[4].replace("-", " "))
# # subjects = {'mathematics', 'biology'}
# # subjects.add("english")
# # print(subjects)
# # text = 'Programming in python.'
# # text.lower()
# # t = text.replace(" ", "")
# # tt = t.replace(".", "")
# # print(tt)
# # dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
# # dji2 = ('HD.US', 'GS.US', 'NKE.US')
# # print(dji1 + dji2)
# # dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
# # dji2 = ('HD.US', 'GS.US', 'NKE.US')
# # print((dji1, dji2))
# # members = (('Kate', 23), ('Tom', 19))
# # a = ('John', 26)
# # members = (members[0], a, members[1])
# # print(members)
# # default = ('YES', 'NO', 'NO', 'YES', 'NO')
# # print(default.count("YES"))
# # names = ('Monica', 'Tom', 'John', 'Michael')
# # print(tuple(sorted(names)))
# info = (('Monica', 19), ('Tom', 21), ('John', 18))
# ascending = tuple(sorted(info))
# print(ascending)
# print(tuple(reversed(ascending)))
# stocks = (
#     ("Apple Inc", ("AAPL.US", 310)),
#     ("Microsoft Corp", ("MSFT.US", 184)),
# )
# print(stocks[0][1][0])
# cities = ['Los Angeles', 'New York', 'Chicago']
# cities.append('Houston')
# print(cities)
# idx = ['001', '002', '001', '003', '001']
# print(idx.count('001'))
# text = 'Python programming'
# text = text.lower()
# a = list(set(text))
# a.remove(" ")
# a.sort()
# print(a)
# filenames = ['view.jpg', 'bear.jpg', 'ball.png']
# filenames.insert(0, "phone.jpg")
# filenames.remove("ball.png")
# print(filenames)
# day1 = ['3984', '9042', '4829', '2380']
# day2 = ['4231', '5234', '1345', '2455']
# print(day1+day2)
# techs = ('python', 'java', 'sql', 'aws')
# print(tuple(sorted(techs)))
# hashtags = ['summer', 'time', 'vibes']
# print(f"{hashtags[0]}#{hashtags[1]}#{hashtags[2]}")

a = input()
b = list(a)
c = [int(item) for item in b]
print(a)
print(b)
print(c)






















