# Введи список, отсортируй его и оставь только уникальные элементы
# Примечание: Уникальные элементы - это элементы, которые появляются только один раз в списке
list1=[1,2,3,6,2,7,10,123,123,6,1,15,123,111,524]
list1.sort()
list2=[]
print(list1)
for i in range(len(list1)):
    s = list1.count(list1[i])
    if s == 1:
        list2.append(i)
    else:
        continue
else:
    print("ИТОГ: ")
print(list2)