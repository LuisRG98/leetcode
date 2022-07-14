class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)[::-1]
        return(n==str(x))