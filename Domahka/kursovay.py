import random
answers = []
count = 0


def trans_morze(word):
    """Переводит на морзе"""
    morze = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-"
    }
    morze_word = []
    for letter in word:
        morze_word.append(morze[letter])
    return morze_word


def random_word():
    words = ["day", "sun", "rice", "snow", "rain", "war", "lizard", "fix"]
    random_result = random.choice(words)
    return random_result


def result_answers(answers):
    true_ans = 0
    false_ans = 0
    for answer in answers:
        if answer is True:
            true_ans += 1
        else:
            false_ans += 1
    print(f"""
Всего задачек: {len(answers)}
Отвечено верно: {true_ans}
Отвечено неверно: {false_ans} """)


input("""Сегодня мы потренируемся расшифровывать морзянку.
Нажмите Enter и начнем
""")

while count < 5:
    r_w = random_word()
    r_morze_w = (trans_morze(r_w))
    response = input(''.join(r_morze_w))
    if response == r_w:
        count += 1
        print(f"Верно, {r_w} \n")
        answers.append(True)
    else:
        count += 1

        print(f"Неверно {r_w}\n")
        answers.append(False)
result_answers(answers)
