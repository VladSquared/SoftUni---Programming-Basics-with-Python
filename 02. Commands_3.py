sequence = input()
sequence = sequence.split()

while True:
    cmd = input()
    if cmd == 'end':
        sequence = list(map(str, sequence))
        print(', '.join(sequence))
        break
    if 'reverse' in cmd:
        index, count = int(cmd.split()[2]), int(cmd.split()[4])
        partition = sequence[index:index + count]
        reversed_partition = partition[::-1]
        sequence = sequence[:index] + reversed_partition + sequence[index + count:]
    if 'sort' in cmd:
        index, count = int(cmd.split()[2]), int(cmd.split()[4])
        sorted_partition = sorted(sequence[index:index + count])
        sequence = sequence[:index] + sorted_partition + sequence[index + count:]
    if 'remove' in cmd:
        count = int(cmd.split()[1])
        sequence = sequence[count:]