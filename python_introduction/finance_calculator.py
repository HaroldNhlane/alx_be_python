income = float(input("Enter your monthly income: "))
expense = float(input("Enter your total monthly expenses: "))
interest = 0.05

monthly_savings = income - expense

print("Your monthly savings are $",monthly_savings)

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Projected savings after one year, with interest, is: $",projected_savings)
