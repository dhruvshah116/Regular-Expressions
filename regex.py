import re

st = "My 2 favourite numbers are 19 and 42"
y = re.findall('[0-9]+', st)
print(y)
'''
[0-9]+  :  This regular expression matches one or more digits.
re.findall() returns all the substrings that matches the given Regular Expression
'''

x = "From : Using the : character"
print(re.findall('^F.+:', x))
# GREEDY MATCHING
'''
Output : ['From : Using the :']

^F : The first occurence should be F
^F.+: Anything but atleast one occurence (+:one or more , .: anything)
^F.+: The last occurence should be ':'

The repeat character [* and +] push outwards in both directions and matches the largest possible (sub)string.

Unless we explicitly mention , the Regular Expression Library attempts to return the largest possible version of 
the string we're trying to match.
'''

print(re.findall('^F.+?:', x))
# NON-GREEDY MATCHING
'''
Prefers the shortest substring that matches the Regular Expression.
If we add a '?' , the + and * chill out a bit and does not push outwards further.
'''

'-------------------------------------------------------------'

' \S : Non-Space or Non-Blank Characters  '

s='From dhruvshah116@yahoo.in Sat Jan 5 09:14:16 2008'
print("Greedy : ",re.findall("\S+@\S+",s))
print("Non-Greedy : ",re.findall("\S@\S",s))
print()

# FINE TUNING STRING EXTRACTION(More Matching than Extracting)
'''
Parentheses are not part of the match , but they tell where to start and stop what string to extract.
'''
print(re.findall('[0-9]+:[0-9]+:[0-9]+',s))
print(re.findall('\s*?\S+\s*?',s))
