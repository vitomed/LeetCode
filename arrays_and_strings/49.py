"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""
import collections


def group_anagrams(arr: list) -> list:
    """
    Time Complexity: O(N*K*logK), where N is the length of `strs`, and K is the maximum length of a string in `strs`.
    The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(K*logK) time.

    Space Complexity: O(NK), the total information content stored in `ans`.
    """
    m = collections.defaultdict(list)
    for item in arr:
        m[tuple(sorted(item))].append(item)
    for sub_array in m.values():
        sub_array.sort()
    answer = list(m.values())[::-1]
    return answer


if __name__ == '__main__':
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["bat"], ["nat", "tan"],
                                                                          ["ate", "eat", "tea"]]
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
