"""
Код работает корректно и полностью решает задачу, но после ревью TeamLead`а остались комментарии о том, что его можно ускорить минимум в 2 раза, буквально поменяв две строчки, а какие он не сказал – лишь оставил ссылку на страницу про регулярные выражения в Python в качестве подсказки.
Используя dis
"""
import dis
import re
import timeit
import cProfile

from typing import List


def valid_emails_without_compilation(strings: List[str]) -> List[str]:
    valid_email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

    def is_valid_email(email: str) -> bool:
        return bool(re.fullmatch(valid_email_regex, email))

    emails = []
    for email in strings:
        if is_valid_email(email):
            emails.append(email)

    return emails


def valid_emails_with_compilation(strings: List[str]) -> List[str]:
    valid_email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")

    def is_valid_email(email: str) -> bool:
        return bool(valid_email_regex.fullmatch(email))

    emails = []
    for email in strings:
        if is_valid_email(email):
            emails.append(email)

    return emails


if __name__ == '__main__':
    print(dis.dis(valid_emails_without_compilation))
    print(dis.dis(valid_emails_with_compilation))
    emails = ["test@example.com"]

    with cProfile.Profile() as pr:
        valid_emails_without_compilation(emails)
        pr.print_stats()
    print("Без компиляции:", timeit.timeit(lambda: valid_emails_without_compilation(emails), number=100))
    with cProfile.Profile() as pr:
        valid_emails_with_compilation(emails)
        pr.print_stats()
    print("С компиляцией:", timeit.timeit(lambda: valid_emails_with_compilation(emails), number=100))
