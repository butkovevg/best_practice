
# SOLID

## Принцип Single responsibility (SRP)
    Один класс имеет только одну зону ответственности
    (Ограничен своей задачей)
## Принцип Open-closed (OCP)
    Можно расширять, но не модифицировать напрямую
## Принцип Liskov substitution (LSP)
    Родительский класс можно заменить на дочерний не ломая логику программы:
    Если в родителе и потомке есть метод, то на вход должно быть одно количество аргументов.

## Принцип Interface segregation (ISP)
    Класс-потомок не должен зависеть от методов, которые он не использует/не может использовать
## Принцип Dependency inversion (DIP)   
    Более высокоуцровневые модули не должны зависеть от низкоуровнывых, а должны зависить все от абстракций.
    Абстракции не должны зависеть от деталей(Детали должны зависеть от абстракции)