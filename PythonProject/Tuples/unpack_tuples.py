product_details = ("IPhone","Apple",3700)

# unpacking option 1
product_name_1 = product_details[0]
brand_1 = product_name_1[1]
price_1 = product_details[2]

print(product_name_1, brand_1, price_1)


# unpacking option 2
product_name_2, brand_2, price_2 = product_details
print(product_name_2, brand_2, price_2)


# unpacking option 3 with splat * operator
product_name_3, *others = product_details # others will be a list containining all remaining elements beside the first element mapped
print(product_name_3,others)