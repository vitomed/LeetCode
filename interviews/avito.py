'''
Вещи
    Одежда
        Мужская
        Женская
Хобби
    Велосипеды
        Горные
    Мангалы
Транспорт

Вещи => Одежда => Мужская
Вещи => Одежда => Женская
Хобби => Велосипеды => Горные
Хобби => Мангалы
Транспорт

class Node {
    text: string
    children: [Node,]
}

Входные параметры
массив нод первого уровня [Вещи, Хобби, Транспорт]
'''

class Node:
    def __init__(self, text, children=[]):
        self.text = text
        self.children = children

def print_paths(node, path=[]):
    path = path + [node.text]
    if len(node.children) == 0:
        print(" => ".join(path))
    else:
        for child in node.children:
            print_paths(child, path)

nodes = [
    Node("Вещи", [
        Node("Одежда", [
            Node("Мужская"),
            Node("Женская")
        ])
    ]),
    Node("Хобби", [
        Node("Велосипеды", [
            Node("Горные")
        ]),
        Node("Мангалы")
    ]),
    Node("Транспорт")
]

if __name__ == '__main__':
    for node in nodes:
        print_paths(node)
