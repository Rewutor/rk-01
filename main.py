num = int(input("Введите число "))

if num < 2 :
    print (f"{num} число меньше 2")
elif num > 2 :
    print (f"{num} Больше двух")
else:
    print("Число равно 2")

num2 = int(input("Введите второе число"))

res = num + num2

word = "Оченьдлинноепредложение"

result = ""
for i in range(res):
    if i <len(word):
        print(word[i])
        result = result + word[i]

    else:
        print("Строка окончена")
        break

print(f"Сохраненные буквы \n{result}")

reverse = result[::-1]

print(reverse)

spisok= ["питон","разрез","огузок","банан"]

print(f"\nИщем совпадающие буквы с: {result}")

# Для каждого слова в списке
for word in spisok:
    print(f"\nСлово '{word}':")
    
    # Находим общие буквы
    common_letters = []
    for letter in result:
        if letter in word and letter not in common_letters:
            common_letters.append(letter)
    
    if common_letters:
        print(f"  Совпадают буквы: {', '.join(common_letters)}")
    else:
        print("  Нет общих букв")


for word in spisok:
    print(f"\nСлово '{word}'")

    common_letters = []
    for letter in result:
        if letter in word and letter not in common_letters:
            common_letters.append(letter)
        
    if common_letters:
        print (f" Совпадающие буквы: {', '.join(common_letters)}")
        print(f" число букв: {len(common_letters)}")
    else:
        print(" Нет общих букв")


left = 25
print(f"\n Складываем все строки {result + reverse+ str(left)}")

right = len(result+reverse+str(left))
print(f"\n Число символов {right} ")

keys = {'green': 20, 'red': 24, 'blue': 22}

found_key= None

for key,value in keys.items():
    if value == right:
        found_key = key
        break

if found_key:
    print(f"Совпал ключ '{found_key}' имеет значение {right}")
else:
    print('Значения не найдено')


HEX_TO_ANSI = {
    '#FF0000': '\033[91m',  # red
    '#00FF00': '\033[92m',  # green
    '#0000FF': '\033[94m',  # blue
    '#FFFF00': '\033[93m',  # yellow
    '#800080': '\033[95m',  # purple
    '#00FFFF': '\033[96m',  # cyan
    '#FFA500': '\033[93m',  # orange (как желтый)
    '#FFC0CB': '\033[95m',  # pink (как фиолетовый)
    '#A52A2A': '\033[31m',  # brown (темно-красный)
    '#808080': '\033[90m',  # gray
    '#000000': '\033[30m',  # black
    '#FFFFFF': '\033[97m',  # white
    '#FF00FF': '\033[95m',  # magenta (как фиолетовый)
    '#008080': '\033[96m',  # teal (как бирюзовый)
    '#E6E6FA': '\033[97m',  # lavender (как белый)
    '#FF7F50': '\033[91m',  # coral (как красный)
    '#FFD700': '\033[93m',  # gold (как желтый)
    '#C0C0C0': '\033[97m',  # silver (как белый)
    '#000080': '\033[94m',  # navy (как синий)
}

print(f"\n🎨 Выводим число {right} цветами из файла:")

with open('text.txt', 'r', encoding='utf-8') as my_file:
    lines = list(my_file)
    
    # Если right больше чем строк в файле, используем модуль
    line_index = (right - 1) % len(lines)  # -1 потому что индексы с 0
    
    for n, line in enumerate(lines):
        line = line.strip()
        if '=' in line:
            color_name, hex_code = line.split('=')
            hex_code_upper = hex_code.upper()
            ansi_color = HEX_TO_ANSI.get(hex_code_upper, '\033[97m')
            
            # Выводим все строки
            print(f"{n+1:03} {ansi_color}{color_name}: {hex_code}\033[0m")
            
            # Если это строка, соответствующая right
            if n == line_index:
                chosen_color = ansi_color
                chosen_name = color_name

print(f"\n{chosen_color}✨ Число {right} выводится цветом '{chosen_name}'\033[0m")




# ========== ЛОГИРОВАНИЕ В ФАЙЛ ==========
from datetime import datetime

