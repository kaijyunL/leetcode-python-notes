class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        is_negative = x < 0
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10
            
            if is_negative:
                if res > (2**31 - digit) // 10:
                    return 0
            else:
                if res > (2**31 - 1 - digit) // 10:
                    return 0
            
            res = res * 10 + digit
            
        return -res if is_negative else res
