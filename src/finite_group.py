import pandas as pd
from itertools import product

class FiniteGroup:
    
    def __init__(self, elements, table, labels=None):
        self.elements = elements
        self.table = table
        self.order = len(elements)
        self.labels = labels if labels else [str(i) for i in range(self.order)]
        self.identity = self.find_identity()

    def get_label(self, element):
        ''' Get the label of an element '''
        if element in self.elements:
            return self.labels[self.elements.index(element)]
        return None

    def operate(self, a, b):
        ''' Perform the group operation on elements a and b using the operation table '''
        return self.table[(a, b)]
    
    def display_table(self):
        ''' Display the operation table in a readable format '''
        df = pd.DataFrame(index=self.labels, columns=self.labels)
        for (a, b), result in self.table.items():
            df.loc[self.get_label(a), self.get_label(b)] = self.get_label(result)
        print(df)
    
    def find_identity(self):
        ''' Find the identity element in the group '''
        for e in self.elements:
            if all(self.operate(e, x) == x for x in self.elements) and all(self.operate(x, e) == x for x in self.elements):
                return e
        return None

    def check_order(self):
        ''' Check the order of each element in the group '''
        e = self.find_identity()
        orders = {}
        for g in self.elements:
            order = 1
            result = g
            while result != e:
                result = self.operate(result, g)
                order += 1
            orders[g] = order
        return orders
    
    def is_abelian(self):
        ''' Check if the group is abelian '''
        for i, g in enumerate(self.elements):
            for j in range(i+1, len(self.elements)):
                h = self.elements[j]
                if self.table[(g, h)] != self.table[(h, g)]:
                    return False
        return True

def create_Cn(n):
    ''' Create the cyclic group Cn with its operation table '''
    elements = list(range(n))
    table = {}

    pairs = list(product(elements, repeat=2))
    for (a, b) in pairs:
        table[(a, b)] = (a + b) % n
    return elements, table

if __name__ == "__main__":
    
    C4 = FiniteGroup(*create_Cn(4), labels=['e', 'a', 'a2', 'a3'])

    print("Elements of C4:", C4.elements)
    print("Order of the group C4:", C4.order)
    print("Operation Table of C4:")
    C4.display_table()
    print("Order of each element in C4:", {C4.get_label(k): v for k, v in C4.check_order().items()})
    print("Identity Element of C4:", C4.get_label(C4.identity))
    print("Is C4 abelian?", C4.is_abelian())