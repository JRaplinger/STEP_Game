attempts=0
defaultpassword="JacobR"
while True:
    
    userinput= input("what is the defaultpassword?")
   
    if userinput==defaultpassword:
        print("Welcome")
        break
        
    else:
        print("Wrong Try Again")
        attempts+=1
    if attempts==5:
        print("too many tries")
        break
        
               
   