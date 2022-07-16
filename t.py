f = open('test.txt', 'wt')
for i in range(200):
    f.write(f"{i}\n")
f.close()
f = open('test.txt', 'rt')
a = f.readlines()
f.close()
print(a)

f = open('test1.txt', 'wt')
f.writelines(a)
f.close()

f = open('test3.txt', 'wt')
for line in a:
    f.write(line)
f.close()

f = open('test2.txt', 'wt')
for line in a:
    if (int(line[:-1])) % 2 == 0:
        f.write(line)
f.close()

word = 'text'
word2 = ''
word1 = word
a = 'x'  # Было
b = 'XXX'  # Стало
for letter in word1:
    if letter == a:
        word2 = word2 + b
        continue
    word2 = word2 + letter

word = word2
print(word)
