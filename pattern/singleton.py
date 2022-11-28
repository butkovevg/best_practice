""" механизм создания одного и только один экземпляра объекта, и предоставление к нему глобальную точку доступа.

цель шаблона Singleton заключаются в следующем:
• Обеспечение создания одного и только одного объекта класса
• Предоставление точки доступа для объекта, который является глобальным для программы
• Контроль одновременного доступа к ресурсам, которые являются общими

Примеры использования:
• ведение журнала
• операции с базой данных
• диспетчера очереди печати
"""


class Singleton:
    __instance = None
    def __init__(self,a):
        if not Singleton.__instance:
            print("1")
            self.a = a
        else:
            self.a = a
            print(2, self.getInstance())
        print(self.a)
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            print(3)
            cls.__instance = Singleton()
        return cls.__instance
s0 = Singleton(1) ## class initialized, but object not created
s1 = Singleton(2) ## instance already created
s2 = Singleton(3) ## instance already created
s3 = Singleton(4) ## instance already created

