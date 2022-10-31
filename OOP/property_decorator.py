# Чтобы не держать в голове название геттеров и сеттеров
class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, new_value):
        self.__old = new_value

    # 1
    # old = property(get_old, set_old) Или второй вариант через декораторы:

    # 2
    # old = old.setter(set_old)
    # old = old.getter(get_old)

    # 3 Третий способ на практике чаще используют:
    # @property
    # def old(self):
    #     return self.__old
    #
    # @old.setter
    # def old(self, new_value):
    #     self.__old = new_value
    #
    # @old.deleter
    # def old(self):
    #     del self.__old

p = Person("Sergei", 33)
p.old = 35  # Сеттер для экземпляра класса __old, а не создает еще одну переменную в p.__dict__. Если бы не было, то сделал локальную переменную.
