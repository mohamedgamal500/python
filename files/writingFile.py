words = ['hi', 'jemy', 'hi', 'jemy', 'hi', 'jemy']
# write
write_fileref = open('jemy.txt', 'w')
for word in words:
    write_fileref.write(word)
    write_fileref.write('\n')
write_fileref.close()
# read
read_fileref = open('jemy.txt', 'r')
lin = read_fileref.read()[:4]  # string(readline and read) , list(readlines)
print(type(lin))

'''for line in read_fileref:
    print(line.strip())
read_fileref.close()'''
