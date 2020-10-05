def repeatedString(s, n):

    # if string is only 'a', then a shows up n times.
    if s == 'a':
        print(n)


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