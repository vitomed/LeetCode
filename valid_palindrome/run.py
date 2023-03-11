def is_palindrome(s: str):
    left_point, right_point = 0, len(s) - 1
    while left_point < right_point:
        while left_point < right_point and not s[left_point].isalnum():
            left_point += 1
        while left_point < right_point and not s[right_point].isalnum():
            right_point -= 1

        if s[right_point].lower() != s[left_point].lower():
            return False

        left_point += 1
        right_point -= 1

    return True


if __name__ == '__main__':
    assert is_palindrome(s='A man, a plan, a canal: Panama')
