class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        strng1 = str(x)
        strng2 = ""
        
        if strng1[0] == "-":
            return False
        
        else: 
            strng2 = strng1[::-1]
            if strng1 == strng2:
                return True
            else:
                return False