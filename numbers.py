guessing_number=18
countoften=1

while countoften<=10:
    print ("guess the number")
    userinput =int (input())
    if userinput >18:
        print ("your entered number is large")
    elif userinput <18:
        print ("your entered number is less")
    elif userinput==18:
        print ("iam a crt value inserted")
        print ("you have won",countoften,"life")
    print (10-countoften,"life's left")
    countoften =countoften+1
if countoften>10:
    print ("you lose")
        