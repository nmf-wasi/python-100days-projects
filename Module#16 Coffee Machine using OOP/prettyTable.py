from prettytable import PrettyTable

table = PrettyTable()
# table is an object and PrettyTable is a Class
# print(table)
table.add_column("Pokemon Name", ["Wasi", "Lia", "Yuna"])
table.add_column("Pokemon Power", ["22", "21", "19"])
table.align = "l"
print(table)
