# Есть словарь песен группы Depeche Mode
songsdict = {
'World in My Eyes': 4.76,
'Sweetest Perfection': 5.43,
'Personal Jesus': 4.56,
'Halo': 4.30,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.6,
'Policy of Truth': 4.88,
'Blue Dress': 4.18,
'Clean': 5.68,
}
print('общее звучание песен  =', sum(songsdict.values()))
# Создайте список песен, время звучаниях которых больше 5 минут
d_1 = songsdict.copy()
d_2 = songsdict.copy()
for key, value in songsdict.items():
    if value<5.00:
        d_1.pop(key)
print(d_1)
# Создайте новый словарь тех песен, в название которых состоит из одного слова
w = songsdict.keys()
for i in w:
    if i.isalpha():
        continue
    else:
        d_2.pop(i)
print(d_2)

