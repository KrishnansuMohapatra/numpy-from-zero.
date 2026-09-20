import numpy as np

# NumPy Lesson 10: Working with Real Data

data = np.genfromtxt(
    "store_records.csv",
    delimiter=",",
    skip_header=1
)

print("Loaded Data Shape:", data.shape)

# Columns: 0: Store ID, 1: Daily Customers, 2: Revenue, 3: Expenses
store_ids = data[:, 0]
customers = data[:, 1]
revenue = data[:, 2]
expenses = data[:, 3]

profit = revenue - expenses
profit_margin = (profit / revenue) * 100

print(f"Total Revenue: ${np.sum(revenue):,.2f}")
print(f"Total Profit:  ${np.sum(profit):,.2f}")
print(f"Average Profit Margin: {np.mean(profit_margin):.2f}%")

high_revenue_stores = store_ids[revenue > np.mean(revenue)]
print("Stores beating average revenue (IDs):", high_revenue_stores.astype(int))

best_idx = np.argmax(profit)
print(f"Most Profitable Store: ID {int(store_ids[best_idx])} with ${profit[best_idx]:,.2f} profit")
