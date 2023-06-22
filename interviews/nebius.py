"""
добавление
удаление
и получение уникального элемента

add(x) - add element `x` to the structure
get_unique() - return some element that is uniquely represented in the structure
delete(x) - remove element `x` from the structure

Доп условие: все операции должна работать за O(1), что будет при добавлении 2 раза и удалении 3
"""


class UniqueStructure:
    def __init__(self):
        self.elements = {}
        self.unique = set()

    def add(self, x):
        if x in self.elements:
            self.elements[x] += 1
            self.unique.discard(x)
        else:
            self.elements[x] = 1
            self.unique.add(x)

    def delete(self, x):
        if x in self.elements:
            self.elements[x] -= 1
            self.unique.discard(x)

    def get_unique(self):
        return next(iter(self.unique), None)