class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationary):
    def draw(self):
        print('Вы пишите ручкой. Прошлый век, да? Отнюдь.')


class Pensil(Stationary):
    def draw(self):
        print('Это что, карандаш? Вы, наверное, художник? Или не нашлось ручки, ха?')


class Handle(Stationary):
    def draw(self):
        print('О, это инструмент улиц. Вы рисуете граффити? Или просто любите писать жирно?')


station = Stationary('Название')
print(station.title)
station.draw()
station = Pen('Название')
station.draw()
station = Pensil('Название')
station.draw()
station = Handle('Название')
station.draw()
