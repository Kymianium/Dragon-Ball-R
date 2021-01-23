import random

def d(num):
    return random.randint(1,num)

def clear():
    for i in range(0,100):
        print('\n')

def process_input(str, values):
    while(True):
        print(str)
        action = input()
        if action.lower() in values:
            return action.lower()
        else:
            print("La opción seleccionada no es válida.")
