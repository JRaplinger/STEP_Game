attempts=0
defaultpassword="JacobR"
username="Jacob"
while True:
    usernameinput= input("what is the username?")
    userinput= input("what is the defaultpassword?")
    if username==username and userinput==defaultpassword:
        print("Correct") 
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
            else:
	        print(num1/num2)	
    	else:
            print("Wrong Try Again")
            attempts+=1
    	    if attempts==5:
        	print("too many tries")
        	break
        
               
   