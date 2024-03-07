import requests

url = "https://jsonkeeper.com/b/84OZ"
r = requests.get(url)


# class Student:


#     def __init__(self, name: str, course: int):
#         self.name = name
#         self.course = course


# student_1 = Student("Алиса", 3)
# student_2 = Student("Маргарита", 2)


# # Не удаляйте этот код, он нужен для проверки

# print(student_1.name, student_1.course)
# print(student_2.name, student_2.course)

# class Album:
#     def __init__(self, artist: str, title: str, tracks: list):
#         self.artist = artist
#         self.title = title
#         self.tracks = tracks


# album_1 = Album("Queen", "Killer Queen", ["Brighton rock",
#                 "Killer Queen", "Tenement Funster"])

# album_2 = Album("Metallica", "Black Album", ["Enter Sandman",
#                 "Sad But True", "Holier Than Thou"])


# print(album_1.artist, album_1.title, len(album_1.tracks), "треков")
# print(album_2.artist, album_2.title, len(album_2.tracks), "треков")


# class Bottle:
#     def __init__(self, color: str, contains: float):
#         self.color = color
#         self.contains = contains
#         contains = 0.0

#     def get_content(self):
#         return self.contains

#     def fill(self, volume):
#         self.contains += volume


# bottle_1 = Bottle("Красная", 0.0)
# bottle_2 = Bottle("Синяя", 0.0)


# print(bottle_1.color, bottle_1.get_content())
# bottle_1.fill(100)
# print(bottle_1.color, bottle_1.get_content())

# print(bottle_2.color, bottle_2.get_content())
# bottle_2.fill(500)
# print(bottle_2.color, bottle_2.get_content())


# class TodoList:
#     def __init__(self):
#         self.tasks = []


#     def add_task(self, name_task: list):
#         self.tasks.append(name_task)


# todo_list = TodoList()
# todo_list.add_task("Выключить свет")
# todo_list.add_task("Поменять лампочку")
# todo_list.add_task("Включить свет")

# # Не удаляйте этот код, он нужен для проверки

# print(" ".join(todo_list.tasks))

# class Player:

#     def __init__(self, name):
#         self.name = name
#         self.score = 0

#     def get_score(self):
#         return self.score

#     def set_score(self, score):
#         self.score = score


# player_1 = Player("Алиса")


# # Не удаляйте этот код, он нужен для проверки

# print(player_1.name, player_1.get_score())
# player_1.set_score(200)
# print(player_1.name, player_1.get_score())
# player_1.set_score(500)
# print(player_1.name, player_1.get_score())


# class Number:

#     def __init__(self, value):
#         self.value = value

#     def get(self):
#         return self.value

#     def add(self, n):
#         self.value += n

#     def subtract(self, n):
#         self.value -= n
# # Пример использования, не влияет ни на что, можно удалить.


# x = Number(7)
# x.add(3)
# x.subtract(10)
# x.get()

# # Не удаляйте этот код, он нужен для проверки

# n = Number(7)
# print(n.get())
# n.add(3)
# print(n.get())
# n.subtract(5)
# print(n.get())


# import math


# class Circle:

#     def __init__(self, radius):
#         self.radius = radius

#     def get_radius(self):
#         return self.radius

#     def get_diameter(self):
#         return self.radius*2

#     def get_perimeter(self):
#         return 2*self.radius * math.pi

# # Не удаляйте этот код, он нужен для проверки


# circle_1 = Circle(7)
# print("радиус", circle_1.get_radius())
# print("диаметр", circle_1.get_diameter())
# print("периметр", round(circle_1.get_perimeter(), 1))


# class Square:
#     def __init__(self, length, color="white"):
#         self.length = length
#         self.color = color

#     def set_side(self, length):
#         self.length = length

#     def set_color(self, color):
#         self.color = color

#     def get_side(self):
#         side_length = self.length
#         return side_length

#     def get_color(self):
#         return self.color

