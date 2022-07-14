class Solution:
    def intToRoman(self, nums: int) -> str:
        valores = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romanos = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        roman = ""
        for i in range(len(valores)):
            while nums >= valores[i]:
                roman += romanos[i]
                nums -= valores[i]
        return roman
