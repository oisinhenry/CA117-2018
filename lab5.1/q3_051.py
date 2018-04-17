import sys, re

for line in sys.stdin:
    print(max(re.findall('[A-Z]+', line), key=len))