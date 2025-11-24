from jinja2 import Environment, FileSystemLoader, select_autoescape
import random


characters_list = ['Орк', 'Эльф', 'Человек','Гном', 'Гоблин', 'Драконид']
character_classes = ['Лучник', 'Ассасин', 'Бард', 'Воин', 'Маг']
classes_skills = {
 'Маг': ['Стрела ледяного огня', 'Снятие проклятия', 'Огненный взрыв', 'Обледенение', 'Ледяное копье', 'Конус холода', 'Прилив сил', 'Морозный доспех'],
 'Воин': ['Блок щитом', 'Казнь', 'Рывок', 'Боевой крик', 'Вихрь', 'Парирование', 'Мощный удар', 'Глубокие раны'],
 'Лучник': ['Верный выстрел', 'Чародейский выстрел', 'Стенающая стрела', 'Стрелы ветра', 'Призыв питомца', 'Глаз зверя', 'Осветительная ракета', 'Приручение животного'],
 'Ассасин': ['Отравление', 'Взлом замка', 'Подлый трюк', 'Исчезновение', 'Ложный выпад', 'Внезапный удар', 'Ошеломление', 'Спринт'],
 'Бард': ['Аккорды ветра', 'Аккорды воды', 'Исцеление', 'Соната жизни', 'Пауза', 'Плач сирен', 'Песнь ветра', 'Реквием']
}
classes_base = {
    'Маг': {
        'skills': classes_skills['Маг'],
        'stats': {
            'intelligence': 15,
        },
        'image': '../character_template/images/wizard.png'
    },
    'Воин': {
        'skills': classes_skills['Воин'],
        'stats': {
            'strength': 15,
        },
        'image': '../character_template/images/warrior.png'
    },
    'Лучник': {
        'skills': classes_skills['Лучник'],
        'stats': {
            'agility': 15,
        },
        'image': '../character_template/images/archer.png'
    },
    'Ассасин': {
        'skills': classes_skills['Ассасин'],
        'stats': {
            'luck': 15,
        },
        'image': '../character_template/images/assasin.png'
    },
    'Бард': {
        'skills': classes_skills['Бард'],
        'stats': {
            'temper': 15
        },
        'image': '../character_template/images/bard.webp'
    }
}

env = Environment(
    loader=FileSystemLoader('../character_template'),
    autoescape=select_autoescape(['html'])
)
template = env.get_template('template.html')


def get_race():
    for i, race in enumerate(characters_list, 1):
        print(f"{i}. {race}")
    choice = int(input("Выберите расу персонажа: "))
    character_race = characters_list[choice - 1]
    return character_race


def get_class():
    for i, cls in enumerate(character_classes, 1):
        print(f"{i}. {cls}")
    choice = int(input("Выберите класс персонажа: "))
    character_class = character_classes[choice - 1]
    return character_class


def get_stats():
    stats = {
        'strength': random.randint(1, 3),
        'agility': random.randint(1, 3),
        'intelligence': random.randint(1, 3),
        'luck': random.randint(1, 3),
        'temper': random.randint(1, 3)
    }
    return stats


def get_classbaff(character_class, classes_base, stats):
    bonus = classes_base[character_class]['stats']
    bonus_attr = list(bonus.keys())[0]
    stats[bonus_attr] = bonus[bonus_attr]
    return stats


def get_yourbaff(character_class, classes_base):
    bonus_attrib = list(classes_base[character_class]['stats'])[0]
    print(f"Повышен аттрибутЖ {bonus_attrib}")


def get_skills(character_class, classes_base):
    skills = random.sample(classes_base[character_class]['skills'], 3)
    first_skill, second_skill, third_skill = skills
    return first_skill, second_skill, third_skill

    
def main():
    char_num = int(input("Сколько персонажей создать?(числом): "))
    for i in range(char_num):
     name = input("Введите имя персонажа: ").strip()
     character_race = get_race()
     print(f"Вы выбрали: {character_race}")
     character_class = get_class()
     print(f"Вы выбрали: {character_class}")
     stats = get_stats()
     stats = get_classbaff(character_class, classes_base, stats)
     get_yourbaff(character_class, classes_base)
     image = classes_base[character_class]['image']
     first_skill, second_skill, third_skill = get_skills(character_class, classes_base)
     rendered_page = template.render(
        name=name, 
        race=character_race,
        character_class=character_class,
        strength=stats['strength'],
        agility=stats['agility'],
        intelligence=stats['intelligence'],
        luck=stats['luck'],
        temper=stats['temper'],
        image=image,
        first_skill=first_skill,
        second_skill=second_skill,
        third_skill=third_skill
     )
    
     with open(f'../characters/index{i+1}.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)


if __name__ == '__main__':
    main()
