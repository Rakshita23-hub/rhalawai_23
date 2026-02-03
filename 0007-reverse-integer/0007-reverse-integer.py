class Solution:
    def reverse(self, x: int) -> int:

        rev = 0
        if x < 0:
            sign = -1
        else:
            sign = 1
        
        x = abs(x)  #absolute abs(-123)=123

        while x != 0:
            digit = x % 10
            x = x // 10
            rev = rev * 10 + digit

        rev = sign * rev

        if rev < -2**31 or rev > 2**31 - 1:
            return 0  #if rev is goes outside of 32 range it will return 0

        return rev

        
        