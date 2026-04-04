# Note always make sure use ```eval()``` with precaution and input sanitations
def is_valid_equation(equation):
    # Define allowed characters to ensure security before using eval()
    allowedOperators = set("/*+- ") 
    
    # Split the string into the expression (lhs) and the expected result (rhs)
    lhs = equation.split("=")[0]
    rhs = equation.split("=")[1]
      
    # Identify unique characters in the lhs that are not operators or spaces
    lhsSet = set(lhs) - allowedOperators
    
    # Ensure there are between 1 and 4 unique digits/characters
    less4 = 4 >= len(lhsSet) > 0
    equ1 = int(rhs)
    
    # Check if the extracted characters are actual digits and rhs is an integer
    allDigit = all(item.isdigit() for item in lhsSet) and (type(equ1) == int)
    
    if allDigit:
        # Calculate the mathematical result of both sides and compare
        result = eval(lhs) == eval(rhs)
        print(eval(lhs)) # Print actual calculation for debugging
        return result
    else:
        # Return False if non-digit characters (other than allowed operators) are found
        return False
