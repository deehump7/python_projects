print()
print("Welcome to the Acme Payroll Program")
print("Please enter the following information to generate your paycheck: ")

# employee names
employee_list = []
employee_list.append(input("What is the employee's name? ").strip().title())

# user input for pay and hours worked
PayRate = float(input('Enter the rate of pay for the employee: $ '))
HoursWorked = float(input("Enter the number of hours worked by the employee: "))
if HoursWorked <= 40:
    normal_pay = round(HoursWorked * PayRate, 2)  # Rounding to 2 decimal places
    grossPay = round(normal_pay, 2)
    print(f"The employee: {employee_list}, worked a total of {HoursWorked}, therefore their pay is: ${normal_pay}")
elif HoursWorked > 40:
    OThours = round(HoursWorked - 40)
    OTPayRate = round(PayRate * 1.5, 2)  # Rounding to 2 decimal places
    normal_pay = round(40 * PayRate, 2)  # Rounding to 2 decimal places
    grossPay = round(normal_pay + OTPayRate * OThours, 2)  # Rounding to 2 decimal places
    print("Employee", employee_list, "has accumulated", OThours, "hours of overtime.")
    print("Employee", employee_list, "'s overtime pay rate is: $", OTPayRate)

# calculate tax deductions
fedtax_rate = 0.10
StateTaxRate = 0.03
FICAtax_rate = 0.07
tax_deductions = grossPay * (fedtax_rate + StateTaxRate + FICAtax_rate)  # Applying tax rates

# Header for the paycheck
NetPay = grossPay - tax_deductions  # Calculating net pay
RegularPay = normal_pay
OTpay = OTPayRate * OThours
GrossPay = normal_pay + OTpay

print("\nPaycheck for", employee_list, ":")
print("Gross Pay:", GrossPay)
print("Regular Pay:", RegularPay)
print("OT Pay:", OTpay)
print("Deductions:", round(tax_deductions, 2))  # Rounding deductions to 2 decimal places
print("Net Pay:", round(NetPay, 2))  # Rounding net pay to 2 decimal places
print("Hours Worked:", HoursWorked)
print("Pay Rate:", PayRate)
