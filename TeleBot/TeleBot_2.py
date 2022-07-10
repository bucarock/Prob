import random

from datetime import datetime
vrem = datetime.now()
#print(vrem)
#print(vrem.year)
#print(vrem.month)
#print(vrem.day)
if vrem.minute < 10:
    print(vrem.hour,':', '0', vrem.minute)
else:
    print((vrem.hour), ':', (vrem.minute))

#print(vrem.minute)
#print(vrem.second)
#print(vrem.microsecond)
dict = {1: 'Кони одинаково дохнут и от работы и от перекура. В общем, совершенно не приспособленное животное, ни к работе, ни к отдыху',
     2: 'Объявление. Цирк примет на работу еще 10 воздушных гимнастов',
     3: 'В древности гонца вешали, если он приносил голосовое сообщение',
     4: 'Сидя на двух диетах похудеешь быстрее. И голодать не будешь!',
     5: 'Путь к сердцу мужчины лежит через просто оставьте его в покое'}
keys = list(dict.values())
z = keys[random.randint(0,4)]
print(z)
