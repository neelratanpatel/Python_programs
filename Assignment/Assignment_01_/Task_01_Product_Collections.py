# This is the python first assignment 

# creating a list and assigning values.
products = list(('Laptop','Phone','Keyboard','Mouse','Monitor','Key Chain'))

# creating a tuple and storing values.

sample_product = ('Laptop',500000,'Electronic')

# Printing 2nd and last product from the product list.

print(products[1])
print(products[-1])

# Appending new products in the product list

products.append('Key')
products.append('Bike')

# Printing the updated product list

print(products)


# Extra Optional
# Converting sample_product into a list

sample_product = list(sample_product)

# changing the updated list price

sample_product[1] = 150000

# converting the sample_product list to again tuple

sample_product = tuple(sample_product)
