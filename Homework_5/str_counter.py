from itertools import count

text_writer = open('Text1.txt', 'w')
writer = None
for i in count(1):
    if writer == '':
        text_writer.write('\n')
        break
    writer = (input('Введите текст. Нажмите на Enter, чтобы перестать: '))
    text_writer.write(writer)
    text_writer.write('\n')
print(f'Всего {i - 2} строк')
text_writer.close()

check_chars = open('Text1.txt', 'r')
words = 0
for line in check_chars:
    words_maker = line.split()
    words = words + len(words_maker)
print(f'всего' , words , 'слов.')