#     def get_perimeter(self):
#         return self.length*4


# # # Не удаляйте этот код, он нужен для проверки


# # square_1 = Square(2)
# # print(square_1.get_side())
# # print(square_1.get_perimeter())
# # print(square_1.get_color())
# # print("—-")
# # square_1.set_side(3)
# # # square_1.set_color("red")
# # # print(square_1.get_side())
# # # print(square_1.get_perimeter())
# # # print(square_1.get_color())
# # # print("—-")
# # # square_1 = Square(1, "black")
# # # print(square_1.get_side())
# # # print(square_1.get_perimeter())
# # # print(square_1.get_color())


# # class Room:

# #     def __init__(self, number, is_free):
# #         self.number = number
# #         self.is_free = is_free


# # def get_free_rooms(rooms):
# #     free_rooms = []
# #     for room in rooms:
# #         if room.is_free:
# #             free_rooms.append(room)
# #         return free_rooms


# # rooms = [Room(14, True), Room(15, False), Room(16, True)]
# # rooms_free = get_free_rooms(rooms)

# # # Не удаляйте этот код, он нужен для проверки

# # [print(r.number) for r in rooms_free]


# class Bottle:
#     def __init__(self, color):
#         self.color = color
#         self.contains = 0.0

#     def get_content(self):
#         return self.contains

#     def fill(self, volume):
#         self.contains += volume


# bottle_1 = Bottle("Красная")
# bottle_2 = Bottle("Синяя")


# # Не удаляйте этот код, он нужен для проверки

# print(bottle_1.color, bottle_1.get_content())
# bottle_1.fill(100)
# print(bottle_1.color, bottle_1.get_content())

# print(bottle_2.color, bottle_2.get_content())
# bottle_2.fill(500)
# print(bottle_2.color, bottle_2.get_content())


# class TodoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, name_task):
#         self.tasks.append(name_task)


# todo_list = TodoList()
# todo_list.add_task("Выключить свет")
# todo_list.add_task("Поменять лампочку")
# todo_list.add_task("Включить свет")

# # Не удаляйте этот код, он нужен для проверки

# print(" ".join(todo_list.tasks))


# class Number:

#     def __init__(self, value):
#         self.value = value

#     def get(self):
#         return self.value

#     def add(self, summ):
#         self.value += summ

#     def subtract(self, minus):
#         self.value -= minus
# # Пример использования, не влияет ни на что, можно удалить.


# x = Number(7)
# x.add(3)
# x.subtract(10)
# x.get()

# # Не удаляйте этот код, он нужен для проверки

# n = Number(7)
# # print(n.get())
# # n.add(3)
# # print(n.get())
# # n.subtract(5)
# # print(n.get())


# import math


# class Circle:

#     def __init__(self, radius):
#         self.radius = radius

#     def get_radius(self):
#         return self.radius

# #     def get_diameter(self):
# #         return self.radius*2

# #     def get_perimeter(self):
# #         return 2*self.radius*math.pi

# # # Не удаляйте этот код, он нужен для проверки


# # circle_1 = Circle(7)
# # print("радиус", circle_1.get_radius())
# # print("диаметр", circle_1.get_diameter())
# # print("периметр", round(circle_1.get_perimeter(), 1))


# # class Square:

# #     def __init__(self, side_length, color="white"):
# #         self.side_length = side_length
# #         self.color = color

# #     def set_side(self, side_length):
# #         self.side_length = side_length

# #     def set_color(self, color):
# #         self.color = color

# #     def get_side(self):
# #         return self.side_length

# #     def get_color(self):
# #         return self.color

# #     def get_perimeter(self):
# #         return self.side_length*4


