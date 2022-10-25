"""Инкапсуляция
  attribute - public
 _attribute - protected Сигнализирует это внутренняя служебная переменная и что атрибут является защищенным. явно не ограничевая доступ извне.
__attribute - private
"""


class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self._y = y
        self.__z = z

    # интерфейсные методы: сеттеры и геттеры.
    def set_coord(self, x=0, y=0, z=0):
        if type(x) in (int, float):
            self.x = x
        else: raise ValueError("Координата должна быть числом")
        self._y = y
        self.__z = z
    def get_coord(self):
        return (self.x, self._y, self.__z)

point = Point(1, 2, 3)
# point.x
# point._y  Желательно обращаться через методы класса
# point.__z Ошибка AttributeError. Только обращаться через методы класса
# point._Point__z но лучше так не делать

# from accessify import private, protected
# Перед методом класса добавить декоратор @private или @protected