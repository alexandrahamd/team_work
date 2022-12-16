class Liquid:

    id: int  # номер жижи, реализовать автоинкремент
    title: str  # название
    density: float  # плотность
    ID = 0

    def __init__(self, title, density):
        Liquid.ID += 1
        self.id = Liquid.ID
        self.title = title
        self.density = density

    def __str__(self):
        return f'{self.id}. Жидкость {self.title} с плотностью {self.density}'

    def __eq__(self, other):
        return self.density == other

    def __lt__(self, other):
        return self.density > other

    def __gt__(self, other):
        return self.density < other


class Eatable(Liquid):
    __taste: str  # вкус, для которого нужно реализовать getter/setter

    def __init__(self, title, density, taste):
        super().__init__(title, density)
        self.__taste = taste

    @property
    def taste(self):
        return self.__taste

    @taste.setter
    def taste(self, taste):
        self.__taste = taste

    @taste.getter
    def taste(self):
        return self.__taste

    def __str__(self):
        return super().__str__() + ' пить можно ' + f'вкус: {self.__taste}'


class Technical(Liquid):
    __usage: str  # применение, для которого нужно реализовать getter/setter

    def __init__(self, title, density, usage):
        super().__init__(title, density)
        self.__usage = usage

    def __str__(self):
        return super().__str__() + ' пить нельзя ' + f'приминение: {self.__usage}'

    @property
    def usage(self):
        return self.__usage

    @usage.setter
    def usage(self, usage):
        self.__usage = usage

    @usage.getter
    def usage(self):
        return self.__usage


def sorting(sorting_list):
    return sorted(sorting_list)


if __name__ == '__main__':
    liquid_list = list()
    while True:
        print('Предлагаю вам ввести параметры жидкости')
        title = input('Введите название: ')
        if title == '-': break
        density = input('Введите плотность: ')
        type_of_liquid = input('Это можно пить? [Y/n]: ')
        if type_of_liquid in ('y', 'Y', ''):
            taste = input('Введите вкус')
            new_item = Eatable(title, density, taste)
            liquid_list.append(new_item)
        if type_of_liquid in ('n', 'N'):
            usage = input('Введите назначение')
            new_item = Technical(title, density, usage)
            liquid_list.append(new_item)
        else:
            raise ValueError
        sorting(liquid_list)

        for i in liquid_list:
            print(i)
