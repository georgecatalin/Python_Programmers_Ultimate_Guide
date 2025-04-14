my_string = "someone@email.com"

modified_string_1 = my_string.replace("@","#") # someone#email.com
print(modified_string_1)

modified_string_2 = my_string.replace("o","q")
print(modified_string_2)

# strings are immutable in Python, and the initial strings are not modified
print(my_string) # someone@email.com

my_string_1 = "hello how are you "
mylist = my_string_1.split(" ")
print(mylist)

my_email_addresses = "george@email.com;sorina@email.ro;mara@email.de"
email_list = my_email_addresses.split(";")
print(email_list)

my_other_string = " consoles and laptops and mobiles"
tuple_partition = my_other_string.partition("and") # creates a tuple dividing the string at the first occurrence of the argument
print(tuple_partition)

my_string_to_strip = "   hello World  "
stripped_string_1 = my_string_to_strip.strip()
print(stripped_string_1)

stripped_string_1_left = my_string_to_strip.lstrip()
print("Stripped at the left side", stripped_string_1_left)
stripped_string_1_right = my_string_to_strip.rstrip()
print("Stripped at the right side", stripped_string_1_right)

just_string = "Hello"
just_string_loutput =just_string.ljust(15,"*")
print("Create a new string with the specified width, aligning the old value at the left, and fill the added space with the specified character", just_string_loutput)

just_string_routput =just_string.rjust(15,"*")
print("Create a new string with the specified width, aligning the old value at the right, and fill the added space with the specified character", just_string_loutput)

just_string_coutput =just_string.center(15,"*")
print("Create a new string with the specified width, aligning the old value at the center, and fill the added space lefthand and righthand side with the specified character", just_string_coutput)

a_number = "1978"
zfilled_number = a_number.zfill(10)
print("Padding the number with the required zeroes at the leftside to produce the specified width as parameter", zfilled_number)
