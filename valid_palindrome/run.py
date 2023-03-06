def isPalindrome(s: str) -> bool:
    start, finish = 0, len(s) - 1
    while start < finish:
        while start < finish and not s[start].isalnum():
            start += 1
        while start < finish and not s[finish].isalnum():
            finish -= 1
        if s[start].lower() != s[finish].lower():
            return False

        start += 1
        finish -= 1

    return True


def checkPalindrome(s: str):
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
    checkPalindrome(s='A man, a plan, a canal: Panama')