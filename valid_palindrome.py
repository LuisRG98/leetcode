class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if not i.isalnum():
                s = s.replace(i,"")
        
        s2 = s.lower()
        return s2[::-1] == s2