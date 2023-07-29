# Acme Payroll Program




print()
print("Welcome to the Acme Payroll Program")
print("Please enter the following information to generate your paycheck: ")

#employee names
employee_list = []
employee_list.append(input("What is the employee's name? ").strip().title())

    
#user input for pay and hours worked
PayRate = float(input('Enter the rate of pay for the employee:$    '))    
HoursWorked = float(input("Enter the number of hours worked by the employee: "))
if HoursWorked <= 40:
    normal_pay = round(HoursWorked * PayRate)
    grossPay = round(normal_pay)
    print(f"The employee: , {employee_list} , worked a total of,{HoursWorked} ,therefore thier pay is: $ , {normal_pay}")
elif HoursWorked > 40:
    OThours = round(HoursWorked -40)
    OTPayRate = round(PayRate * 1.5)
    normal_pay = round(40 * PayRate)
    grossPay = round(normal_pay + OTPayRate * OThours)
    print("Employee", employee_list, "has accumulated", OThours,)
    print("Employee", employee_list, "\'s overtime payrate is:$ ", OTPayRate,)
    
#calculate tax deductions 
fedtax_rate = .10
StateTaxRate = .03
FICAtax_rate = .07
tax_deductions = (grossPay - (fedtax_rate + StateTaxRate + FICAtax_rate))
 


#Header for the paycheck

NetPay = grossPay - (tax_deductions)
RegularPay = normal_pay
OTpay = OTPayRate *OThours
GrossPay = normal_pay + OTpay
HoursWorked = input(HoursWorked)
PayRate = input(PayRate)
FedTax = .10
StateTax = .03
FICAtax_rate = .07
totaldeductions = tax_deductions
Employee_Name = input(employee_list)

print ("Paycheck for", Employee_Name, ":")
print ("Gross Pay:", GrossPay)
print ("Regular Pay:", RegularPay)
print ("OT Pay:", OTpay)
print ("Deductions:", totaldeductions)
print ("Net Pay:", NetPay)
print ("Hours Worked:", HoursWorked)
print ("Pay Rate:", PayRate)


  

    
