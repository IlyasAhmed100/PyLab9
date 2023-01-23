# Task 9.1

# The Weight Function 

# Introduction 

print("This programme will convert a chosen weight given by you into a different weight measurement. The choices are between:" '\n' "Kilograms (kg)" '\n' "Pounds (lbs)" '\n' "Stones (st)")
# Getting The User To Input A Measurement To Convert From One Unit To Another
def main():
    measurementAmount = int(input("Please input a measurement value to convert: "))
    sourceUnit = str(input("Please input the units of this measurement"))
    targetUnit = str(input("Please input the target units of this measurement"))

    if sourceUnit == "cm" or sourceUnit == "in" or sourceUnit == "m":
        convertLength (measurementAmount, sourceUnit, targetUnit)
    elif sourceUnit == "kg" or sourceUnit == "lbs" or sourceUnit == "st":
        convertWeight (measurementAmount, sourceUnit, targetUnit)
    

# Defining the Length Conversion 
def convertLength (measurementAmount, sourceUnit, targetUnit):
# If The sourceUnit is Centimetres, Convert To Other Units
    if sourceUnit == "cm":
        if targetUnit == "in":
            measurementAmount = measurementAmount * 0.3937007874
        elif targetUnit == "m":
            measurementAmount = measurementAmount * 0.01
        else:
            measurementAmount = -1
# If The SourceUnit Is Inches, Convert To Other Units
    elif sourceUnit == "in":
        if targetUnit == "cm":
            measurementAmount = measurementAmount * 2.54
        elif targetUnit == "m":
            measurementAmount = measurementAmount * 0.0254
        else:
            measurementAmount = -1
# If The SourceUnit Is Metres, Convert To Other Units
    elif sourceUnit == "m":
        if targetUnit == "cm":
            measurementAmount = measurementAmount * 100
        elif targetUnit == "in":
            measurementAmount = measurementAmount * 39.37007874
        else:
            measurementAmount = -1
    else:
        measurementAmount = -1

    if measurementAmount == -1:
        print("This is invalid")
    else:
        print("Your conversion is " + str(measurementAmount) + " " + targetUnit + ".")   

# Defining The Weight Conversion
def convertWeight (measurementAmount, sourceUnit, targetUnit):
# If The sourceUnit is Kilograms, Convert To Other Units
    if sourceUnit == "kg":
        if targetUnit == "lbs":
            measurementAmount = measurementAmount * 2.2046244202
        elif targetUnit == "st":
            measurementAmount = measurementAmount * 0.1574730444
        else:
            measurementAmount = -1
    elif sourceUnit == "lbs":
        if targetUnit == "kg":
            measurementAmount = measurementAmount * 0.45359237
        elif targetUnit == "st":
            measurementAmount = measurementAmount * 0.0714285714
        else:
            measurementAmount = -1
    elif sourceUnit == "st":
        if targetUnit == "kg":
            measurementAmount = measurementAmount * 6.35029318
        elif targetUnit == "lbs":
            measurementAmount = measurementAmount * 14
        else:
            measurementAmount = -1
    else:
        measurementAmount = -1

    if measurementAmount == -1:
        print("This is invalid")
    else:
        print("Your conversion is " + str(measurementAmount) + " " + targetUnit + ".")                 
main()               
                        
                        
                    
                        
                    


                


