from typing import List


def reverse(x: int) -> int:
    result = 0
    is_negative = False
    if x < 0:
        is_negative = True
        x = x * -1
    if x == 2 ** 31:
        return 0
    while x > 0:
        if result > 214748364:
            return 0
        elif result == 214748364:
            if int(x % 10) > 8 or (int(x % 10) == 7 and is_negative == True):
                return 0
        result = result * 10 + int(x % 10)
        print(result)
        print(x)
        x = int(x / 10)
    if is_negative:
        result = result * -1

    return result
