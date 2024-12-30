import numpy as np

sales_data = np.array([
    [200, 250, 300, 400],  
    [150, 200, 250, 300],  
    [100, 150, 200, 250],  
    [180, 220, 270, 320]   
])
products = sales_data[:3, :]
print("Sales data for the first three products:\n", products)
month_product = sales_data[:, -2:]
print("\nSales data for all products in the last two months:\n", month_product)
specific_product = sales_data[1, 3]
print("\nSales data for the 2nd product in the 4th month:", specific_product)
