# Метод реализовывать не нужно
def is_version_correct(ver_num: int) -> bool:
    if ver_num == 3:
        return True
    return False


# Метод который нужно реализовать
def get_bad_version(last_ver_num: int) -> int:
    left = 1
    right = last_ver_num

    if left < right:
        while left < right:
            mid = left + (right - left) // 2
            if is_version_correct(mid):
                left = mid + 1
            else:
                right = mid

    if is_version_correct(left):
        return -1

    return left


get_bad_version(4)
get_bad_version(5)

import random
from collections import Counter

# Балансировщик.
# Есть множество серверов с различной производительностью и на них поступают запросы от пользователей.
# Требуется написать класс, который будет для каждого нового запроса определять на какой сервер его стоит переотправить,
# так чтобы сервера получили долю трафика пропорциональную их производительностям.
# считаем, что запросов очень много


class LoadBalancer:
  def __init__(self, servers):
    self.servers = servers
    self.last_server = None
    self.counter = Counter()

  def get_server(self):
    totla_capacity = sum(server["capacity"] for server in self.servers)
    rand_num = random.uniform(0, totla_capacity)
    cumulative_sum = 0

    for server in self.servers:
      cumulative_sum += server["capacity"]
      if cumulative_sum > rand_num:
        self.last_server = server["name"]
        self.counter[self.last_server] += 1
        return server["name"]
