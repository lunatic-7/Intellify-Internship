# # Question 1 (Python):

# # Write a python function to give the frequency of digits appearing after the decimal place.

# # Using inbuilt decimal library, to take larger decimal places as well.
from decimal import *

def give_remainder_dict(dividend, divisor, number_of_digits):
    # Using try except error handling to avoid any arbitrary input.
    try:
        cdiv = dividend / divisor
        occur = {}
        # Handling completely divisible inputs
        if int(cdiv) == cdiv:
            occur[0] = number_of_digits
            print(occur)
        # Handling output with some decimal places
        else:
            # Setting precision
            getcontext().prec = number_of_digits
            # Taking value as a string, to split it later on
            value = str(Decimal(dividend) /Decimal(divisor))
            # Splitting the string into decimal and non decimal part.
            # b is the part after decimal
            a,b = value.split(".",1)
            occurances = {}
            
            # Counting no. of occurances of digits appearing after the decimal place, and appending it to a dictionary.
            for _ in b:
                if int(_) in occurances:
                    occurances[int(_)] += 1
                else:
                    occurances[int(_)] = 1
                # Setting occurance of 0
                occurances[0] = number_of_digits - len(b)
                # printing final answer
            print(occurances)
    except:
        # print,if any error occurs.
        print("Some error occured, Check your inputs!")

give_remainder_dict(100,25,10)
