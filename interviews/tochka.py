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