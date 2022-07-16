'''Задание 3
Пользователь вводит с клавиатуры строку и символ
для поиска. Посчитайте сколько раз в строке встречается
искомый символ. Полученное число выведите на экран.'''
word = '''In both cases this allows any modifications required due to UI changes 
to all be made in one place. Useful information on this technique can be found on 
numerous blogs as this ‘test design pattern’ is becoming widely used. We encourage the 
reader who wishes to know more to search the internet for blogs on this subject. Many have 
written on this design pattern and can provide useful tips beyond the scope of this user guide. 
To get you started, though, we’ll illustrate page objects with a simple example.'''
letter = 'e'
count = 0
for symbol in word:
    if letter == symbol:
        count = count + 1

print(f'Count of symbols {letter} : {count}')

'''Задание 4
Пользователь вводит с клавиатуры строку и слово
для поиска. Посчитайте сколько раз в строке встречается
искомое слово. Полученное число выведите на экран.'''
word = '''lllIn both cases this allows any modifications required due to UI changes 
to all be made in one place. Useful information on this technique can be found on 
numerous blogs as this ‘test design pattern’ is becoming widely used. We encourage the 
reader who wishes to know more to search the internet for blogs on this subject. Many have 
written on this design pattern and can provide useful tips beyond the scope of this user guide. 
To get you started, though, we’ll illustrate page objects with a simple example.'''
letters = 'll'
letters_length = len(letters)
count = 0
for i in range(len(word) - letters_length):
    if letters == word[i:(i + letters_length)]:
        count = count + 1

print(f'Count of symbols {letters} : {count}')

# 3.1-4.1
word = '''In both cases this allows any modifications required due to UI changes 
to all be made in one place. Useful information on this technique can be found on 
numerous blogs as this ‘test design pattern’ isisis becoming widely used. We encourage the 
reader who wishes to know more to search the internet for blogs on this subject. Many have 
written on this design pattern and can provide useful tips beyond the scope of this user guide. 
To get you started, though, we’ll illustrate page objects with a simple example.'''
letters = 'll'
count = word.count(letters)
print(f'Count of symbols {letters} : {count}')

'''Задание 5
Пользователь вводит с клавиатуры строку, слово для
поиска, слово для замены. Произведите в строке замену
одного слова на другое. Полученную строку отобразите
на экране.'''
text = '''In both cases this allows any modifications required due to UI changes 
to all be made in one place. Useful information on this technique can be found on 
numerous blogs as this ‘test design pattern’ is becoming widely used. We encourage the 
reader who wishes to know more to search the internet for blogs on this subject. Many have 
written on this design pattern and can provide useful tips beyond the scope of this user guide. 
To get you started, though, we’ll illustrate page objects with a simple example.'''
old_word = 'this'
new_word = 'THIS'
lenth_of_word = len(old_word)
for i in range(len(text) - lenth_of_word):
    if old_word == text[i:(i + lenth_of_word)]:
        text = text[:i] + new_word + text[i + lenth_of_word:]
print(text)
text = '''In both cases this allows any modifications required due to UI changes 
to all be made in one place. Useful information on this technique can be found on 
numerous blogs as this ‘test design pattern’ is becoming widely used. We encourage the 
reader who wishes to know more to search the internet for blogs on this subject. Many have 
written on this design pattern and can provide useful tips beyond the scope of this user guide. 
To get you started, though, we’ll illustrate page objects with a simple example.'''
old_word = 'this'
new_word = 'THIS'
text = text.replace(old_word, new_word)
print(text)

'''Задание 1
Есть некоторый текст. Реализуйте следующую функциональность:
■ Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
■ Посчитайте сколько раз цифры встречаются в тексте;
■ Посчитайте сколько раз знаки препинания встречаются в тексте;
■ Посчитайте количество восклицательных знаков в тексте.'''
text = '''because we’re encouraging the developer of a test to try and think about the services that they’re interacting with rather than the implementation, PageObjects should seldom expose the underlying WebDriver 
instance. to facilitate this, methods on the PageObject should return other PageObjects. this means that we can effectively model the user’s journey through our application 1! It also means that should the way that pages relate to one another change (like when the login page asks the user to change their password the first time they log into a service, when it previously didn’t do that) simply changing the appropriate method’s signature will cause the tests to fail to compile! put another way, we can tell which tests would fail without needing to run them when we change the relationship between 3 pages and reflect this in the PageObjects!'''
# 1.1
for i in range(len(text) - 2):
    if text[0].islower():
        text = text[0].upper() + text[1:]
    elif text[i:i + 2] == '. ' and text[i + 2].islower():
        text = text[:i + 2] + text[i + 2].upper() + text[i + 3:]
print(text)
# 1.2
number_count = 0
for letter in text:
    if letter.isdigit():
        number_count = number_count + 1
# 1.3
symbols = '.,:;!?'
symbol_count = 0
for letter in text:
    if letter in symbols:
        symbol_count = symbol_count + 1

# 1.4
symbol = '!'
symbol_count = 0
for letter in text:
    if letter == symbol:
        symbol_count = symbol_count + 1

a = '123456'
b = 'ABcd'
print(a.isdigit())
print(b.isalpha())
text = '''because we’re encouraging the developer of a test to try and think about the services that they’re interacting with rather than the implementation, PageObjects should seldom expose the underlying WebDriver 
instance. to facilitate this, methods on the PageObject should return other PageObjects. this means that we can effectively model the user’s journey through our application 1! It also means that should the way that pages relate to one another change (like when the login page asks the user to change their password the first time they log into a service, when it previously didn’t do that) simply changing the appropriate method’s signature will cause the tests to fail to compile! put another way, we can tell which tests would fail without needing to run them when we change the relationship between 3 pages and reflect this in the PageObjects!'''
print(text.find('e !'))
print(text.rfind('e'))
text = text.upper()
print(text)
text = text.lower()
print(text)
text = text.title()
print(text)
text = text.capitalize()
print(text)

print()
# ****
text = '''because we’re encouraging the developer of a test to try and think about the services that they’re interacting with rather than the implementation, PageObjects should seldom expose the underlying WebDriver 
instance. to facilitate this, methods on the PageObject should return other PageObjects. this means that we can effectively model the user’s journey through our application 1! It also means that should the way that pages relate to one another change (like when the login page asks the user to change their password the first time they log into a service, when it previously didn’t do that) simply changing the appropriate method’s signature will cause the tests to fail to compile! put another way, we can tell which tests would fail without needing to run them when we change the relationship between 3 pages and reflect this in the PageObjects!'''

# 1.1.1
low_letter = 'abcdefghijklmnopqrstuvwxyz'
up_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(text) - 2):
    if text[0].islower():
        for j in range(len(low_letter)):
            if text[0] == low_letter[j]:
                text = up_letter[j] + text[1:]
    elif text[i:i + 2] == '. ' and text[i + 2].islower():
        for j in range(len(low_letter)):
            if text[i] == low_letter[j]:
                text = text[:i + 2] + up_letter[j] + text[i + 3:]
print(text)
