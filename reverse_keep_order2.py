def reverse_keep_order(s):
  
  new_string = ""
  i = len(s) - 1

  while i >= 0:
      if s[i] == " ":
          new_string += s[i]
          i -= 1
      else:
          end_idx = i
          while s[i] != " " and i >= 0:
              i -= 1
          new_string += s[i + 1:end_idx + 1]

  return new_string

  # look at Hackbright answers