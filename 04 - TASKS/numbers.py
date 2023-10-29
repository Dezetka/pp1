

def check_numbers():
    x = int(input('Enter the first number of range:'))
    y = int(input('Emter the second number of range:'))
    n = int(input('Enter the number you want to check if it belongs to the range:'))
    
    if n in range(x,y):
       z = True
       print(f'Number {n} in range <{x},{y}>:',z)
    else:
        z = False
        print(f'Number {n} in range <{x},{y}>:', z)

