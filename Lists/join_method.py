my_list = ["George", "Sorin", "Liviu", "Cornel", "Mirel"]

print(" and ".join(my_list)) # George and Sorin and Liviu and Cornel and Mirel

print(f"{" , ".join(my_list[:-1])} and {my_list[-1]}") # George , Sorin , Liviu , Cornel and Mirel
