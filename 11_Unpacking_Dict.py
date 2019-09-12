# Unpacking & Dictionaries

my_list = [1, 2, 3]
x, y, z = my_list  # Automatically assign vars to each item in list
print(z)

# Defining a key value pair. name, mobile, city are the keys and each of them has a value
customer = {
    "name": "Pratik",
    "mobile": "890989",
    "city": "Aurangabd"
}
print(customer.get("name"))
customer["name"] = "Changed Name"
print(customer["name"])

num = {
    1: "One",
    2: "Two",
    3: "Three"
}
no = input('> ')
output = ''
for i in no:
    output += num.get(int(i))+'\t'
print(output)