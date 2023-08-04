import pandas as pd
import matplotlib.pyplot as plt


# Inventory by Month
inventorybymonth = 'inventorybymonth.xlsx'
ibm = pd.read_excel(inventorybymonth)
plt.plot(ibm['Month'], ibm['Inventory'], marker='o', linestyle='-', color='b')
plt.fill_between(ibm['Month'], ibm['Inventory'], alpha=0.3, color='blue')
plt.xlabel('Month')
plt.ylabel('Inventory')
plt.title('Inventory by Month')
plt.grid(False)
plt.show()

# Inventory by Product
inventorybyproduct = 'inventorybyproduct.xlsx'
ibp = pd.read_excel(inventorybyproduct)

plt.barh(ibp['Inventory'], ibp['Product'])
plt.xlabel('Inventory')
plt.ylabel('Product')
plt.title('Inventory by Product')
plt.grid(False)
plt.show()


# Product Breakdown
productbreakdown = 'productbreakdown.xlsx'
pb = pd.read_excel(productbreakdown)

data_grouped = pb.groupby('Product')['Breakdown'].sum()
plt.pie(data_grouped, labels=data_grouped.index, autopct='%1.1f%%')
plt.title('Product Breakdown')
plt.axis("equal")
plt.show()

# Sales by Product
salesbyproduct = 'salesbyproduct.xlsx'
sbp = pd.read_excel(salesbyproduct)

plt.bar(sbp['Product'], sbp['Sales'])
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Sales By Product')
plt.grid(False)
plt.show()

# Sales by Year
salesbyyear = 'salesbyyear.xlsx'
sby = pd.read_excel(salesbyyear)
plt.plot(sby["Year"], sby["Sales"])
plt.title("Sales by Year")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()



