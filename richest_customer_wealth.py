class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for i in accounts:
            if maxi<sum(i):
                maxi = sum(i)
        return maxi