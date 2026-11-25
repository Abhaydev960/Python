principal = float(input("Enter initial investment (Rs.): "))
rate = float(input("Enter annual interest rate (%): "))
years = float(input("Enter number of years: "))
times = int(input("Compounds per year (1, 4, 12): "))

if principal < 0 or rate < 0 or years < 0 or times <= 0:
    print("Please enter valid values.")
else:
    amount = principal * (1 + rate / (100 * times)) ** (times * years)
    print("\n----- INVESTMENT REPORT -----")
    print(f"Initial investment: Rs. {principal:,.2f}")
    print(f"Future value: Rs. {amount:,.2f}")
    print(f"Interest earned: Rs. {amount - principal:,.2f}")
