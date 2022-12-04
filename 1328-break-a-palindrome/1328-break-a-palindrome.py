class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: return ''
        palindrome = list(palindrome)
        
        for i, x in enumerate(palindrome):
            if (temp:=palindrome[i]) != "a":
                palindrome[i] = "a"
                if palindrome != palindrome[::-1]:
                    return "".join(palindrome)
                palindrome[i] = temp
        palindrome[-1] = "b"
        return "".join(palindrome)