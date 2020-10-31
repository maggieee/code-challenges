# One instagram sticker pack has each of the letters 
# in "instagram" in it as many times as that letter 
# appears in "instagram". 

# Write a function that takes in a word and returns
# an integer for how many sticker packs would be 
# needed to spell out the word.

# e.g. instagram_pack("gram") --> 1
# instagram_pack("grass") --> 2
# instagram_pack("margarita") --> 2
# instagram_pack("tagging") --> 3

def instagram_pack(str):

    insta_dict = {}
    str_dict = {}
    pack_count = 0

    # for char in "instagram":
    #         if insta_dict.get(char):
    #             insta_dict[char] += 1
    #         else:
    #             insta_dict[char] = 1

    # for char in str:
    #         if str_dict.get(char):
    #             str_dict[char] += 1
    #         else:
    #             str_dict[char] = 1

    # for char in "instagram":
    #     insta_dict[char] = insta_dict.get(char, 0) + 1

    for char in str:
        str_dict[char] = str_dict.get(char, 0) + 1

    for key, value in str_dict.items():

        if key == "a" and value > pack_count:
            if value / 2 > pack_count:
                pack_count = round(value / 2)
                
        if key != "a" and value > pack_count:
            pack_count = value

    return pack_count

print(instagram_pack("grass"))