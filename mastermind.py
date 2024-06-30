import random
dig = random.randrange(1000, 10000)
 
D = int(input("Guess the 4 digit number:"))
if(D == dig):
    print("WOW!...you guessed it right in single try !! You're a Mastermind!")
else:
    ctr = 0
    while(D != dig):
        ctr += 1
        count = 0
        D = str(D)
        dig = str(dig)
        correct = []
        for i in range(0, 4):
            if(D[i] == dig[i]):
                count += 1
                correct.append(D[i])
            else:
                continue
        if (count < 4) and (count != 0):
            print("Not quite the number. But you did get ",
                  count, " digit(s) correct!")
            print("Also these numbers in your input were correct.")
 
            for k in correct:
                print(k, end=' ')
            print('\n')
            print('\n')
            D = int(input("Enter your next choice of numbers: "))
        elif(count == 0):
            print("None of the numbers in your input match.")
            D = int(input("Enter your next choice of numbers: "))
    if D == dig:
        print("You've become a Mastermind!")
        print("It took you only",ctr,"tries")