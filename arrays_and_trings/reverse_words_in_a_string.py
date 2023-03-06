from collections import deque

class Approach2:
    def trim_spaces(self, s: str, space: str) -> list:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == space:
            left += 1

        while left <= right and s[right] == space:
            right -= 1

        l = []
        while left <= right:
            if s[left] != space or l[-1] != space:
                l.append(s[left])
            left += 1
        return l

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list, space: str) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            while end < n and l[end] != space:
                end += 1
            self.reverse(l=l, left=start, right=end - 1)
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:
        space = " "
        l = self.trim_spaces(s=s, space=space)
        self.reverse(l, left=0, right=len(l) - 1)
        self.reverse_each_word(l, space=space)
        return "".join(l)


class Approach3:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == " ":
            left += 1
        while left <= right and s[right] == " ":
            right -= 1
        d, word = deque(), []
        while left <= right:
            s_left = s[left]
            if s_left == " " and word:
                d.appendleft("".join(word))
                word = []
            elif s_left != " ":
                word.append(s_left)
            left += 1

        d.appendleft("".join(word))
        return " ".join(d)


test_cases = {
    "1": {"input": "a good   example", "output": "example good a"},
    "2": {"input": "the sky is blue", "output": "blue is sky the"},
    "3": {"input": "  hello world  ", "output": "world hello"}
}
if __name__ == '__main__':
    # Approach2
    solution = Approach2()
    reversed_s = solution.reverseWords(s=test_cases["1"]["input"])
    assert reversed_s == test_cases["1"]["output"]

    reversed_s = solution.reverseWords(s=test_cases["2"]["input"])
    assert reversed_s == test_cases["2"]["output"]

    reversed_s = solution.reverseWords(s=test_cases["3"]["input"])
    assert reversed_s == test_cases["3"]["output"]
    # Approach3
    solution = Approach3()
    reversed_s = solution.reverseWords(s=test_cases["1"]["input"])
    assert reversed_s == test_cases["1"]["output"]

    reversed_s = solution.reverseWords(s=test_cases["2"]["input"])
    assert reversed_s == test_cases["2"]["output"]

    reversed_s = solution.reverseWords(s=test_cases["3"]["input"])
    assert reversed_s == test_cases["3"]["output"]

