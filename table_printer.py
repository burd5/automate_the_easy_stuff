# Table Printer

def printTable(list):
    colWidths = [0] * len(list)
    for i in range(len(list)):
        colWidths[i] = len(max(list[i], key = len))
    for i in range(len(list[0])):
        for j in range(len(list)):
            print(list[j][i].rjust(colWidths[j], ' '), end= ' ')
        print()
    

print(printTable([['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]))