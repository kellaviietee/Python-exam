"""Exam2 (06.01)."""
from enum import Enum


def sum_of_digits(s: str) -> int:
    """
    Return sum of all the digits.

    The input string contains different symbols.
    Sum all the digits.
    sum_of_digits("123") => 6
    sum_of_digits("a") => 0
    sum_of_digits("") => 0
    sum_of_digits("1-2-3-99") => 24
    """
    pass


def range_with_count(start: int, stop: int, count: int) -> list:
    """
    Return list from start to stop with number total values in the list.

    count >= 1

    range_with_count(1, 5, 1) -> [1.0]
    range_with_count(1, 5, 2) -> [1.0, 5.0]
    range_with_count(1, 5, 3) -> [1.0, 3.0, 5.0]
    range_with_count(1, 5, 4) -> [1.0, 2.333333333333333, 3.6666666666666665, 5.0]
    range_with_count(1, 5, 5) -> [1.0, 2.0, 3.0, 4.0, 5.0]
    range_with_count(5, 1, 5) -> [5.0, 4.0, 3.0, 2.0, 1.0]
    """
    pass


def add_symbols(string: str, symbols: str) -> str:
    """
    Return given string with added symbols where needed.

    If letter in string exists in symbols, double it in result.
    If number in string exists in symbols, triple it in result.

    It does not change the result when any symbol appears more than once in symbols.

    add_symbols("ab12", "b12a") -> "aabb111222"
    add_symbols("xyz", "xxxxxx") -> "xxyz"
    add_symbols("aaaa", "b") -> "aaaa"
    add_symbols("aab", "a") -> "aaaab"
    """
    pass


def h_index(articles: list) -> int:
    """
    Given a list where each value represents the times of citations of one article.

    Return an h index of the person.

    H-index is the largest number such that a number of publications
    have at least the same number of citations.

    Examples:
    [4, 2, 4] => 2
    [1, 2, 2] => 2
    [] => 0
    [1, 1, 1, 1] => 1
    [3, 5, 7] => 3
    [2, 5, 7] => 2
    [5, 4, 7, 3, 6] => 4
    """
    pass


def count_pairs(s: str) -> int:
    """
    Count pairs in string.

    We'll say that a "pair" in a string is two instances of a char separated by a char.
    So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x.
    Recursively compute the number of pairs in the given string.

    count_pairs("axa") => 1
    count_pairs("aa") => 0
    count_pairs("axax") => 2
    count_pairs("axbx") => 1
    """
    pass


