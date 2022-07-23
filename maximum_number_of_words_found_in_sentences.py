class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = [len(x.split(' ')) for x in sentences]
        return max(res)
            