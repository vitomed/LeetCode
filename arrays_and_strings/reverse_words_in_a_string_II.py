class Solution1:
    def reverse(self, l: list, left: int, right: int):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverseWords(self, l: list):
        left, right = 0, len(l)
        self.reverse(l, left=left, right=right - 1)

        n = len(l)
        start = end = 0
        while start < n:
            while end < n and l[end] != " ":
                end += 1
            self.reverse(l=l, left=start, right=end - 1)
            start = end + 1
            end += 1

        return l


test_cases = [
    (
        ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"],
        ["b", "l", "u", "e", " ", "i", "s", " ", "s", "k", "y", " ", "t", "h", "e"]
    ),
    (
        ["a"],
        ["a"]
    )
]
if __name__ == '__main__':
    solution = Solution1()

    for test_case in test_cases:
        assert solution.reverseWords(test_case[0]) == test_case[1]
