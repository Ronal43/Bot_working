f = open('mamba.txt', 'r+')
s = (f.read())
a = s.split('\n')
print (a)
f.close()
i = a.pop (0)
del a[0]
del a[-1]
a.insert('0', 'хуй')
print (i)
print (a)
f = open('mamba.txt', 'w')
for index in a:
    f.write(index + '\n')
f.close
f = open('mamba.txt', 'r+')
s = (f.read())
a = s.split('\n')
print (a)
f.close()
