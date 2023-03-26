import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

chipo = pd.read_csv(url, sep='\t')

# See the first 10 entries
print(chipo.head(10))

# see how many entries are there:
print(chipo.shape[0])
# or
print(chipo.info())

# What is the number of columns in the dataset?
print(chipo.shape[1])

# 7. Print the name of all the columns.
print(chipo.columns)

# How is the dataset indexed?
print(chipo.index)

# Step 9. Which was the most-ordered item?
c = chipo.groupby('item_name')
# if you want to sum all columns in the DataFrame,
# including non-numeric columns, you can set numeric_only=False:
c = c.sum(numeric_only=False)
c = c.sort_values(['quantity'], ascending=False)
print(c.head(1))

# Step 11. What was the most ordered item in the choice_description column?
c = chipo.groupby('choice_description').sum(numeric_only=False)
c = c.sort_values(['quantity'], ascending=False)
print(c.head(1))

# Step 12. How many items were ordered in total?
print(chipo.quantity.sum())

# Step 13. Turn the item price into a float
# datatype now is object:
print(chipo.item_price.dtype)
# The function takes a single argument x, which is expected to be a string
# with the dollar value. The function uses string slicing to remove
# the first character (the dollar sign) and the last character
# (presumably a space or some other character) from the string,
# leaving only the numerical value.
# The resulting string is then converted to a float using the float() function.
dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)
print(chipo.item_price.dtype)
#Step 14. How much was the revenue for the period in the dataset?
revenue = (chipo['quantity']* chipo['item_price']).sum()

print('Revenue was: $' + str(np.round(revenue,2)))

#Step 15. How many orders were made in the period?
#returns a Pandas Series containing the counts of unique values in the 'order_id' column. Each value in the Series represents the number of times a particular order ID appears in the DataFrame.
#.count() is then called on the resulting Series to count the number of unique order IDs in the DataFrame.
#This gives the total number of orders that were placed.
orders = chipo.order_id.value_counts().count()
print(orders)

#Step 16. What is the average revenue amount per order?
chipo['revenue'] = chipo['quantity'] * chipo['item_price']
order_grouped = chipo.groupby(by=['order_id']).sum(numeric_only=False)
print(order_grouped.mean(numeric_only=True)['revenue'])

#Step 17. How many different items are sold?
chipo.item_name.value_counts().count()