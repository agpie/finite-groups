from itertools import product

# Z4
elements = [0, 1, 2, 3]

'''
opTable = {
    (0, 0): 0,
    (0, 1): 1,
    (0, 2): 2,
    (0, 3): 3,
    (1, 0): 1,
    (1, 1): 2,
    (1, 2): 3,
    (1, 3): 0,
    (2, 0): 2,
    (2, 1): 3,
    (2, 2): 0,
    (2, 3): 1,
    (3, 0): 3,
    (3, 1): 0,
    (3, 2): 1,
    (3, 3): 2
}
'''

def create_z4():
    elements = [0, 1, 2, 3]
    table = {}

    pairs = list(product(elements, repeat=2))

    for (a, b) in pairs:
        table[(a, b)] = (a + b) % 4

    return elements, table


def multiply(a, b, Table):
    return Table[(a, b)]

#result = multiply(2, 3, opTable)
#print(result)
elements, table = create_z4()
print("Elements: ", elements)
print("Operation Table: ")
for key in table:
    print(f"{key}: {table[key]}")
result = multiply(2, 3, table)
print("2 * 3 = ", result)