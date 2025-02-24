import file_operations
from faker import Faker
fake = Faker("ru_RU")
import random
import os




skills = [
          'Стремительный прыжок',
          'Электрический выстрел',
          'Ледяной удар',
          'Стремительный удар',
          'Кислотный взгляд',
          'Тайный побег',
          'Ледяной выстрел',
          'Огненный заряд'
          ]

letters_mapping = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


def replace_font(text, mapping):
    return ''.join([mapping.get(char, char) for char in text])


new_skills = [replace_font(skill, letters_mapping) for skill in skills]
runic_skills = []

for skill in new_skills:
    runic_skills.append(skill)

for i in range(1, 11):
    skills_new = random.sample(runic_skills, 3)

    # Контекст для рендеринга
    context = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": random.randint(3, 18),
        "agility": random.randint(3, 18),
        "endurance": random.randint(3, 18),
        "intelligence": random.randint(3, 18),
        "luck": random.randint(3, 18),
        "skill_1": skills_new[0],
        "skill_2": skills_new[1],
        "skill_3": skills_new[2]
    }

    rendered_template = file_operations.render_template("src/charsheet.svg", "result.svg", context)
    ## Сохранение результата в файл
    filename = os.path.join("output/src", f"result_{i}.svg")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(rendered_template)

    print(f"Файл {filename} создан и записан.")
    # Рендеринг шаблона
    file_operations.render_template("src/charsheet.svg", "result.svg", context)



# # Создаем директорию, если она не существует
# directory = "output/svg/"
# os.makedirs(directory, exist_ok=True)
#
# # Создаем и записываем 10 разных файлов
# for i in range(1, 11):
#     skills_new = random.sample(runic_skills, 3)
#     filename = os.path.join(f"result_{i}.svg")
#     print(f"Файл {filename} создан и записан.")
# context = {
#   "first_name": fake.first_name(),
#   "last_name": fake.last_name(),
#   "job": fake.job(),
#   "town": fake.city(),
#   "strength": random.randint(3, 18),
#   "agility": random.randint(3, 18),
#   "endurance": random.randint(3, 18),
#   "intelligence": random.randint(3, 18),
#   "luck": random.randint(3, 18),
#   "skill_1": skills_new[0],
#   "skill_2": skills_new[1],
#   "skill_3": skills_new[2]
# }
#
#
#
# file_operations.render_template("src/charsheet.svg", "result.svg", context)
#
#
#
