__author__ = 'Hannie'

name = input("Enter name: ")
hours = input("Enter number of hours worked weekly: ")
pay = input("Enter hourly pay rate: $")
cpf = input("Enter CPF contribution rate(%): ")
grosspay = float(hours)*float(pay)
cpf_contribution = float(cpf)/100*grosspay
print('''Payroll statement for {0}
Number of hours worked in a week: {1}
Hourly pay rate: ${2:.2f}
Gross pay: {3:.2f}
CPF contribution at {4}% = ${5:.2f}
Net pay = ${6:.2f}'''.format(name, hours, pay, grosspay, float(cpf), cpf_contribution, grosspay - cpf_contribution))
