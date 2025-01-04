availabelItems = {
    1:{'Item': 'Biscuits', 'Quantity':5, 'Cost/Item':20.5},
    2:{'Item': 'Chocolates', 'Quantity':10, 'Cost/Item':35},
    3:{'Item': 'Coffee', 'Quantity':25, 'Cost/Item':55},
    4:{'Item': 'Chips', 'Quantity':10, 'Cost/Item':50},
    5:{'Item': 'Cream', 'Quantity':5, 'Cost/Item':30}
}
name = 'Aaradhya'
address = 'Mathura'
distance = 15
deliveryCharge = 30


def display_available_items(a):
    print("\t\t Available Items")
    print(f'{'S.No.':<15}{'Item':<15}{'Quantity':<15}{'Cost/Item':<15}')
    for index, row in a.items():
        print(f"{index:<15}{row['Item']:<15}{row['Quantity']:<15}{row['Cost/Item']:<15}")

# display_available_items(availabelItems)

user_cart = {'Biscuits': 3, 'Chocolates': 7, 'Coffee': 20, 'Chips': 13, 'Cream': 7}
Total_cost = 0
for i in user_cart:
    want = user_cart[i]
    it = i
    for j in availabelItems:
        it2 = availabelItems[j]['Item']
        if it == it2:
            have = availabelItems[j]['Quantity']
            if want > have:
                print(f"Sorry, we don't have {want} {it}" )
                user_cart[it2] = 0
            else:
                Total_cost += (availabelItems[j]['Cost/Item']) * (want)
                availabelItems[j]['Quantity'] = availabelItems[j]['Quantity'] - want

def display_cart_items(a):
    print("\t\t Items in the cart")
    print(f'{'S.No.':<15}{'Item':<15}{'Quantity':<15}{'Cost':<15}')
    count = 1
    for index, row in a.items():
        print(f'{count:<15}{index:<15}{row:<15}{(row)*availabelItems[count]['Cost/Item']}')
        count += 1


display_cart_items(user_cart)
print(f'Total item cost : {Total_cost}')
distance_cost = distance * deliveryCharge
final_cost = Total_cost + distance_cost
print(f'Final amount : {final_cost}')
print(f'Name : {name},Address : {address}, Distance : {distance}')
