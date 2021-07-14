"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

from functools import reduce 

while True:
    input_string = input()
    token = input_string.split(' ')

    


    if token[0] == 'q':
        break
    else:
        if token[0] == '+':
            result = float(token[1])
            for i in range(2, len(token)):
                result = add(result, float(token[i]))

            #result = (add(float(token[1]), float(token[2])))
        
        elif token [0] == '-':
            result = float(token[1])
            for i in range(2, len(token)):
                result = subtract(result, float(token[i]))
            
        
        elif token [0] == '*':
            result = float(token[1])
            for i in range(2, len(token)):
                result = multiply(result, float(token[i]))

        elif token [0] == '/':
            result = float(token[1])
            for i in range(2, len(token)):
                result = divide(result, float(token[i]))

        elif token [0] == 'square':
            result = square(float(token[1]))
            
        elif token[0] == 'cube':
            cube(float(token[1]))

        elif token[0] == 'pow':
            result = float(token[1])
            for i in range(2, len(token)):
                result = pow(result, float(token[i]))

        elif token[0] == 'mod':
            result = float(token[1])
            for i in range(2, len(token)):
                result = mod(result, float(token[i]))
            
        else:
            print("Selection not valid")
            result = 0
        print(result)