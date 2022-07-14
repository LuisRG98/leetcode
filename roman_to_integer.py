class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n = len(s)-1
        suma = dic[s[n]]
        for i in range(n-1,-1,-1):
            if dic[s[i]] >= dic[s[i+1]]:
                suma +=dic[s[i]]
            else:
                suma -=dic[s[i]]
        return(suma)