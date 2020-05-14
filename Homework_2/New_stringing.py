count = 0
word_length = 0
user_words = input('Введите несколько символов через пробелы: ')
user_words = user_words.split()
for word in user_words:
    count = count + 1
    print(f'{count})', word[:10])






