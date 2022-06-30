# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла:
# test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os
import os
os.mkdir('DZ')
os.chdir('DZ')
print(os.getcwd())
f1=open('test_1.txt', 'w')
f2=open('test_2.txt', 'w')
f3=open('test_3.txt', 'w')
f1.close()
f2.close()
f3.close()
os.rename('test_1.txt','rename_1.txt')
os.rename('test_2.txt','rename_2.txt')
os.rename('test_3.txt','rename_3.txt')
os.remove('rename_1.txt')
os.remove('rename_2.txt')
os.remove('rename_3.txt')
os.chdir('..')
os.rmdir('DZ')