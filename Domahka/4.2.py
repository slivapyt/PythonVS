words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}
coins = 0
answers = {}
print("Выберите уровень сложности.")
chous_lvl = input("Легкий, средний, сложный.\n".lower())
print("Выбран уровень сложности, мы предложим 5 слов, подберите перевод.")
input("Нажмите Enter.")
if chous_lvl == "легкий":
    words = words_easy
elif chous_lvl == "средний":
    words = words_medium
else:
    words = words_hard
for k, v in words.items():
    print(f'{k}, {len(v)} букв, начинается на {v[0:1]}...')
    assumption = input()
    if assumption == v:
        print(f'Верно, {k} — это {v}.')
        answers[k] = True
        coins += 1
    else:
        print(f'Неверно. {k} — это {v}.')
        answers[k] = False
ans_pravda = [y for y in answers if answers[y] is True]
ans_neprava = [y for y in answers if answers[y] is False]
print("\nПравильно отвечены слова:")
print("\n".join(ans_pravda))
print("\nНеправильно отвечены слова:")
print("\n".join(ans_neprava))
print(f'''
Ваш ранг:
{levels[coins]}''')
