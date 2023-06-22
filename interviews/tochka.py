#!/usr/bin/python3.8
import logging
from typing import Dict, Optional


class InvalidFileFormat(IOError):
    pass

from collections import defaultdict

def get_api_stats() -> Optional[Dict[int, int]]:
    """Парсит логи вебсервера и считает кол-во ответов с разными HTTP статусами
    Пример записи лога:
    2020-10-02 01:43:43,138 [INFO] [e4a16bf8] server.api: "GET /swagger/?format=openapi HTTP/1.1" 200 111905
    """
    log_file = "/var/log/app/access.log"
    codes = defaultdict(int)

    try:
        with open(log_file, encoding="utf-8") as f:

            for line in f:
                line_splitted = line.split()
                http_status = line_splitted[-2]

                if not (100 <= int(http_status) <= 599):
                    raise InvalidFileFormat('Http status not in the range')
                codes[http_status] += 1

        return dict(
            sorted(codes.items(),
            key=lambda x: x[1],
            reverse=True)
            )

    except IOError as e:
        logging.error(
            'Something went wrong while oppening log: %s', str(e))
    except InvalidFileFormat as e:
        logging.error('Invalid log file: %s', str(e))
        raise

    return None


print(get_api_stats())

if get_api_stats() is None:
    logging.info("empty file")


def get_api_stats():
    ...

def check_stats():
    ...

def count_stats():
    ...

# counter
# упадет при int(http_status)
# разделение ответственности


# 2
# принимает список и отдает список строк
# async def download(urls: list) -> list[str]:
# чтобы сделал чтобы можно было качать ограничение на количество подлкючений нужно добавить Семафор
# Семафоры позволяют ограничить доступ к ресурсам определенным числом потоков или задач
import aiohttp
import asyncio


async def download(urls: list, max_connections: int) -> list[str]:
    async with aiohttp.ClientSession() as session:
        semaphore = asyncio.Semaphore(max_connections)
        tasks = []
        for url in urls:
            tasks.append(download_url(session, url, semaphore))
        results = await asyncio.gather(*tasks)
        return results

async def download_url(session, url, semaphore):
    async with semaphore:
        async with session.get(url) as response:
            text = await response.text()
            return text

urls = ["http://example.com", "http://example.org", "http://example.net"]
result = asyncio.run(download(urls, 2))
print(result)


#напиши классы модели  для базы данных
"""
Клиенты (инн, фио)
Счета (чей счет, номер счета)
Платежи (откуда, куда, сколько, когда)
"""

class Client:
    id = Column(int)
    inn = Column(string)
    fio = Column(string)

class Account:
    id = Column(int)
    colient_id = Column(int)
    number = Column(str)


class Payment:
    id = Column(int)
    from_account_id = Column(int)
    to_account_id = Column(int)
    amount = Column(int)
    data = Column(datetime)
"""
Если в базе данных установлено ограничение Foreign Key Constraint (FK) 
для столбцов from_account_id и to_account_id в таблице payment,

на что мы можем расчитывать если есть этот тип ограничение
и сработает ли этот запрос:

insert into payment values from_account_id = 123, to_account_id = 345, ...;
"""

# без нормализации

"""
Для получения 10 самых крупных счетов можно использовать следующий SQL-запрос:

SELECT number, SUM(amount) AS total_amount
FROM Account
JOIN Payment ON Account.id = Payment.from_account_id
GROUP BY Account.id, Account.number
ORDER BY total_amount DESC
LIMIT 10;
"""

# после денормалзации

class Client:
    id = Column(int)
    inn = Column(string)
    fio = Column(string)

class Account:
    id = Column(int)
    colient_id = Column(int)
    number = Column(str)
    amount = Column(Integer)


class Payment:
    id = Column(int)
    from_account_id = Column(int)
    to_account_id = Column(int)
    amount = Column(int)
    data = Column(datetime)

"""
Для получения 10 самых крупных счетов можно использовать следующий SQL-запрос:

SELECT number, amount
FROM Account
ORDER BY amount DESC
LIMIT 10;
"""