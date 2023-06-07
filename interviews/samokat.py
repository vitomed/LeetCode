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
