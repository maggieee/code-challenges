Write a function that, when given a list of words, 
eliminates any words that are anagrams of previous
words, then returns an ordered list of the remaining
words.

remove_anagrams(["coed", "code", "list", "listen", "silent"]) --> ["coed", "list", "listen"]

# save a so

# key is word with letters sorted --> value is list of words with letters not sorted

def remove_anagrams(word_list):
  
  sorted_words = set()
  
  result_list = []
  
  for word in word_list:
    if "".join(sorted(word)) not in sorted_words:
      result_list.append(word)
      sorted_words.add("".join(sorted(word)))
    
  return sorted(result_list)

print(remove_anagrams(["coed", "code", "list", "listen", "silent"]))


One instagram sticker pack has each of the letters 
in "instagram" in it as many times as that letter 
appears in "instagram". 

Write a function that takes in a word and returns
an integer for how many sticker packs would be 
needed to spell out the word.

e.g. instagram_pack("gram") --> 1
instagram_pack("grass") --> 2
instagram_pack("margarita") --> 2
instagram_pack("tagging") --> 3