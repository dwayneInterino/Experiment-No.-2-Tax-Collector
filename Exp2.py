monthIncome = int(input("Enter your monthly income: "))
annualIncome = monthIncome*12


def yearlytax(income):
    if income <= 250000:
        print("Your Annual Tax is 0")
        print("Your Monthly Tax is 0")
    elif income > 250000 or income <= 400000:
        annualtax = (income - 250000) * 0.15
        monthlytax = annualtax/12
        print("Your Annual Tax is ", annualtax)
        print("Your Monthly Tax is ", monthlytax)
    elif income > 400000 or income <= 800000:
        annualtax = 22500 + ((income - 400000) * 0.2)
        monthlytax = annualtax/12
        print("Your Annual Tax is ", annualtax)
        print("Your Monthly Tax is ", monthlytax)
    elif income > 800000 or income <= 2000000:
        annualtax = 102500 + ((income - 800000) * 0.25)
        monthlytax = annualtax/12
        print("Your Annual Tax is ", annualtax)
        print("Your Monthly Tax is ", monthlytax)
    elif income > 2000000 or income <= 8000000:
        annualtax = 402500 + ((income - 2000000) * 0.3)
        monthlytax = annualtax/12
        print("Your Annual Tax is ", annualtax)
        print("Your Monthly Tax is ", monthlytax)
    else:
        annualtax = 2202500 + ((income - 8000000) * 0.35)
        monthlytax = annualtax/12
        print("Your Annual Tax is ", annualtax)
        print("Your Monthly Tax is ", monthlytax)


yearlytax(annualIncome)
