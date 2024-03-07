import json
from random import choice


def load_question(q_lst="Domahka/question_8_2.json"):
    '''Получаем данные о студенте из json'''
    with open(q_lst, "r") as file:
        data = json.load(file)
        return data


question_list = load_question()


def get_rand_q(question_list=question_list):
    count = 0
    list_rand_q = []
    while count < 5:
        count += 1
        list_rand_q.append(choice(question_list))

    return list_rand_q  # НЕ ВОЗВРАЩАЕТ БОЛЬШЕ СВОЕГО СПИСКА


rand_question = get_rand_q()


class Question():

    def __init__(self, rand_question=rand_question):
        self.rand_question = rand_question
        self.all_points = 0
        self.good_ans = 0

    def get_points(self):
        self.points = int(self.i_question["d"])*10
        self.all_points += self.points
        self.all_points

    def is_correct(self):
        if self.i_question["a"] == input():
            self.get_points()
            self.build_positive_feedback()
        else:
            self.build_negative_feedback()

    def build_question(self):
        for i_question in self.rand_question:
            self.i_question = i_question
            print(f"Вопрос: {i_question["q"]}\nСложность {i_question["d"]}/5")
            self.is_correct()
        return (f"Вот и все!\nОтвечено {self.good_ans} вопроса из {len(self.rand_question)}\nНабрано баллов: {self.all_points} ")

    def build_positive_feedback(self):
        print(f"Ответ верный, получено  баллов {self.points}")
        self.good_ans += 1

    def build_negative_feedback(self):
        print(f"Возвращает : Ответ неверный, верный ответ {
              self.i_question["a"]} ")


test = Question(rand_question)
print(test.build_question())
