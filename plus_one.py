class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n =""
        for i in digits:
            n +=str(i)
        s = str(int(n)+1)
        return [x for x in s]