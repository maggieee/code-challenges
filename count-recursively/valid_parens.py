Given a string S of '(' and ')' parentheses, we add the minimum number of 
parentheses ( '(' or ')', and in any positions ) so that the resulting 
parentheses string is valid.

Given a parentheses string, return the minimum number of parentheses 
we must add to make the resulting string valid.

Input: "())"
Output: 1

Input: "((("
Output: 3

Input: "()"
Output: 0

Input: "()))(("
Output: 4

Input: "(()())"
Output: 0

Input: ")))"
Output: 3
"""

# loop through the string
# if you come across an open paren, add to the stack
# if you come across a closed paren, if the stack's not empty, remove an open paren from the stack
# if the stack is empty, this open paren does not have a complement, so you increase the count by 1

def valid_parens(str):
  
  open_parens = []
  count = 0
  
  for char in str:
    if char == "(":
      open_parens.append(char)
    else:
      if open_parens:
        open_parens.pop()
      else:
        count += 1
        
  return len(open_parens) + count

print(valid_parens("((("))
      