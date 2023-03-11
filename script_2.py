from script_1 import converterC, converterF, converterK
userInput = str(input("Enter temperature and unit: "))
input = userInput.split(" ")
temp = int(input[0])
unit = str(input[-1])
if unit == 'C':
    converterC(temp)
elif unit == 'F':
    converterF(temp)
elif unit == 'K':
    converterK(temp)
else:
    print("Error! Invalid Input")
