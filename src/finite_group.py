import pandas as pd
from itertools import product

def create_Cn(n):
    ''' Create the group Z4 with its operation table '''
    elements = list(range(n))
    table = {}

    pairs = list(product(elements, repeat=2))
    for (a, b) in pairs:
        table[(a, b)] = (a + b) % n
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

def find_identity(elements, table):
    ''' Find the identity element in the group '''
    for e in elements:
        if all(operate(e, x, table) == x for x in elements) and all(operate(x, e, table) == x for x in elements):
            return e
    return None

def check_order(elements, table):
    ''' Check the order of each element in the group '''
    e = find_identity(elements, table)
    orders = {}
    for g in elements:
        order = 1
        result = g
        while result != e:
            result = operate(result, g, table)
            order += 1
        orders[g] = order
    return orders

def is_abelian(elements, table):
    ''' Check if the group is abelian '''
    for i, g in enumerate(elements):
        for j in range(i+1, len(elements)):
            h = elements[j]
            if table[(g, h)] != table[(h, g)]:
                return False
    return True

if __name__ == "__main__":
    elements, table = create_Cn(6)
    print("Elements of Cn:", elements)
    print("Order of each element:", check_order(elements, table))
    print("Identity Element:", find_identity(elements, table))
    print("Is the group abelian?", is_abelian(elements, table))
    print("Operation Table:")
    display_table(table)

    # Example operation
    a, b = 2, 3
    result = operate(a, b, table)
    print(f"Example: {a} * {b} = {result}")