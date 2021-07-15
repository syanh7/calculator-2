"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

from functools import reduce 

while True:

    """Gets input from user
    splits the user input by space
    and puts it in the token list"""
    input_string = input("Enter your equation")
    token = input_string.split(' ')

    


    if token[0] == 'q':
        """checks if token at index 0
        is 'q', will quit program if it is"""
        break

    else:
        if token[0] == '+':
            """if the user selects addition 
            first this will set result at token
            index 1, then iterate through the rest
            of the list, passing the previous result
            and next item in list as args to add function"""
            result = float(token[1])
            for i in range(2, len(token)):
                result = add(result, float(token[i]))
        
        elif token [0] == '-':
            """user selects subtraction, program passes
            two args to subtract function until token
            list is exhusted"""
            result = float(token[1])
            for i in range(2, len(token)):
                result = subtract(result, float(token[i]))
            
        
        elif token [0] == '*':
            """user selects multiply, program passes
            two args to multiply function until token
            list is exhusted"""
            result = float(token[1])
            for i in range(2, len(token)):
                result = multiply(result, float(token[i]))

        elif token [0] == '/':
            """user selects div, program passes
            two args to div function until token
            list is exhusted"""
            result = float(token[1])
            for i in range(2, len(token)):
                result = divide(result, float(token[i]))

        elif token [0] == 'square':
            """Send token at index 1 to
            square func and gets result back"""
            result = square(float(token[1]))
            
        elif token[0] == 'cube':
            """Sends token at index 1 to
            cube func and gets result back"""
            result = cube(float(token[1]))

        elif token[0] == 'pow':
            """program passes two args to 
            mod function until token
            list is exhusted"""
            result = float(token[1])
            for i in range(2, len(token)):
                result = pow(result, float(token[i]))

        elif token[0] == 'mod':
            """program passes two args to 
            mod function until token
            list is exhusted"""
            result = float(token[1])
            for i in range(2, len(token)):
                result = mod(result, float(token[i]))
            
        else:
            print("Selection not valid")
            result = 0
        print(result)