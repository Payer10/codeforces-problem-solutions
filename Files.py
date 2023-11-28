'''#open a file
f = open('a.txt', 'w')

#getting some infos
print('name =', f.name)
print('is it closed?', f.closed)
print('mode =', f.mode)
f.write('my fovourite language is python')
f.close()

#appending to a file
f = open('a.txt', 'a')
f.write('i also love java')
f.close()

# r+ functionality
f = open('a.txt','r+')
info = f.read()
print(info)
f.close()
'''
# w+ mode
f = open('a.txt', 'w+')
f.write('python is best in the programe.')
f.close()