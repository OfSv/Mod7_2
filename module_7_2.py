# Позиционирование в файле
# Задача  "Записать и запомнить"

'''
Записываем в файл file_name все строки из списка strings, каждая на новой строке.
Возвращаем словарь strings_positions
(ключ - кортеж (<номер строки>,<байт начала строки>), значение - записанная строка)
'''

def custom_write(file_name, strings):
    file_name = 'test.txt'
    strings_positions = {}
    i = 0
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings:
        i += 1
        b = file.tell()
        file.write(f'{string}\n')
        strings_positions[(i, b)] = string
    file.close()
    print('словарь: ', strings_positions)
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
