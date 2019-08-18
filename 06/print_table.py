table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def print_table():
    col_widths = [0] * len(table_data)
    for i in range(len(table_data)):
        col_widths[i] = len(max(table_data[i])) + 1
    for j in range(len(table_data[0])):
        str = ""
        for i in range(len(table_data)):
            str += table_data[i][j].rjust(col_widths[i])
        print(str)
        str = ""


print_table()
