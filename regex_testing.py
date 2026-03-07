import re

text_wall = open('some_strings.txt')
for line in text_wall:
    re.sub(r'\d{10}|\+084\d+ |\+084 \d+', "[REDACTED]", text_wall)
print(text_wall)