availabelItmes = {
    1: {'Item': 'Biscuits', 'Quantity':5, 'Cost/Item':20.5},
    2:{'Item': 'Chocolates', 'Quantity':10, 'Cost/Item':35},
    3:{'Item': 'Coffee', 'Quantity':25, 'Cost/Item':55},
    4:{'Item': 'Chips', 'Quantity':10, 'Cost/Item':50},
    5:{'Item': 'Cream', 'Quantity':5, 'Cost/Item':30}
}

def display_available_items(a):
    print("\t\t Available Items")
    print(f'{'S.No.':<15}{'Item':<15}{'Quantity'<15}{'Cost/item':<15}')
    for index, row in dict.items():
        print(f"{index:<15}{row['Item']:<15}{row['Quantity']:<15}{row['Cost/item']:<15}")