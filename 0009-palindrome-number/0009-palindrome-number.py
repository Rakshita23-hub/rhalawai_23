class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp=x
        rev_num=0
       
        while temp > 0:
            rev_num =rev_num * 10+ temp % 10
            temp=temp//10

        return rev_num == x
        