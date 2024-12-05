# Error Handling - pdb, syntax(forgetting a :), Nameerror - things arent defined, typeerror, keyerror, zerodivision

while True:
    try:
        age = int(input('What is your age? '))
        print(age)
        10/age
    except ValueError as err: #doesnt handling dividing by 0, just if a string
        print(f'Please enter a number {err}')
    except ValueError:
        print("!!!") #never executes because it only runs once and goes back to the while loop
    except ZeroDivisionError: #handles dividing by 0
        print("please enter a number")
    else:
        print("Thanks")
        break
    finally: #no matter what do this
        print("Okay Im done")

#raise ValueError("hey cut it out")
#can use this to stop the program from running, dont use the except block

import pdb
def add(num1, num2):
    pdb.set_trace()
    t = 4*5
    return num1 + num2

add(4, 'hsdfsaf')
