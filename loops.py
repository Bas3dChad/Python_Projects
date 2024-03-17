# for loop is used to iterate over a sequence, such as a list, tuple, string or any other iterable object. It allows you to perform a set of instructions repeadetly for each item in the sequence.
"""
fruits = ['apples', 'oranges', 'bananas', 'strawberries', 'watermelon', 'pineapple', 'mango']
print(fruits)
"""
"""
for index, i in enumerate (fruits):
    print(index, i)
"""
""" 
for i in range(1, 5):
    print(i)

"""
    # A nested for loop is a loop inside another loop. Allows you to perform repeated iterations within iterations. WIth nested for loops you can traverse and manipulate elements in multiple dimensions such as a matrix or a list of lists

"""
matrix = [[1,2,3], 
                [4,5,6], 
                [7,8,9]]

for row in matrix:
  for element in row:
    print(element)

"""

"""
for i in range(1,5):
    for j in range(i):
       print('*', end='  ')
       print()
    """

#Make a list in animals. use the for loops and print it.
#Make a list of country. use the nested for loops and print in iterable of sequence.
#Practice lists append and remove functions from an empty list