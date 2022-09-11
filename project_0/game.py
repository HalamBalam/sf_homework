import numpy as np

number = np.random.randint(1, 101)

count = 0

while True:
    count += 1
    predict_number = int(input("Guess number from 1 to 100: "))
    
    if predict_number > number:
        print("Number must be less!")
        
    elif predict_number < number:
        print("Number must be bigger!")
        
    else:
        print(f"You guess the number! This number is {number}, counts = {count}")
        break