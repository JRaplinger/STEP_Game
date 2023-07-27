while True:
    num1= float(input("Enter num1: "))
    num2= float(input("Enter num2: "))
    operator = input("Enter the operation +,-,*,/")
    if operator=="*":
	          print(num1*num2)
    elif operator== "+":
		    print(num1+num2)
    elif operator == "-":
		    print(num1-num2)
    elif operator== "/":
		    if(num2==0):
			     print("can't divide by zero")
		    else:print(num1/num2)	
    else:
	    print("Invalid operator. Please try again.")  
    continue

