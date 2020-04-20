def oddNumbers(l, r):
    for i in range(l, r+1):
        if i % 2 == 1:
            print(i)
    
    return True


def reverseVowels(word):

    vowels = ['a','e','i','o','u']
    caught_vowels = []

    for idx,i in enumerate(word):
        if i in vowels:
            word = word[:idx] + "*" + word[idx+1:]
            caught_vowels.append(i)
            print(word)
    
    caught_vowels = caught_vowels[::-1]

    for idx2, j in enumerate(word):
        if j == "*":
            word = word[:idx2] + caught_vowels[0] + word[idx2+1:]
            caught_vowels.pop(0)

    return word