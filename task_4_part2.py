sales = [100, 200, 300, 400, 500]
total_sales = 0
i = 0

while total_sales < 1000 and i < len(sales):
    total_sales += sales[i]
    i += 1

print("\nTotal sales =", total_sales)
