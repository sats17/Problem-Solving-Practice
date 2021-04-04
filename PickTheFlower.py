"""
Joru needs to pick the flower, let's help him with path.

Given Metadata-
Row = Number of row in area
Column = Number of column in area
JoruPlace = A array coordinate where joru stands.
FlowerPlace = A Flower coordinate where flower placed.
"""

def JorusHelper(row, column, joruPlace, flowerPlace):
    area = [[0 for col in range(column)] for row in range(row)]
    for row in area:
        print(row)



row = 4
col = 5
joruPlace = [1,1]
flowerPlace = [2,3]
JorusHelper(row, col, joruPlace, flowerPlace)