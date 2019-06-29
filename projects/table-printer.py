#! /usr/local/bin/env python3

# table-printer.py


def print_table(table):
    # Create a list containing the same number of 0 values as
    # the number of inner lists in tableData
    col_width = [0] * len(table)
    inner_list = 0     # inner list count

    # Find the longest word in each of the inner_list so that
    # the col_width is wide enough to fit all the words
    while inner_list < len(table):
        for word in table_data[inner_list]:
            if len(word) > col_width[inner_list]:
                col_width[inner_list] = len(word)
        inner_list += 1

    # Iterate over inner_lists and print each corresponding word from
    # each inner_lists and right aligned with the col_width value.
    # A space was added to both sides of each word to create column spaces.
    for each_word in range(len(table[0])):
        new_row = ''
        for inner_list in range(len(table)):
            new_row += ' ' + table[inner_list][each_word].rjust(
                col_width[inner_list]) + ' '
        print(new_row)


table_data = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose'],
]

print_table(table_data)
