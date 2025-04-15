# tuples are immutable, however they can be still modified by transforming them into lists and back

this_tuple = (1,"Jeffrey","Freddi","jfreddi0@apple.com","Male","30.162.129.18","512-466-186","695-920-1915")

print("This is the initial tuple \t ->", this_tuple)

this_tuple_list = list(this_tuple)
this_tuple_list[0] = 46
this_tuple_list.append("0722 764 836")

print(type(this_tuple_list))

this_tuple = tuple(this_tuple_list)
print("This is the tuple after modification through conversion in list \t ->", this_tuple)