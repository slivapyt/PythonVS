# # N = int(input())


# # def get_sum(N):
# #     a = b = c = 1
# #     count = 3
# #     yield a
# #     yield b
# #     yield c
# #     while count < N:
# #         a = a + b + c
# #         count += 1
# #         yield a
# #         if count == N:
# #             break
# #         b = a + b + c
# #         yield b
# #         count += 1
# #         if count == N:
# #             break
# #         c = a + b + c
# #         yield c
# #         count += 1
# #         if count == N:
# #             break


# # add = get_sum(N)
# # for i in add:
# #     print(i, end=" ")

# N = int(input())


# def get_sum(N):
#     a = b = c = 1
#     for _ in range(N):
#         yield a
#         a, b, c = b, c, a + b + c


# print(*get_sum(N))


# import random
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"

# lon_pas = int(input())


# def get_ran_pass(lon_pas):
#     rand_pass_num = [random.choice(chars) for i in range(lon_pas)]
#     return rand_pass_num


# for i in get_ran_pass(lon_pas):
#     print(i, end=" ")


# import random
# from string import ascii_lowercase, ascii_uppercase
# # random.seed(1)

# len_pass = int(input())


# def get_rand_pass(len_pass):
#     chars = ascii_lowercase + ascii_uppercase
#     name = ""
#     for i in range(len_pass):
#         indx = random.randint(0, len(chars)-1)
#         name += chars[indx]

#     yield name + "@mail.ru"


# i = 0
# while i < 5:
#     print("".join(get_rand_pass(len_pass)))
#     i += 1


# def get_num():
#     num = 2
#     coin = 0
#     if not num % 2 == 0 and num == 2:
#         if not num % 3 == 0 and num == 3:
#             if not num % 5 == 0 and num == 5:
#                 num += 1
#                 yield num
#                 coin += 1
#                 if coin == 20:
#                     break
#     else:
#         num += 1


# def get_num():
#     coin = 0
#     num = 2
#     while coin <= 20:
#         if num % 2 != 0 or num == 5 or num == 3 or num == 2:
#             if num % 3 != 0 or num == 5 or num == 3 or num == 2:
#                 if num % 5 != 0 or num == 5 or num == 3 or num == 2:

#                     yield num
#                     num += 1
#                     coin += 1
#                 else:
#                     num += 1
#             else:
#                 num += 1
#         else:
#             num += 1


# for i in list(get_num()):
#     print(i, end=" ")
# print("\n2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71")
# # ('2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71')


# num = map(abs(int, input().split()))

# print(*num)

# for i in num:
#     print(abs(i),end=" ")

# import sys

# lst_in = list(map(str.strip, sys.stdin.readlines()))

# lst2D = [list(map(int, i.split())) for i in lst_in]

# s = input()
# s_lst = s.split()
# tp = [tuple(map(tuple, i)) for i in s_lst]


# tp = []
# sss = []
# s = "house=дом car=машина men=человек tree=дерево"


# s_lst = s.split()


# for i in s_lst:
#     tp = (tuple(i.split("=")))
#     sss.append(tp)

# print(tuple(sss))


# sss = []
# s = "house=дом car=машина men=человек tree=дерево"
# s_lst = s.split()


# tp = tuple(tuple(i.split("=")) for i in s_lst)
# print(tp)

# for i in s_lst:
#     tp = (tuple(i.split("=")))
#     sss.append(tp)
# print(tuple(sss))


# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# text = input().replace(" ", "-")
# # trans = [v for k, v in text.items]
# for i in text:
#     if i != "-":
#         text = text.replace(i, t[i])


# print(text)

# citys = input().split()
# # s = map(lambda x: citys[x] if len(x) > 5 in citys else "-")
# # print(s)

# s = map(lambda x: x if len(x) > 5 else "-", citys)
# print(*s)

# test_c = "Тула Ульяновск Хабаровск Владивосток Омск Уфа".split()
# # citys = input().split()
# fil = filter(lambda x: len(x) > 5, test_c)
# print(next(fil), next(fil), next(fil))


# lst_test = """зонт=1000
# палатка=10000
# спички=22
# котелок=543""".split()


# tp = tuple(tuple(i.split("=")) for i in lst_test)
# # fil = filter(lambda x: x[2], tp)

# print(tp)

# num_1 = input().split()
# num_2 = input().split()
# if num_2 > num_1:
#     num_1, num_2 = num_2, num_1

# print(num_1, num_2)
# num_1 = input().split()
# num_2 = input().split()
# if num_2 > num_1:
#     num_1, num_2 = num_2, num_1
# filt = filter(lambda x: x in num_2, num_1)
# print(*filt)


# num_1 = list(map(int, input().split()))
# num_2 = list(map(int, input().split()))
# if num_2 > num_1:
#     num_1, num_2 = num_2, num_1
# filt = filter(lambda x: x in num_2 and int(x) % 2 == 0, num_1)
# filt = sorted(list(filt))
# print(*filt)


# # mails = input().split()
# import string
# letters_and_digits = string.ascii_lowercase + string.digits
# symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890.@"

# mail_test = "abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com".split()
# # mails = input().split()
# for mail in mail_test:
#     if mail.issubset(symbols):
#         print(mail)
