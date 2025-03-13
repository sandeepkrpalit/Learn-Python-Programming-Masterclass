shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list)) #reference address of shopping_list
print(id(another_list))  #reference address of another_list

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(another_list)

a = b = c = d = e = f = another_list
print(a)

print("Adding cream")
b.append("cream") #append cream to the list
print(c)
print(d)
