# 3 задача
f = open('red.txt','w')
while True:
    s = input()
    if s == '':
        break
    f.write(s+'\n')
f.close()