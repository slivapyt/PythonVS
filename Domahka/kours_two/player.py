
class Player():
    def __init__(self, name):
        self.name = name
        self.used_words = []

    def get_quantity_words(self):
        return len(self.used_words)

    def get_used_words(self, word):
        self.used_words.append(word)

    def check_word_in_used(self, word):
        if word in self.used_words:
            return True
        else:
            return False


# class Player:
#     def __init__(self, name):
#         self.name = name
