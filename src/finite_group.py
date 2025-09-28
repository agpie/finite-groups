import pandas as pd
from itertools import product

def create_z4():
    ''' Create the group Z4 with its operation table '''
    elements = [0, 1, 2, 3]
    table = {}

    pairs = list(product(elements, repeat=2))

    for (a, b) in pairs:
        table[(a, b)] = (a + b) % 4

    return elements, table

def operate(a, b, table):
    ''' Perform the group operation on elements a and b using the operation table '''
    return table[(a, b)]

def display_table(table):
    ''' Display the operation table in a readable format '''
    df = pd.DataFrame(index=elements, columns=elements)
    for (a, b), result in table.items():
        df.loc[a, b] = result
    print(df)

if __name__ == "__main__":
    elements, table = create_z4()
    print("Elements of Z4:", elements)
    print("Operation Table:")
    display_table(table)

    # Example operation
    a, b = 2, 3
    result = operate(a, b, table)
    print(f"Example: {a} * {b} = {result}")