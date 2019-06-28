#! /usr/local/bin/env python3

# table-printer.py

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]


def printTable():
    colWidths = [0] * len(tableData)
    for each in tableData:
        for item in each:
            print(item)


printTable(tableData)
