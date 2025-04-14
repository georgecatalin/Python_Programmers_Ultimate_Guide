import math

shopping_cart = [200,57,4676,33,21]

total_amount = sum(shopping_cart)
print(f"The total amount of the shopping cart is {total_amount}")
max_buy = max(shopping_cart) # 4676
print(max_buy)
min_buy = min(shopping_cart) #21
print(min_buy)

print(math.prod(shopping_cart)) # 200 *57*4676*33*31