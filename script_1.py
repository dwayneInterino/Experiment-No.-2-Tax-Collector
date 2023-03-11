def converterC(temp):
    convert = str(input("Convert it into F or K? "))
    if convert == 'F':
        tempConvert = (temp*(9/5))+32
        print("{0} C converted to {1} F".format(temp, tempConvert))
    elif convert == 'K':
        tempConvert = temp + 273.15
        print("{0} C converted to {1} K".format(temp, tempConvert))
    else:
        print("Error! Invalid Input")


def converterF(temp):
    convert = str(input("Convert it into C or K? "))
    if convert == 'C':
        tempConvert = (temp - 32)*(5/9)
        print("{0} F converted to {1} C".format(temp, tempConvert))
    elif convert == 'K':
        tempConvert = (temp + -32)*(5/9)+273.15
        print("{0} F converted to {1} K".format(temp, tempConvert))
    else:
        print("Error! Invalid Input")


def converterK(temp):
    convert = str(input("Convert it into C or F? "))
    if convert == 'C':
        tempConvert = temp - 273.15
        print("{0} K converted to {1} C".format(temp, tempConvert))
    elif convert == 'F':
        tempConvert = (temp - 273.15)*(9/5)+32
        print("{0} K converted to {1} F".format(temp, tempConvert))
    else:
        print("Error! Invalid Input")
