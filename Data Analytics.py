import pandas as pd 

# Correct path to CSV file using raw string
data = pd.read_csv(r"C:\Users\Faruq\source\repos\orders.csv", na_values=['Not Available','unknown'])
print(data['Ship Mode'].unique())

#rename the column names
data.columns = data.columns.str.lower()
data.columns = data.columns.str.replace(' ','_')

#derive new column for discount, sale price and profit 
data['discount'] = data['list_price']*data['discount_percent']/100
data['sale_price'] = data['list_price'] - data['discount']
data['profit'] = data['sale_price'] - data['cost_price']


#convert order from object data type to datetime
data['order_date'] = pd.to_datetime(data['order_date'], format = "%Y-%m-%d")


#drop cost price, list price and discount percent columns
data.drop(columns=['list_price','cost_price','discount_percent'], inplace = True)
print(data.head(5))
#print(data.columns)

import sqlalchemy as sal
engine = sal.create_engine("mssql+pyodbc://ANKIT\\SQLEXPRESS/master?driver=ODBC+Driver+17+for+SQL+Server")
conn = engine.connect()
