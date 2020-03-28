"""Find window of time when most authors were active.

For example::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, and Carol were all active then).

If there's more than one period, find the earliest::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ...    ('Eve',   1955, 1985),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, Carol were active 1920-1945. Bob, Dave, and Eve were active 1951-1960.
Since there's a tie, the first was returned)
"""

def most_active(bio_data):
    """Find window of time when most authors were active."""

# create a list of years from 1900 - 1999 (baseline for heat map):

    years = []

    for year in range(1900, 2000):
        years.append(0)
    
# add active years to heat map:

    for data in bio_data:
        for year in range((data[1]-1900), (data[2]-1900+1)):
            years[year] += 1

# find all active years with highest number of authors:

    current = 0

    for year in years:
        while current < year:
            current = year 
    
    active_years = []
    count = 0

    for year in years:
        if current == year:
            active_years.append(count)
        count += 1

    print(active_years)

# only keep longest stretch of continuous years:

    # def find_longest_stretch(years):


    # current = 0
    # lst = []

    # if active_years[-1] - active_years[0] == len(active_years):
    #     lst = active_years
    # else:
    #     find_longest_stretch(active_years)



    
            

    
        

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")