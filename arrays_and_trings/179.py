"""
Valid Parentheses

An input string is valid if:

    * Open brackets must be closed by the same type of brackets.
    * Open brackets must be closed in the correct order.
    * Every close bracket has a corresponding open bracket of the same type.
"""


def is_valid(chars: str) -> bool:
    map_parentheses = {"[": "]", "{": "}", "(": ")"}
    stack = []
    for char in chars:
        if char in map_parentheses:
            stack.append(char)
        else:
            top_bracket = stack.pop()
            if map_parentheses[top_bracket] != char:
                return False
    return not stack


if __name__ == '__main__':
    assert is_valid("()")
    assert is_valid("()[]{}")
    assert not is_valid("(]")
    assert not is_valid("(((((((((()")
