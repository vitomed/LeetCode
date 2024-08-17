# Реализованы аналоги стандартных функций языка для работы со списками.
# Нужно оценить, насколько быстрые эти реализации, и предложить возможные пути их оптимизации (без использования стандартных функций Python).
from typing import Generic, Iterable, List, TypeVar

T = TypeVar('T')


class IterTools(Generic[T]):
    def revert(self, source: List[T]) -> List[T]:
        result: List[T] = []
        for element in source:
            result.insert(0, element)
        return result

    def _revert(self, source):
        return source[::-1]

    def except_values(self, source: List[T], excepted: List[T] = []) -> Iterable[T]:
        for v in source:
            try:
                if excepted.index(v):
                    continue
            except ValueError:
                yield v

    def distinct(self, source: List[T]) -> List[T]:
        result: List[T] = []

        for item in source:
            contains: bool = False
            for e in result:
                if e == item:
                    contains = True
                    break
            if not contains:
                result.append(item)

        return result


it = IterTools[int]()
print(it.revert([1, 2, 3]))
# [3, 2, 1]
print(list(it.except_values([1, 2, 3, 4, 5, 6, 7], [2, 4, 7])))
# [1, 3, 5, 6]
print(it.distinct([1, 2, 2, 3, 4, 5, 7, 6, 5, 10, 1, 7, 8]))
# [1, 2, 3, 4, 5, 7, 6, 10, 8]