# Чтобы не держать в голове название геттеров и сеттеров
class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old
    def get_old(self):
        return self.__old
    def set_old(self, new_value):
        self.__old = new_value

    old = property(get_old, set_old)

p = Person("Sergei", 33)