class Solution:
    def reverse(self, x: int) -> int:
        strng = str(x)
        negative = False
        if strng[0] == "-":
            negative = True
            
        if negative == True:
            return int(strng[1::-1])*(-1)
        else:
            return int(strng[::-1])