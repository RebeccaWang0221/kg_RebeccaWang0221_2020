import sys

s1 = sys.argv[1]
s2 = sys.argv[2]

li1 = [x for x in s1]
li2 = [x for x in s2]

set1 = set(li1)

if len(set1) < len(li2):
    print ("false")
else:
    print ("true")