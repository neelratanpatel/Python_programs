
#####    ###    ####   #   #                  #   
  #     #   #  #       #  #                  ##   
  #     #####   ###    ###       ####         #   
  #     #   #      #   #  #                   #   
  #     #   #  ####    #   #                #####



# This is the python first task Product Collections
 
# creating a list and assigning values. 
products = list(('Laptop','Phone','Keyboard','Mouse','Monitor','Key Chain')) 
 
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

# creating a dictionary which name is price_dict with product name and values

price_dict = dict(laptop=500000,phone=50000,keyboard=30000,mouse=15000,key_chain=500,key=5000,mt_15=300000)

# Adding a new product in the dictionary

price_dict['bmw_m5'] = 23000000

print(price_dict)