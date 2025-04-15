java = ("Java", "Programming Language")
cpp = ("C++", "Classic Programming Language")
aspnet = ("ASP.NET", "Web Framework")

technologies_1 = java + cpp # it creates a new tuple
print(type(technologies_1), technologies_1)

technologies_all = java + cpp + aspnet # concatenation with + is not memory efficient as it creates two times tuples
print(type(technologies_all), technologies_all)

# merge tuples using the splat * operator -> it fills in the elements in the tuples, and thus memory efficient
technologies_merged = (*java, *cpp, *aspnet)
print(type(technologies_merged), technologies_merged)

technologies_merged_1 = (*java, *cpp, "Python", "Programming Language", *aspnet) # additional elements can be added to the tuple
print(type(technologies_merged_1), technologies_merged_1)