# # # Не удаляйте этот код, он нужен для проверки
# # square_1 = Square(2)
# # print(square_1.get_side())
# # print(square_1.get_perimeter())
# # print(square_1.get_color())
# # print("—-")
# # square_1.set_side(3)
# # square_1.set_color("red")
# # print(square_1.get_side())
# # print(square_1.get_perimeter())
# # print(square_1.get_color())
# # print("—-")
# # square_1 = Square(1, "black")
# # print(square_1.get_side())
# # print(square_1.get_perimeter())
# # print(square_1.get_color())


# class Room:

#     def __init__(self, number, is_free):
#         self.number = number
# #         self.is_free = is_free


# # def get_free_rooms(rooms):
# #     free_rooms = []
# #     for room in rooms:
# #         if room.is_free:
# #             free_rooms.append(room.number)

# #     return free_rooms


# # rooms = [Room(14, True), Room(15, False), Room(16, True)]
# # rooms_free = get_free_rooms(rooms)

# # # Не удаляйте этот код, он нужен для проверки

# # for room in rooms_free:
# #     print(room)
# # # [print(r.number) for r in rooms_free]


# # class Character():

# #     def move(self, direction, distance):

# #         directions_list = {"north": "на север", "south": "на юг",
# #                            "west": "на запад", "east": "на восток"}
# #         if direction not in directions_list.keys():
# #             print(self.name, "движется непонятно куда")
# #         else:
# #             print(self.name, "движется", distance,
# #                   "метров", directions_list[direction])


# # class Hero(Character):

# #     def __init__(self, name):
# #         self.name = name


# # class Enemy(Character):

# #     def __init__(self, name):
# #         self.name = name


# # pythomir = Hero("Питомир")
# # bugoonya = Enemy("Багуня")

# # pythomir.move("north", 50)
# # pythomir.move("west", 10)
# # pythomir.move("climb", 0)

# # bugoonya.move("north", 50)
# # bugoonya.move("west", 10)
# # pythomir.move("climb", 0)

# # # Не удаляйте код ниже, это проверка!

# # if not 'Character' in dir():
# #     print("Общий класс родитель Character не создан")

# # if not hasattr(Character, "move"):
# #     print("У общего класса отсутствует метод move")


# class Enemy():

#     def __init__(self, name, health):

#         self.is_alive = True
#         self.name = name
#         self.health = health


# class Dragon(Enemy):

#     def bite(self):
#         print("я кусаюсь")

#     def burn(self):
#         print("я дышу огнем")


# dragon = Dragon("Инхеритий Проворный", 300)

# # Не удаляйте код ниже, это проверка!

# dragon.bite()
# dragon.burn()


# class Hero():

#     def __init__(self, name, posessions):
#         self.name = name
#         self.posessions = posessions

#     def __repr__(self):
#         return f'Геронй {self.name} взял с собой {" ".join(self.posessions)} '


# # Не удаляйте код ниже, он нужен для проверки

# hero = Hero("Питомир", ["меч", "плащ", "шляпа"])
# print(hero)


# class Box():

#     def __init__(self, size, weight, contains):
#         self.size = size
#         self.weight = weight
#         self.contains = contains

#     def observe(self):
#         return f"Это похоже на ящик размером {self.size} и весом {self.weight}"


# class Container(Box):

#     def open(self):
#         return f"В ящике размером {self.size} и весом {self.weight} кг оказалось {self.contains}"


# box_1 = Box("30x30", 1, "15 золотых монет")

# container_1 = Container("50x30", 2, "7 золотых монет")

# # Код проверки, не удаляйте его

# try:
#     Box
# except:
#     print("Класс Box не задан")
# try:
#     Container
# except:
#     print("Класс Container не задан")
# try:
#     Container.open
# except:
#     print("Метод open у Container не задан или с ошибкой")
# try:
#     Container.observe
# except:
#     print("Метод observe у Container не наследуется или с ошибкой")
# try:
#     box_1
# except:
#     print("Экземпляр box_1 не существует")
# try:
#     container_1
# except:
#     print("Экземпляр container_1 не существует")

# print(container_1.observe())
# print(container_1.open())
