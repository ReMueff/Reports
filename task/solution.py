import re

with open('task.txt', 'r+', encoding='utf-8') as file:
    text = file.read()

# 1.найти все натуралльные числа

s = re.compile(r"[0-9]+")
print('\nЗадание №1:\n', s.findall(text), end='\n\n')

# 2.Найдите все «слова», написанные капсом (то есть строго заглавными), возможно внутри настоящих слов (аааБББввв)

print('Задание №2:\n', re.findall(r'\b[a-zа-я]*[A-ZА-Я]{2,}[a-zа-я]*\b', text), end='\n\n')

# 3.Найдите слова, в которых есть русская буква, а когда-нибудь за ней цифра

print('Задание №3:\n', re.findall(r'\b[А-Я]\S+\d+\S+\b', text), end='\n\n')

# 4. Найдите все слова, начинающиеся с русской или латинской большой буквы (\b — граница слова)

print('Задание №4:\n', re.findall(r'\b[a-zA-Zа-яА-ЯёЁ]\S+\b', text), end='\n\n')

# 5. Найдите слова, которые начинаются на гласную (\b — граница слова)

print('Задание №5:\n', re.findall(r'\b[аеёиоуэюяАЕЁИОУЭЮЯaeioyuAEIOYU]\S+\b', text), end='\n\n')

# 6. Найдите все натуральные числа, не находящиеся внутри или на границе слова

print('Задание №6:\n', re.findall(r'\W*([1-9]+)\W*', text), end='\n\n')

# 7. Найдите строчки, в которых есть символ * (. — это точно не конец строки!)

print('Задание №7:\n', re.findall(r'[\n^](.*\*.*)\n', text), end='\n\n')

# 8. Найдите строчки, в которых есть открывающая и когда-нибудь потом закрывающая скобки

print('Задание №8:\n', re.findall(r'[\n^](.*\(.*\).*)\n', text), end='\n\n')

# 9. Выделите одним махом весь кусок оглавления (в конце примера, вместе с тегами);

print('Задание №9:\n', re.findall(r'(<a href=.*)+', text), end='\n\n')

# 10. Без тегов

print('Задание №10:\n', re.findall(r': (.*)</a>', text), end='\n\n')

# 11. Найдите пустые строчки

empty = (re.findall(r'(.){0}\n\n', text))

print(f"Задание №11:\nКоличество пустых строк: {len(empty)}")
