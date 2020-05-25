#2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
from itertools import count

text_writer = open('Text1.txt', 'w')                #Не удержался и создал программно :(
writer = None
for i in count(1):
    if writer == '':
        text_writer.write('\n')
        break
    writer = (input('Введите текст. Нажмите на Enter, чтобы перестать: '))
    text_writer.write(writer)
    text_writer.write('\n')                          #Выше: создаем файл и с помощью input добавляем в него символы
print(f'Всего {i - 2} строк')                        #Выводим количество строк за вычетом двух лишних после Enter
text_writer.close()

check_chars = open('Text1.txt', 'r')
words = 0                                               #Создаем переменную, в которой будем держать количество слов
for line in check_chars:
    words_maker = line.split()                          #Делим файл на слова
    words = words + len(words_maker)                    #Считаем количество слов.
print(f'всего' , words , 'слов.')
