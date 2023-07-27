import random
number = random.randint(1,100)
attempts=0
operator = input("Enter your name: ")
counter =0
while True:
    operation=int(input("enter number"))
    if operation>number:
        print("Too big")
        attempts+=1
        continue

    else:
        attempts+=1
        print("Congratulations you guessed the number {number} in {attempts} attempts")
         
    break    

    