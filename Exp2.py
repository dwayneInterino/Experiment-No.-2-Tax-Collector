monthIncome = int(input("Enter your monthly income: "))
annualIncome = monthIncome*12


def yearlytax(income):
    if income <= 250000:
        print("Your Annual Tax is 0")
        print("Your Monthly Tax is 0")
    elif income > 250000 & income <= 400000:
        annualtax = (income - 250000) * 0.15
        monthlytax = annualtax/12
        print("Your Annual Tax is ", annualtax)
        print("Your Monthly Tax is ", monthlytax)
    elif income > 400000 & income <= 800000:
        annualtax2 = 22500 + ((income - 400000) * 0.2)
        monthlytax2 = annualtax2/12
        print("Your Annual Tax is ", annualtax2)
        print("Your Monthly Tax is ", monthlytax2)
    elif income > 800000 & income <= 2000000:
        annualtax3 = 102500 + ((income - 800000) * 0.25)
        monthlytax3 = annualtax3/12
        print("Your Annual Tax is ", annualtax3)
        print("Your Monthly Tax is ", monthlytax3)
    elif income > 2000000 & income <= 8000000:
        annualtax4 = 402500 + ((income - 2000000) * 0.3)
        monthlytax4 = annualtax4/12
        print("Your Annual Tax is ", annualtax4)
        print("Your Monthly Tax is ", monthlytax4)
    else:
        annualtax5 = 2202500 + ((income - 8000000) * 0.35)
        monthlytax5 = annualtax5/12
        print("Your Annual Tax is ", annualtax5)
        print("Your Monthly Tax is ", monthlytax5)


yearlytax(annualIncome)
