# Продемонстрируйте разные уровни доступа на примере любого класса

class Ferma:
    a = 100 # Коровы . public
    _b = 200 # Овцы  . protected
    __c = 30 # Лошади . private

Ferma()
print('Количество голов коров - ', Ferma.a)
print('Количество голов овец - ', Ferma._b)
print('Количество голов лошадей - ', Ferma._Ferma__c)