def valid_parentheses(sequence: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

    Example 1:
    Input: sequence = "()"
    Output: true


    Example 2:
    Input: sequence = "()[]{}"
    Output: true

    Example 3:
    Input: sequence = "(]"
    Output: false

    Example 4:
    Input: sequence = "([)]"
    Output: false

    Example 5:
    Input: sequence = "{[]}"
    Output: true

    :return boolean whether sequence is valid or not
    """
    pass


class Donut:
    """Donut class."""

    def __init__(self, filling: str, icing: str):
        """
        Donut class constructor.

        :param icing: donut icing
        :param filling: donut filling
        """
        self.filling = filling
        self.icing = icing


class DonutFactory:
    """DonutFactory class."""

    def __init__(self):
        """DonutFactory class constructor."""
        pass

    def add_donuts(self, donuts: list):
        """
        Add list of fresh donuts to already existing ones.

        :param donuts: list of donuts to add
        :return:
        """
        pass

    def get_donuts(self) -> list:
        """
        Return list of all donuts present on the line at the moment.

        :return: list of all donuts
        """
        pass

    def pack_donuts_by_filling_and_icing(self) -> dict:
        """
        Method should return dict with donuts divided by filling and icing.

        Dict key must be represented as tuple of filling and icing and value as list of donuts with
        given filling and icing.
        {(filling, icing): [donut1, donut2]}

        After packing, the production line for donuts should be empty (everything is packed).

        :return: dict
        """
        pass

    def sort_donuts_by_icing_and_filling(self) -> list:
        """
        Method should return list of donuts sorted by icing in alphabetical order and then by filling in alphabetical order.

        :return: sorted list of donuts
        """
        pass

    def get_most_popular_donut(self) -> dict:
        """
        Method should return dict with icing and filling of the most popular donut.

        {'icing': most_pop_donut_icing, 'filling': most_pop_donut_filling}
        If there are several icing-filling combinations with the same amount of donuts,
        use the one which icing is alphabetically lower (a comes before b).

        :return: dict with icing and filling of most pop donut
        """
        pass

    def get_donuts_by_flavour(self, flavour: str) -> list:
        """
        Get list of donuts that have the same icing or filling as given in method parameter.

        :return: list of donuts with the given flavour.
        """
        pass


class Species(Enum):
    """Different species."""

    Dragon = 1
    Vampire = 2
    Beast = 3


class Monster:
    """Monster class."""

    def __init__(self, species: Species, bounty: int):
        """Constructor."""
        pass

    def get_species(self) -> Species:
        """Return the species of the monster."""
        pass

    def get_bounty(self) -> int:
        """Return the bounty for this monster."""
        pass

    def is_alive(self) -> bool:
        """Whether the monster is alive."""
        pass

    def slay(self) -> bool:
        """
        Slay the monster.

        If monster is already dead, return False.
        Otherwise kill the monster and return True.
        """
        pass

    def __repr__(self) -> str:
        """
        Return string representation.

        "A {species} worth {bounty} coins"
        """
        pass


class Village:
    """
    Village class.

    Village starts with 100 money and 0 age.
    Each day population is lowered by 1 for each monster in the village.
    Population cannot be lower than 0.
    If the population is 0, witcher cannot work there.
    """

    def __init__(self, name: str, initial_population: int):
        """Constructor."""
        pass

    def get_name(self) -> str:
        """Return name of the village."""
        pass

    def get_population(self) -> int:
        """Return population of the village."""
        pass

    def get_monsters(self) -> list:
        """
        Return a list of monsters bothering the village.

        If there are no population, no monsters are not bothering the village.
        """
        pass

    def add_monster(self, monster: Monster) -> None:
        """Add monster to the village."""
        pass

    def add_money(self, amount) -> None:
        """Add money to the village."""
        pass

    def advance_day(self) -> None:
        """
        Advance time by one day.

        The age of the village is increased by one.
        """
        pass

    def pay(self, amount: int) -> bool:
        """
        Pay the required amount.

        If the village does not have enough money, return False.
        Otherwise spend the amount and return True.
        """
        pass

    def __repr__(self) -> str:
        """
        Return string representation of the village.

        "{name}, population {population}, age {age}"
        """
        pass


class Witcher:
    """
    Witcher class.

    Witcher starts with 0 money.
    """

    def __init__(self, name: str, school: str):
        """Constructor."""
        pass

    def get_money(self) -> int:
        """Return the amount of money the witcher has."""
        pass

    def get_slain(self) -> list:
        """Return a list of slain monsters in the order they are slain."""
        pass

    def get_hunted_species(self) -> list:
        """
        Return a list of Species objects of the slain monsters ordered alphabetically.

        Each value should be in the list once, so there can be max 3 objects in the result.
        """
        pass

    def hunt_most_expensive(self, village: Village) -> bool:
        """
        Hunt the most expensive monster.

        Try to hunt the most expensive monster (the one who has the highest bounty) in the given village.
        The monster is slain and then the village tries to pay the witcher.
        If there is a monster to kill and the village can pay the money, return True.
        Otherwise return False.
        The monster is slain even if there is no money to pay.
        """
        pass

    def __repr__(self) -> str:
        """
        Return string representation.

        "{name} of {school} school with {number of monsters} monsters slain"
        """
        pass


if __name__ == '__main__':
    assert sum_of_digits("123") == 6
    assert sum_of_digits("") == 0

    assert range_with_count(1, 5, 2) == [1.0, 5.0]
    assert range_with_count(5, 1, 5) == [5.0, 4.0, 3.0, 2.0, 1.0]

    assert add_symbols("aab", "a") == "aaaab"
    assert add_symbols("aab1", "a12") == "aaaab111"

    assert h_index([4, 2, 4]) == 2
    assert h_index([5, 4, 7, 3, 6]) == 4

    assert valid_parentheses("()") is True
    assert valid_parentheses("[[") is False
    assert valid_parentheses("[(])") is False

    assert count_pairs("axa") == 1
    assert count_pairs("axaxa") == 3
    assert count_pairs("") == 0

    # donut examples

    donut_factory = DonutFactory()
    donut1 = Donut('chocolate', 'sugar')
    donut2 = Donut('caramel', 'chocolate')
    donut3 = Donut('cherry', 'marshmallow')
    donut4 = Donut('chocolate', 'sugar')
    donut5 = Donut('vanilla', 'cream')
    donut6 = Donut('vanilla', 'cream')
    donut7 = Donut('cherry', 'marshmallow')
    donut8 = Donut('chocolate', 'sugar')

    donuts = [donut1, donut2, donut3, donut4, donut5, donut6, donut7, donut8]

    donut_factory.add_donuts(donuts)

    print(donut_factory.get_donuts_by_flavour('marshmallow'))  # [donut3, donut7]
    print(donut_factory.get_most_popular_donut())  # {icing: sugar, filling: chocolate}
    print(donut_factory.pack_donuts_by_filling_and_icing())  # {(chocolate, sugar): [donut1, donut4, donut8],
    #                                                               (caramel, chocolate): [donut2],
    #                                                               (cherry, marshmallow): [donut3, donut7],
    #                                                               (vanilla, cream): [donut5, donut6]}
    print(donut_factory.sort_donuts_by_icing_and_filling())  # [donut2, donut5, donut6, donut3, donut7, donut1,
    #                                                           donut4, donut8]

    # Witcher
    tallinn = Village("Tallinn", 7)
    godzilla_species = Species.Beast
    godzilla = Monster(godzilla_species, 200)
    print(godzilla.get_species() == Species.Beast)   # True
    print(str(godzilla.get_species()))   # Species.Beast
    modzilla = Monster(Species.Dragon, 200)
    dracula = Monster(Species.Vampire, 100)
    frankenstein = Monster(Species.Beast, 300)
    tallinn.add_monster(godzilla)
    tallinn.add_monster(modzilla)
    tallinn.add_monster(dracula)
    tallinn.add_monster(frankenstein)

    print(tallinn.get_population())  # 7
    tallinn.advance_day()
    tallinn.add_money(500)
    print(tallinn.get_population())  # 3
    ago = Witcher("Ago", "TalTech")
    print(ago.hunt_most_expensive(tallinn))  # True
    print(ago.get_money())  # 300
    print(tallinn.get_monsters())   # [A Beast worth 200 coins, A Dragon worth 200 coins, A Vampire worth 100 coins]
    print(ago.hunt_most_expensive(tallinn))  # True
    print(ago.get_money())  # 500
    print(tallinn.get_monsters())   # [A Dragon worth 200 coins, A Vampire worth 100 coins]
    print(ago.hunt_most_expensive(tallinn))  # False
    print(ago.get_money())  # 500
    print(ago.hunt_most_expensive(tallinn))  # True
    print(tallinn.get_monsters())   # []

    print(ago.get_hunted_species())  # [<Species.Beast: 3>, <Species.Dragon: 1>, <Species.Vampire: 2>]
    print(ago.get_hunted_species()[0] == Species.Beast)   # True

    # enum examples
    species_list = [Species.Beast, Species.Vampire, Species.Beast]
    print(species_list[0] == species_list[1])   # False
    print(species_list[0] == species_list[2])   # True
