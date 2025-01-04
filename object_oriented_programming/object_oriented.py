from prettytable import PrettyTable 
table = PrettyTable()
table.add_column('Pokemon name', ['pickachue', 'squirtel', 'sarmander'])
table.add_column('type', ['electric', 'water', 'fire'])
table.align = "l"
print(table)
