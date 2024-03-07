from get_word import BasicWord
from player import Player
from utils import load_web_dictionary
random_word = load_web_dictionary()
get_rand_word = BasicWord(random_word)


name = input("Введите имя игрока\n")

print(f"Привет, {name}!")
print(f"Составьте {get_rand_word.quantity_short_words()} слов из слова {
      get_rand_word.get_main_word().upper()}\nСлова должны быть не короче 3 букв")
print(f'Что бы закончить игру, угадайте все слова или напишите "стоп"')
print(f"Поехали, ваше первое слово?\n")

player_class = Player(name)

while player_class.get_quantity_words() < get_rand_word.quantity_short_words():
    inp_word = input()
    if len(inp_word) > 2:
        if inp_word != "стоп":
            if get_rand_word.try_chek(inp_word):
                if not player_class.check_word_in_used(inp_word):
                    print("верно")
                    player_class.get_used_words(inp_word)
                else:
                    print("уже использовано")
            else:
                print("неверно")
        else:
            break
    else:
        print("слишком короткое слово")

print(f"Игра завершена, вы угадали {
    player_class.get_quantity_words()} слов!")
