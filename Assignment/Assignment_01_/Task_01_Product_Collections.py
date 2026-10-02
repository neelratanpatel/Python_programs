
#####    ###    ####   #   #                  #   
  #     #   #  #       #  #                  ##   
  #     #####   ###    ###       ####         #   
  #     #   #      #   #  #                   #   
  #     #   #  ####    #   #                #####



# This is the python first task Product Collections
 
# creating a list and assigning values. 
products = list(('Laptop','Phone','Keyboard','Mouse','Monitor','Key_chain')) 
 
# creating a tuple and storing values. 
 
sample_product = ('Laptop',500000,'Electronic') 
 
# Printing 2nd and last product from the product list. 
 
print(products[1]) 
print(products[-1]) 
 
# Appending new products in the product list 
 
products.append('Key') 
products.append('Mt-15') 
 
# Printing the updated product list 
 
print(products) 
 
 
# Extra Optional 
# Converting sample_product into a list 
 
sample_product = list(sample_product) 
 
# changing the updated list price 
 
sample_product[1] = 150000 
 
# converting the sample_product list to again tuple 
 
sample_product = tuple(sample_product) 





#####    ###    ####   #   #                  #### 
  #     #   #  #       #  #                      # 
  #     #####   ###    ###       ####          ### 
  #     #   #      #   #  #                   #    
  #     #   #  ####    #   #                 #####



# This is the python second task Categories

# defining a new list categories which includes the categories of product list

catetgories = ['electronic','electronic','electronic','electronic','electronic','tool','tool','bike']

# converting the categories list into categories_set using set

catetgories_set = set(catetgories)

# adding an item into set

catetgories_set.add('car')

# Chacking the dublicate values is ignore or not

catetgories_set.add('tool')

# Chaecking the value is present in the set or not

print('bike' in catetgories_set)
print('Fruits' in catetgories_set)

# getting the total number of unique categories in set

print(len(catetgories_set))




#####    ###    ####   #   #                  #### 
  #     #   #  #       #  #                      # 
  #     #####   ###    ###       ####          ### 
  #     #   #      #   #  #                      # 
  #     #   #  ####    #   #                 #####


# This is the python Third task Product Pricing

# 3.1 creating a dictionary which name is price_dict with product name and values

price_dict = dict(Laptop=500000,Phone=50000,Keyboard=30000,Mouse=15000,Monitor=20000,Key_chain=500,Key=5000,Mt_15=300000)

# 3.2.a Adding a new product in the dictionary

price_dict['bmw_m5'] = 23000000

# 3.2.b Removing a existing product in the dictionary 

item_for_remove = 'Laptop'

if item_for_remove in price_dict:
    price_dict.pop(item_for_remove)
else:
    print(item_for_remove,"is not present in the list")

# 3.3 Print the average price of all products (use only dictionary operations and basic arithmetic)

total_sum = 0;
total_item=0
for value in price_dict.values():
    total_item=total_item+1
    total_sum+=value

print(total_sum/total_item)



#####    ###    ####   #   #                     # 
  #     #   #  #       #  #                   #  # 
  #     #####   ###    ###       ####        # # # # #
  #     #   #      #   #  #                      # 
  #     #   #  ####    #   #                     #


# 4.1 Using the products list and price_dict, create a list of tuples named catalog where each tuple (product_name,price and category).

tup1 = tuple(products)
tup2 = tuple(price_dict.values())
tup3 = tuple(catetgories)

catalog = tup1 + tup2 + tup3
print(catalog)

# print(products)    
# print(price_dict)
# print(catetgories)