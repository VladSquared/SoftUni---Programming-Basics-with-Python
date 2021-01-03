users = {}
capacity = int(input())

while True:
    cmd = input()
    if cmd == 'Statistics':
        break
    elif cmd.split("=")[0] == 'Add':
        name, sent, received = cmd.split("=")[1], int(cmd.split("=")[2]), int(cmd.split("=")[3])
        if name in users:
            continue
        users[name] = {'sent': sent, 'received': received}
    elif cmd.split("=")[0] == 'Message':
        sender, receiver = cmd.split("=")[1], cmd.split("=")[2]
        if not sender in users or not receiver in users:
            continue
        users[sender]['sent'] += 1
        users[receiver]['received'] += 1
        if users[sender]['sent'] + users[sender]['received'] >= capacity:
            print(f'{sender} reached the capacity!')
            del users[sender]
        if users[receiver]['received'] + users[receiver]['sent'] >= capacity:
            print(f'{receiver} reached the capacity!')
            del users[receiver]
    elif cmd.split("=")[0] == 'Empty':
        name = cmd.split("=")[1]
        if name == 'All':
            users = {}
        elif name in users:
            del users[name]

print(f'Users count: {len(users)}')

users = dict(sorted(users.items(), key=lambda x: (-x[1]['received'], x[0])))

for user in users:
    print(f'{user} - {users[user]["sent"] + users[user]["received"]}')
