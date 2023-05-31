from prettytable import PrettyTable

import subprocess


output = subprocess.check_output(['qm', 'list']).decode('utf-8')


lines = output.strip().split('\n')

table = PrettyTable()
table.field_names = ["VM", "MEM (MB)"]

total_memory = 0

for line in lines[1:]:
    columns = line.split()
    memory = int(columns[3])
    name = columns[1]
    total_memory += memory
    table.add_row([name, memory])

print(table)
print("Total VM memory: {} MB".format(total_memory))

host_memory_output = subprocess.check_output(['free', '-m']).decode('utf-8')
host_memory_lines = host_memory_output.strip().split('\n')
host_memory_values = host_memory_lines[1].split()[1:]
host_total_memory = int(host_memory_values[0])

difference = host_total_memory - total_memory
print("Current Host memory: {} MB".format(host_total_memory))
print("Difference: {} MB".format(difference))
