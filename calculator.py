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
            result = 0
            for i in range(1, len(token)):
                print(i)
                result = add(result, float(token[i]))

            result = (add(float(token[1]), float(token[2])))
        
        elif token [0] == '-':
            result = (subtract(float(token[1]), float(token[2])))
            
        elif token [0] == '*':
            result = (multiply(float(token[1]), float(token[2])))

        elif token [0] == '/':
            result = (divide(float(token[1]), float(token[2])))

        elif token [0] == 'square':
            result = (square(float(token[1])))
            
        elif token[0] == 'cube':
            result = (cube(float(token[1])))

        elif token[0] == 'pow':
            result = (power(float(token[1]), float(token[2])))

        elif token[0] == 'mod':
            result = (mod(float(token[1]), float(token[2])))
            
        else:
            print("Selection not valid")
            result = 0
        print(result)