class Solution:
    def isValid(self, s: str) -> bool:
        lista = []
        for i in s:
            if i in ['[','(','{']:
                lista.append(i)
            elif i == ')' and len(lista)!=0 and lista[-1] =='(':
                lista.pop()
            elif i == '}' and len(lista)!=0 and lista[-1] =='{':
                lista.pop()
            elif i == ']' and len(lista)!=0 and lista[-1] =='[':
                lista.pop()
            else:
                return False
        return lista == []