"""
Tyler Marchiano
SSW 567
HW01: Testing Triangle Classification
09.10.2021
"""
import sys
import unittest 

def classify_triangle(a, b, c):
    """
    Function that takes 3 numbers as input and returns if these 3 numbers are the sides of a 
    equilateral, isosceles, scalene, or right triangle
    """
    result = ""
    #Right triangle if a^2 + b^2 = c^2
    if a**2 + b**2 == c**2:
        result += "Right "
    
    #Equilateral if all side are equal
    if a == b == c:
        result += "Equilateral Triangle"
    #Isosceles if two sides are equal
    elif a == b != c or a == c != b or b == c != a:
        result += "Isosceles Triangle"
    #Scalene if no sides are equal
    else:
        result += "Scalene Triangle"
    
    return result

def main() -> None:
    '''Main function that prompts user for 3 sides of a triangle'''
    try: 
        a: float = float(input('Please enter the first side of the triangle: '))
        b: float = float(input('Please enter the second side of the triangle: '))
        c: float = float(input('Please enter the third side of the triangle: '))
    except:
        print('Error: You have entered invalid input. Input needs to be an number!')
        sys.exit(0)
    
    #Make sure all inputs are positive
    if a > 0 and  b > 0 and c > 0:
        print(classify_triangle(a, b, c))
    else:
        print('Error: All inputs must be positive!')
        sys.exit(0)


if __name__ == "__main__":
    print()
    print("Running main()....")
    main()

