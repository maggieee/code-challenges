class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if s == "":
            return True
        
        lst = []
        
        for i in s.lower():
            if i.isalnum() is True:
                lst.append(i)
                
        if lst == lst[::-1]:
            return True
        
        else:
            return False