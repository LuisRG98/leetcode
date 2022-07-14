class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        suma = 0
        l2 = []
        for i in nums:
            suma+=i
            l2.append(suma)
        return l2