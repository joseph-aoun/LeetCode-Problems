class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: return ''
        palindrome = list(palindrome)
        
        for i in range(len(palindrome)//2):
            if i >= len(palindrome)//2: break
            if palindrome[i] != "a":
                palindrome[i] = "a"
                return "".join(palindrome)
        palindrome[-1] = "b"
        return "".join(palindrome)