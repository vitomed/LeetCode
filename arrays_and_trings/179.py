"""
Valid Parentheses

An input string is valid if:

    * Open brackets must be closed by the same type of brackets.
    * Open brackets must be closed in the correct order.
    * Every close bracket has a corresponding open bracket of the same type.
"""


def is_valid(arr: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for element in arr:
        if element in mapping:
            top_element = stack.pop() if stack else "#"

            if mapping[element] != top_element:
                return False

        else:
            stack.append(element)

    return not stack


if __name__ == '__main__':
    assert is_valid("()")
    assert is_valid("()[]{}")
    assert not is_valid("(]")
    assert not is_valid("(((((((((()")
