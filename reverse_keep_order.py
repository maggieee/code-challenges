"""In this challenge, you need to reverse a string, 
keeping the word themselves in order, and preserving exact spacing.

For example, for the string:
"   hello_kitty "

This should produce:
" kitty  hello   "

(Note that we keep the 3 spaces before hello, the two spaces 
between “hello” and “kitty," and the space after “kitty”."""


# have a string
# how would you reverse a string if you were also reversing the letters?
# how would you alter your approach to not reverse the words?

# reverse by looping

# range is where do you want to stop, where do you want to end, and step (exclusive)

def reverse_keep_order(str):
  
  new_str = ""
  stop_char_index = None
  
  for i in range(len(str)-1, -1, -1): #looping through the indexes of the string backwards
    if str[i] == " ":
      if stop_char_index is not None:
        new_str += str[i+1:stop_char_index+1]
        stop_char_index = None
      new_str += str[i] # i is the index 
    elif str[i] != " ":
      if stop_char_index is None:
        stop_char_index = i
        
  if stop_char_index:
    new_str += str[0:stop_char_index+1]
        
  return new_str

print("test '  hi Emily !!!   ' --> '   !!! Emily hi  '")
  
print(reverse_keep_order(" cat rat bat"))