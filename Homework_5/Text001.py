from itertools import count

text_creator = open('Text1.txt', 'a')
writer = None
for i in count(1):
    if writer == '':
        break
    writer = (input('Введите текст. Нажмите на Enter, чтобы перестать: '))
    text_creator.write(writer)
    text_creator.write('\n')
text_creator.close()





