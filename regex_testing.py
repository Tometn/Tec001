import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search(r'^From (\S+.@\S+)', line):
        mail = str(re.findall(r'^From (\S+@\S+)', line))
        print(mail)
