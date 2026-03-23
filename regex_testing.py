import re

email_counter = {}

mbox_short = open('mbox-short.txt')
for line in mbox_short:
    line = line.rstrip()
    emails = tuple(re.findall(r'^From\s\S+@[^\s);]+\s\w+\s(\w+\s+\d+)\s\d+\s(\d+)', line))
    for email in emails:   
        email_counter[email] = email_counter.get(email, 0) + 1

for key in email_counter:
    print(key, ':', email_counter[key])