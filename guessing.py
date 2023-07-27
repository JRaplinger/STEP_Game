import random
number = random.randint(1,100)
operator = input("Enter your name: ")
counter =0
low= 1
mid=(low+high)/2
high=100
attempts=0
while True:
    if number==mid:
        print("Congrats")
        break
   
    elif number<mid:
        high=mid-1
        attempts+=1
        mid=(low+high)/2
        

    else:
        low=mid+1
        attempts+=1
      