cheat_word= open('words.txt', 'r')
cheat_list = ((cheat_word.read()).splitlines())

user_word = input("Insert word you want: ")
user_word_list = []
for x in user_word:
    user_word_list.append(x)

for word in cheat_list:
    if len(word) == len(user_word):
        cheat_word_index = 0
        for index in user_word_list:
            if index == "_":
                cheat_word_index += 1
                continue
            if index != word[cheat_word_index]:
                break
            cheat_word_index += 1

        if cheat_word_index == len(user_word):
            print(word)

