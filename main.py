from random import randint
from graphic_arts.start_game_banner import run_screensaver

DEFAULT_ATTACK: int = 5
DEFAULT_DEFENCE: int = 10
DEFAULT_STAMINA: int = 80


class Character:
    """Общее описание класса. Базовые навыки для всех персонажей."""
    BRIEFF_DESC_CHAR_CLASS: str = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK: tuple[int, int] = (1, 3)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (1, 5)
    SPECIAL_SKILL: str = 'Удача'
    SPECIAL_BUFF: int = 15

    def __init__(self, name):
        self.name = name

    def attack(self) -> str:
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    def defence(self) -> str:
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона')

    def special(self) -> str:
        return (f'{self.name} применил специальное умение '
                f'{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}.')

    def __str__(self) -> str:
        return f'{self.__class__.__name__} - {self.BRIEFF_DESC_CHAR_CLASS}'


class Warrior(Character):
    """Класс воина. Навыки и способности воина."""
    BRIEFF_DESC_CHAR_CLASS: str = (' дерзкий воин ближнего боя. '
                                   'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK: tuple[int, int] = (3, 5)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (5, 10)
    SPECIAL_BUFF: int = DEFAULT_STAMINA + 25
    SPECIAL_SKILL: str = 'Выносливость'


class Mage(Character):
    """Класс мага.Навыки и способности мага."""
    BRIEFF_DESC_CHAR_CLASS: str = (' находчивый воин дальнего боя. '
                                   'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK: tuple[int, int] = (5, 10)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (-2, 2)
    SPECIAL_BUFF: int = DEFAULT_ATTACK + 40
    SPECIAL_SKILL: str = 'Атака'


class Healer(Character):
    """Класс лекаря. Навыки и способности лекаря"""
    BRIEFF_DESC_CHAR_CLASS: str = (' могущественный заклинатель. '
                                   'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK: tuple[int, int] = (-3, -1)
    RANGE_VALUE_DEFENCE: tuple[int, int] = (2, 5)
    SPECIAL_BUFF: int = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL: str = 'Защита'


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа
    """
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    approve_choice: str = ''

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель - warrior, '
                               'Маг - mage, Лекарь - healer ')
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(char_class: Character) -> str:
    """Основная функция тренировки."""
    commands: dict = {'attack': Character.attack(char_class),
                      'defence': Character.defence(char_class),
                      'special': Character.special(char_class)}
    print('Потренируйся управлять своими навыками.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи одну из команд: '
                    'attack — чтобы атаковать противника, '
                    'defence — чтобы блокировать атаку противника, '
                    'special — чтобы использовать свою суперсилу. '
                    'Если не хочешь тренироваться, введи команду skip. ')
        if cmd in commands:
            print(commands[cmd])
    return 'Тренировка окончена.'


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: Character = choice_char_class(char_name)

    print(start_training(char_class))
