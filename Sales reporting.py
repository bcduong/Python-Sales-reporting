#!/usr/bin/env python
# coding: utf-8

# # Task 1: Import packages and Load data

# In[210]:


import pandas as pd
import matplotlib.pyplot as plt


# In[211]:


import os


# In[212]:


path = '/Users/bcduong/Desktop/Inseec/Sales_Reporting/'


# In[213]:


df = pd.read_csv(path + 'sales2019_1.csv')


# In[214]:


df


# In[215]:


df.head(5)


# # Task 2: Clean and Preprocess data

# ## Task 2.1: Merge 12-month data

# In[216]:


filepaths = []
for file in os.listdir (path):
    if file.endswith('.csv'):
        filepath = path + file 


# In[217]:


filepaths.append(filepath)


# In[218]:


filepaths


# In[219]:


os.listdir (path)


# In[220]:


frames = []
all_length = []
for file in os.listdir(path):
    if file.endswith('.csv'):
        filepath = path + file
        df1 = pd.read_csv(filepath)
        frames.append(df1)
        result = pd.concat(frames)
        length_1month = len(df1.index)
        all_length.append(length_1month)


# In[221]:


print (sum (all_length))


# In[222]:


result


# In[223]:


print (sum(all_length))


# ## Task 2.2: Add colomn Month

# In[224]:


result['Month']= result['Order Date'].str [0:2]
result


# In[225]:


print (set(result['Month']))


# ## Task 2.3: Get rid of 'NaN' and 'Or' values

# In[226]:


result = result.dropna (how ='all')
result = result[result['Month'] != 'Or']
result


# In[227]:


print (set(result['Month']))


# # Task 3: Reporting

# ## Task 3.1: Which month has highest sales? 

# #### Change column data type

# In[228]:


df = result


# In[229]:


dftypes = df.dtypes


# In[230]:


dftypes


# In[238]:


df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'], downcast = 'integer')
df['Price Each'] = pd.to_numeric(df['Price Each'], downcast = 'float')
df


# In[ ]:





# #### Create and move Sales column 

# In[239]:


df['Sales'] = df['Quantity Ordered'] * df['Price Each']


# In[240]:


df.head(5)


# In[241]:


moving_column = df.pop ('Sales')


# In[242]:


df.insert (4, 'Sales', moving_column)


# In[243]:


df.head(5)


# In[244]:


sales_value = df.groupby ('Month'). sum()['Sales']


# In[245]:


sales_value


# In[246]:


months = range(1,13)
plt.bar(x=months, height=sales_value)
plt.xticks(months)
plt.xlabel('Months')
plt.ylabel('Sales in USD')
plt.show()


# ## Task 3.2: Which city has highest sales? 

# In[247]:


sample_adresse = '942 Church St, Austin, TX 73301'


# In[248]:


sample_adresse.split (',')[1]


# In[249]:


address_to_city = lambda address:address.split (',')[1]


# In[250]:


df['City'] = df['Purchase Address'].apply(address_to_city)


# In[251]:


df


# In[252]:


sales_by_city = df.groupby('City').sum()['Sales']


# In[253]:


sales_by_city


# In[254]:


cities = [city for city, sales in sales_by_city.items()]
plt.bar(x=cities, height=sales_by_city)
plt.xticks(cities, rotation=90, size=8)
plt.xlabel('Cities')
plt.ylabel('Sales in USD')
plt.show()


# ## Task 3.3: What time should we place ads to optimze effiency?

# ###  What time costumers place order the most

# In[255]:


df ['Order Date'] = pd.to_datetime (df['Order Date'])
df['hour'] = df['Order Date'].dt.hour
df


# In[256]:


sales_by_hour = df.groupby ('hour').count()['Sales']
sales_by_hour


# In[257]:


hours = [hour for hour, sales in sales_by_hour.items()]


# In[258]:


plt.plot (hours, sales_by_hour)
plt.grid()
plt.xticks(hours, rotation = 90, size = 8)
plt.xlabel('Hour')
plt.ylabel('Nomber of order')


# ### Which products are often sold together? 

# In[ ]:





# In[259]:


df_dup = df[df['Order ID'].duplicated(keep=False)]
groupProduct = lambda product: ', '.join(product)
df_dup['All Products'] = df_dup.groupby('Order ID')['Product'].transform(groupProduct)
df_dup = df_dup[['Order ID', 'All Products']].drop_duplicates()
df_dup['All Products'].value_counts().head(10)


# In[260]:


df_dup


# ## Task 3.5: Relation between price and quantity sold

# In[261]:


all_products = df.groupby('Product').sum()['Quantity Ordered']
prices = df.groupby('Product').mean()['Price Each']
product_list = [product for product, quant in all_products.items()]
all_products


# In[262]:


x = product_list
y1 = all_products
y2 = prices


# In[265]:


fig, ax1 = plt.subplots ()

ax2 = ax1.twinx()
ax1.bar(x, y1, color ='g')
ax2.plot (x, y2, 'b-')

ax1.set_xticklabels(products_list, rotation=90, size=8)
ax1.set_xlabel('Products')
ax1.set_ylabel('Quantity Ordered', color='g')
ax2.set_ylabel('Price Each', color='b')

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