def log_color_to_file(color_name, number, filename='color_log.txt'):
    """
    Записывает в файл информацию о цвете
    """
    # Текущее время
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    
    # Формируем запись для файла
    log_entry = f"[{now}] Цвет: {color_name} | Число: {number}\n"
    
    # Записываем в файл
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    
    # Выводим на экран подтверждение
    print(f"✅ Записано в лог: {color_name} = {number}")

# ========== ВЫЗЫВАЕМ ФУНКЦИЮ ==========
if 'chosen_name' in locals() and 'right' in locals():
    log_color_to_file(chosen_name, right)
    
    # Показываем содержимое лога
    print(f"\n📋 СОДЕРЖИМОЕ ЛОГ-ФАЙЛА:")
    print("-" * 40)
    
    try:
        with open('color_log.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            if content:
                print(content)
            else:
                print("Лог-файл пуст")
    except FileNotFoundError:
        print("Лог-файл создан, но ещё пуст")

import json

profile = {

    "name": "Иван",
    "age": 22,
    "id": 485579,
    "city": "Москва"
    }

with open ('profilev1.json', 'w', encoding='utf-8') as f:
    json.dump(profile, f, ensure_ascii=False, indent=4)

print("Данные сохранены в файл JSON")



with open('profilev1.json', 'r',encoding='utf-8') as f:
    loaded_data = json.load(f)

print("Считанные данные")

print(loaded_data)

print(f"Тип:{type(loaded_data)}")




#Ver2

profile = {
    "485579": {  # ID как ключ
        "name": "Иван",
        "age": 22,
        "city": "Москва"
    }
}

# Сохраняем
with open('profilev2.json', 'w', encoding='utf-8') as f:
    json.dump(profile, f, ensure_ascii=False, indent=4)

print("Данные сохранены")

# Новый человек
new_person = {
    "485580": {  # новый ID
        "name": "Серега",
        "age": 24
        
    }
}

try:
    with open('profilev2.json', 'r', encoding='utf-8') as f:
        all_profiles = json.load(f)
except FileNotFoundError:
    all_profiles = {}

# Добавляем нового человека
all_profiles.update(new_person)

# Сохраняем обратно
with open('profilev2.json', 'w', encoding='utf-8') as f:
    json.dump(all_profiles, f, ensure_ascii=False, indent=4)

print(f"Добавлен {new_person['485580']['name']}")

# Показываем всё
print("\n Все профили:")
for user_id, user_data in all_profiles.items():
    print(f"ID: {user_id}, Имя: {user_data['name']}, Возраст: {user_data['age']}, Город: {user_data['city']}")


def add_profile_to_file(user_id, name, age, city=None, filename='profilev2.json'):
    """
    Добавляет новый профиль в JSON файл
    
    Параметры:
    user_id (str): ID пользователя
    name (str): Имя
    age (int): Возраст
    city (str): Город (необязательный)
    filename (str): Имя файла
    """
    # Создаём нового человека
    new_person = {
        user_id: {
            "name": name,
            "age": age
        }
    }
    
    # Добавляем город, если он указан
    if city:
        new_person[user_id]["city"] = city
    
    # Читаем существующий файл
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            all_profiles = json.load(f)
        print(f"Прочитано {len(all_profiles)} профилей")
    except FileNotFoundError:
        all_profiles = {}
        print("Создан новый файл")
    
    # Добавляем нового человека
    all_profiles.update(new_person)
    
    # Сохраняем обратно
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_profiles, f, ensure_ascii=False, indent=4)
    
    print(f" Добавлен {name} (ID: {user_id})")
    
    # Возвращаем обновлённый словарь
    return all_profiles


def show_all_profiles(filename='profilev2.json'):
    """Показывает все профили из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            profiles = json.load(f)
        
        print(f"\n Все профили (всего: {len(profiles)}):")
        print("-" * 50)
        
        for user_id, user_data in profiles.items():
            name = user_data.get('name', 'Неизвестно')
            age = user_data.get('age', '?')
            city = user_data.get('city', 'Не указан')
            print(f"ID: {user_id}")
            print(f"  Имя: {name}")
            print(f"  Возраст: {age}")
            print(f"  Город: {city}")
            print()
            
    except FileNotFoundError:
        print("Файл не найден")


profile = add_profile_to_file(
    user_id="485581",
    name="Анна",
    age=27,
    city="Питер"
)

show_all_profiles()