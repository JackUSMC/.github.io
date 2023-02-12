# Define the inputs
monthly_income = float(input("Enter the monthly income: "))
monthly_expenses = float(input("Enter the monthly expenses: "))
purchase_price = float(input("Enter the purchase price: "))
down_payment = float(input("Enter the down payment: "))
closing_cost = float(input("Enter the closing cost: "))
taxes = float(input("Enter the annual property taxes: "))
after_repair_value = float(input("Enter the after repair value: "))

# Calculate the monthly cash flow
monthly_cash_flow = monthly_income - monthly_expenses

# Calculate the pro forma cap rate
cap_rate = (monthly_income - monthly_expenses) / (after_repair_value - down_payment - closing_cost)

# Calculate the NOI
noi = monthly_income * 12 - monthly_expenses * 12

# Calculate the total cash needed
total_cash_needed = down_payment + closing_cost + taxes / 12

# Calculate the cash on cash ROI
coc_roi = (monthly_income * 12 - monthly_expenses * 12 - total_cash_needed) / total_cash_needed

# Calculate the purchase cap rate
purchase_cap_rate = noi / purchase_price

# Output the results
print("Monthly Cash Flow:", monthly_cash_flow)
print("Pro Forma Cap Rate:", cap_rate)
print("NOI:", noi)
print("Total Cash Needed:", total_cash_needed)
print("Cash on Cash ROI:", coc_roi)
print("Purchase Cap Rate:", purchase_cap_rate)
