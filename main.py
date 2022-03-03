name: str = 'Сабина.'
age = 18
print('Меня зовут', name, 'Мне', age, 'лет')

y = 'Сабина'
x = y * 4 + y
print(x)

username = input('Хэй!Как тебя зовут?')
print('Приветик,',username)
userage = int(input('Сколько тебе лет?'))
if userage >= 18:
    print('Только не делай глупостей, прошу! О, черт, я уже опоздал, да?')
elif userage < 18:
    print('Ты потерялся? Где твоя мама?')
elif userage >= 30:
    print('Возраст не такая уж и важная вещь ведь...честно говорю')

print(username[2:-1])
print(username[::-1])
print(username[:3])
print(username[5:])

print(username.upper())
print(username.lower())
print(username.capitalize()) # or name.title()
U = username.capitalize()
print(U.swapcase())

print('2+2*2?')
a = int(input())
if a == 6:
    print('Ты умничка!!')
else:
    print('А теперь вспомни чередование действий, ага?')
    a2 = int(input())
    if a2 == 6:
        print('Так-то лучше, умничка!')

#5,7,9 не вышло((((((((