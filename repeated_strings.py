def repeatedString(s, n):

    # if string is only 'a', then a shows up n times.
    set_a = set(s)
    if len(set_a) == 1 and 'a' in set_a:
        return n

    num_repeats = n // len(s)
    num_remaining_letters = n % len(s)

    # use built-in count method for better runtime
    return ((s.count('a') * num_repeats) + s[:num_remaining_letters].count('a'))


"""
Alternative solution / O(mn)
def repeatedString(s, n):
    
    if s == 'a':
        return n

    count = 0
    # remaining number of letters to complete sequence
    remaining_string = n - len(s)
    # number of repeats using floor division
    num_repeats = remaining_string // len(s)
    # calculate any remaining letters
    remaining_letters = remaining_string % (s)
    # concatenate everything for 1st n number of letters
    string = s + (s * num_repeats) + s[:remaining_letters]

    for char in string:
        if char == 'a':
            count += 1

    return count
"""

"""
Alternative solution / O(nm)
def repeatedString(s,n):

    if s == 'a':
        return n

    count = 0
    string_long = s * n
    string = string_long[:n]
    for char in string:
        if char == 'a':
            count += 1

    return count
"""

if __name__ == '__main__':

    print(repeatedString('aba', 10))
    print(repeatedString('a', 1000000000000000))