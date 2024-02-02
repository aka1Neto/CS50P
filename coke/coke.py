amount = 50;
coins = [25, 10, 5];

while amount > 0:
    print("Amount Due:", amount);
    coin = int(input("Insert Coin: "));
    if coin in coins:
        amount -= coin;

print("Change Owed:", amount * -1);