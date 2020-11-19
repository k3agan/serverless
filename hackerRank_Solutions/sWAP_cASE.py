def swap_case(s):
    return ''.join([char.lower() if char.isupper() else char.upper() for char in s])

"""
The list comprehension returns a list of characters ['h','A','C','K','E','R' ...]
This is why perform join on a blank string.

Sample Input:
HackerRank.com presents "Pythonist 2".

Sample Output:
hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""