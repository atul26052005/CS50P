cost = 50
amount_paid = 0

while amount_paid < cost:
    print(f"Amount Due: {cost - amount_paid}")
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        amount_paid += coin

change = amount_paid - cost
print(f"Change Owed: {change}")