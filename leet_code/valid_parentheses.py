def isValid(s: str) -> bool:

    if len(s) == 0:
        return True
    if len(s) % 2 == 1:
        return False

    stack = []

    for char in s:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
        if char == ")" or char == "}" or char == "]":
            if not stack:
                return False
            temp = stack.pop()
            if char == "}" and temp != "{":
                return False
            if char == ")" and temp != "(":
                return False
            if char == "]" and temp != "[":
                return False

    if not stack:
        return True


class Solution:
    pass
