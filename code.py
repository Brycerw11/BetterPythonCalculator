print ('Welcome to the Ryandw11 calculator, with improvements from Brycerw11.')

print ('How many problems would you like to solve?')
while True: #Loop until valid int is given
    try:
        num_of_problems = int(input())
        break
    except:
        print("Please input a whole number.")

count = 0
while count < num_of_problems:
    count = count + 1
    print ('Type 1 for addition; 2 for subtraction; 3 for multiplication; 4 for division;)')
    print ('5 for area of a Trapezoid; 6 for area of a Triangle; 7 for area of a Parallelogram; 8 for path or circuit')
    
    while True:
        try:
            c = int(input())
            if c > 9 or c < 0:
                break
        except:
            print("Please input a valid number.")
        
    if c == 1:
        print ('Please enter a number')
        num1 = int(input())
        print ('Please enter another number')
        num2 = int(input())
        awn = (num1 + num2)
        print ('your awnser is:')
        print (awn)
    elif c == 2:
        print ('please enter a number')
        num1 = int(input())
        print ('please put in another number')
        num2 = int(input())
        awn = (num1 - num2)
        print ('your awnser is:')
        print (awn)
    elif c == 3:
        print ('please enter a number')
        num1 = int(input())
        print ('please put in another number')
        num2 = int(input())
        awn = (num1 * num2)
        print ('your awnser is:')
        print (awn)
    elif c == 4:
        print ('please enter a number')
        num1 = int(input())
        print ('please put in another number')
        num2 = int(input())
        awn = (num1 / num2)
        print ('your awnser is:')
        print (awn)
    elif c == 5:
        print ('Please put in base 1')
        b1 = int(input())
        print ('please put in base 2')
        b2 = int(input())
        print ('please put in the height')
        h = int(input())
        a1 = (b1 + b2)
        a2 = (a1 * h)
        awn = (a2 / 2)
        print (' your awnser is:')
        print (awn)
    elif c == 6:
        print ('please enter the base')
        b = int(input())
        print ('please put in the hight')
        h = int(input())
        a1 = (b * h)
        awn = (a1 / 2)
        print ('your awnser is:')
        print (awn)
    elif c == 7:
        print ('please enter the base')
        b = int(input())
        print ('please enter the height')
        h = int(input())
        awn = (b * h)
        print ('your awnser is:')
        print (awn)
    elif c == 8:
        print ('how many points are there?')
        e2 = int(input())
        count2 = 0
        while count2 < e2:
            count3 = count2
            count2 = count2 + 1
            print ('enter a point')
            p = int(input())
            if count3 == 0:
                print ('Enter a point')
                p2 = int(input())
                a = ( p + p2)
            else:
                a = (a + p)
        awn = a
        print (awn)
                
        
    else:
        print ('Error: you did not enter a number or number is not vaild!')
print (' press enter to close/end program.')
end = input()
print ('thank you for using my project!')
