class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=''.join(ch for ch in s if ch.isalnum())

    
        if s[ : :-1]==s:
            return True
        return False
        