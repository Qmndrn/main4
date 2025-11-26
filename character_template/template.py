from jinja2 import Environment, FileSystemLoader, select_autoescape
import random

characters_list = [
    'Орк', 'Эльф', 'Человек', 'Гном', 'Гоблин', 'Драконид'
]
character_classes = ['Лучник', 'Ассасин', 'Бард', 'Воин', 'Маг']

classes_base = {
    'Маг': {
        'skills': [
            'Стрела ледяного огня', 'Снятие проклятия', 'Огненный взрыв',
            'Обледенение', 'Ледяное копье', 'Конус холода', 'Прилив сил',
            'Морозный доспех'
        ],
        'stats': {'intelligence': 15},
        'image': 'character_template/images/wizard.png'
    },
    'Воин': {
        'skills': [
            'Блок щитом', 'Казнь', 'Рывок', 'Боевой крик', 'Вихрь',
            'Парирование', 'Мощный удар', 'Глубокие раны'
        ],
        'stats': {'strength': 15},
        'image': 'character_template/images/warrior.png'
    },
    'Лучник': {
        'skills': [
            'Верный выстрел', 'Чародейский выстрел', 'Стенающая стрела',
            'Стрелы ветра', 'Призыв питомца', 'Глаз зверя',
            'Осветительная ракета', 'Приручение животного'
        ],
        'stats': {'agility': 15},
        'image': 'character_template/images/archer.png'
    },
    'Ассасин': {
        'skills': [
            'Отравление', 'Взлом замка', 'Подлый трюк', 'Исчезновение',
            'Ложный выпад', 'Внезапный удар', 'Ошеломление', 'Спринт'
        ],
        'stats': {'luck': 15},
        'image': 'character_template/images/assasin.png'
    },
    'Бард': {
        'skills': [
            'Аккорды ветра', 'Аккорды воды', 'Исцеление', 'Соната жизни',
            'Пауза', 'Плач сирен', 'Песнь ветра', 'Реквием'
        ],
        'stats': {'temper': 15},
        'image': 'character_template/images/bard.webp'
    }
}

env = Environment(
    loader=FileSystemLoader('character_template'),
    autoescape=select_autoescape(['html'])
)
template = env.get_template('template.html')


def get_race():
    for racenumber, race in enumerate(characters_list, 1):
        print(f"{i}. {race}")
    choice = int(input("Выберите расу персонажа: "))
    return characters_list[choice - 1]


def get_class():
    for classnumber, cls in enumerate(character_classes, 1):
        print(f"{i}. {cls}")
    choice = int(input("Выберите класс персонажа: "))
    return character_classes[choice - 1]


def main():
    char_num = int(input("Сколько персонажей создать?(числом): "))
    for numofchars in range(char_num):
        name = input("Введите имя персонажа: ").strip()
        character_race = get_race()
        print(f"Вы выбрали: {character_race}")

        character_class = get_class()
        print(f"Вы выбрали: {character_class}")

        stats = {
            'strength': random.randint(1, 3),
            'agility': random.randint(1, 3),
            'intelligence': random.randint(1, 3),
            'luck': random.randint(1, 3),
            'temper': random.randint(1, 3)
        }

        stats.update(classes_base[character_class]['stats'])

        first_skill, second_skill, third_skill = random.sample(
            classes_base[character_class]['skills'], 3
        )

        rendered_page = template.render(
            name=name,
            race=character_race,
            character_class=character_class,
            strength=stats['strength'],
            agility=stats['agility'],
            intelligence=stats['intelligence'],
            luck=stats['luck'],
            temper=stats['temper'],
            image=classes_base[character_class]['image'],
            first_skill=first_skill,
            second_skill=second_skill,
            third_skill=third_skill
        )

        with open('characters/index{i+1}.html', 'w', encoding='utf8') as file:
            file.write(rendered_page)


if __name__ == '__main__':
    main()
