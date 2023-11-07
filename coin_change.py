def findMin(val):
     
    deno = [1, 5, 10, 25]
    n = len(deno)
    ans = []
    i = n - 1
    while(i >= 0):
        while (val >= deno[i]):
            val -= deno[i]
            ans.append(deno[i])
        i -= 1
 
    print("Number of coins required are {}".format(len(ans)))

value = 113
findMin(value)

def make_change(target, denominations):
    denominations.sort(reverse=True)  # Sort denominations in descending order
    num_coins = 0
    change = []
    # looping through all the denominations
    for denom in denominations:
        while target >= denom:
            target -= denom
            num_coins += 1
            change.append(denom)

    return num_coins, change


target_value = 120
power_of_c_denominations = [1, 5, 25]  # Consider denominations (5^0, 5^1, 5^2)
num_coins, optimal_change = make_change(target_value, power_of_c_denominations)

print("Number of coins required are:", num_coins)
print("The most optimal change is as:", optimal_change)

def make_change_dp(coins, n):
    # Initialize a list to store the minimum number of coins for each value from 0 to n
    min_coins = [float('inf')] * (n + 1)

    # minnumber of coins to make change for 0 cents is 0
    min_coins[0] = 0

    # loop through each coin denomination
    for coin in coins:
        # Update min_coins for values from coin to n in the array
        for v in range(coin, n + 1):
            min_coins[v] = min(min_coins[v], min_coins[v - coin] + 1)

    # minnumber of coins needed to make change for 'n' cents is stored in at nth index in the array
    return min_coins[n]

coin_denominations = [1, 3, 4]
target_value = 6

min_coins_needed = make_change_dp(coin_denominations, target_value)
print("Minimum number of coins needed:", min_coins_needed)
