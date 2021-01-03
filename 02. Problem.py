import re

pattern = r'(?P<separator>[*|@])(?P<tag>[A-Z][a-z]{2,})(?P=separator): (\[[A-Za-z]\]\|){3}$'

for _ in range(int(input())):
    message = input()
    checked_message = re.search(pattern, message)
    if checked_message == None:
        print("Valid message not found!")
    else:
        x = checked_message.groupdict()
        tag = x['tag']
        d1, d2, d3 = message[-11], message[-7], message[-3]
        print(f'{tag}: {ord(d1)} {ord(d2)} {ord(d3)}')
