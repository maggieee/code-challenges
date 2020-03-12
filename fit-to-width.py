"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""

def fit_to_width(string, limit):
    """Print string within a character limit."""

    split_string = string.split(" ")
    word_line = split_string[0]
    char_count = len(split_string[0])
    split_string = split_string[1:]

    if len(string) <= limit:
        print(string)

    else:
        for word in split_string:
            char_count += len(word) + 1
            if char_count <= limit:
                word_line = word_line + " " + word
                split_string.pop(0)
            else:
                print(word_line)
                char_count = len(split_string[0])
                word_line = split_string[0]
                
        

        
    return None


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
