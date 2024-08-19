import re
import cProfile
import pstats
import io


def without_compilation(strings):
    """Функция без предварительной компиляции регулярного выражения"""

    def is_valid_email(email):
        return bool(re.fullmatch(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$", email))

    return [email for email in strings if is_valid_email(email)]


def with_compilation(strings):
    """Функция с предварительной компиляцией регулярного выражения"""
    valid_email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")

    def is_valid_email(email):
        return bool(valid_email_regex.fullmatch(email))

    return [email for email in strings if is_valid_email(email)]


def run_profiling():
    # Пример списка email'ов для тестирования
    emails = ["test@example.com", "invalid_email@", "another.test@domain.com", "wrong@.com"] * 1000

    # Профилирование функции без компиляции регулярного выражения
    pr = cProfile.Profile()
    pr.enable()
    without_compilation(emails)
    pr.disable()

    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.TIME)
    ps.print_stats()
    print("Without Compilation:")
    print(s.getvalue())  # Вывод результатов профилирования для функции без компиляции

    # Профилирование функции с компиляцией регулярного выражения
    pr = cProfile.Profile()
    pr.enable()
    with_compilation(emails)
    pr.disable()

    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.TIME)
    ps.print_stats()
    print("With Compilation:")
    print(s.getvalue())  # Вывод результатов профилирования для функции с компиляцией


# Запуск профилирования
run_profiling()
