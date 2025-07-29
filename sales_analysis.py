
# Sales Data Analysis Project

## 1. Load Dataset
import pandas as pd

df = pd.read_csv("sales_data_cleaned.csv")
df['date'] = pd.to_datetime(df['date'])
df['total_amount'] = df['quantity'] * df['price']
print(df.head())

## 2. Product-wise Sales
product_sales = df.groupby('product_name')['total_amount'].sum().sort_values(ascending=False)
print(product_sales)

## 3. Sales by Location
location_sales = df.groupby('location')['total_amount'].sum().sort_values(ascending=False)
print(location_sales)

## 4. Daily Sales Trend
daily_sales = df.groupby('date')['total_amount'].sum()
print(daily_sales)

## 5. Visualizations
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 5))
sns.barplot(x=product_sales.index, y=product_sales.values, palette="Blues_d")
plt.title("Top Products by Total Sales")
plt.ylabel("Total Sales (₹)")
plt.xlabel("Product Name")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(x=location_sales.index, y=location_sales.values, palette="Greens_d")
plt.title("Sales by Location")
plt.ylabel("Total Sales (₹)")
plt.xlabel("Location")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.lineplot(x=daily_sales.index, y=daily_sales.values, marker='o')
plt.title("Daily Sales Trend")
plt.ylabel("Total Sales (₹)")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
