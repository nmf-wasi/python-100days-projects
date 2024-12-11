# s="Hello World"
# s[1:4] is 'ell'** -- chars starting at index 1 and extending up to but not including index 4
# s[1:] is 'ello'** -- omitting either index defaults to the start or end of the string
# s[:]** **is 'Hello**' -- omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence like a string or list)
# s[1:100] is 'ello'** -- an index that is too big is truncated down to the string length
s = "Hello World"
print(s[::-1])
# this will reverse print the string

tup=('P','i','a','n','o')
print(tup[::-1])