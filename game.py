#The concepts used are-
# functions(callback)
# lopping(if, while and nesting)
# string functions (s.lower)
# user input function
# 'random' module



print('''
MASTERMIND - A mini python project
----------------------------------
                                    by  -Rohan Sharma
                                        -Vishal Angadi
                                        -Rohan Ajay
                                        
                                    

This is a classic Mastermind game, but instead of colors we use numbers.
The computer generates a random 4-digit number, which the user has to guess.
After each guess the user is given two numbers, first is 'postion' and second
is 'numbers'. The position number tells how many numbers from the user's guess are
correct and in the right position. The numbers number tells the user how many digits
in the guess are correct but in the wrong position.
User is given 10 chances to guess right.

If you are manally entering a number, then your number should -
> Have non-repetitive digits
> Not start with zero

Have fun playing!
\n
''')
import random


def game():
    print("Would you like the system to generate a number for you or would you like to manually enter one?")
    a=input("Enter 1 for system and 2 for manual : ")       #user specifies his choice


    while a!='1' and a!='2'  :       #1 ...and a=='2'
            a=input("Enter either '1' or '2': ")                           

    if a=='2':                                                       #manual entering and validation
            number=input("Enter a 4 digit number: ")
            
            while len(number)!=4:
                number=input("Please enter a 4 digit number only: ")                        


            if len(number)==4:
                for digit in number:
                    if digit.isdigit()==False:
                        number=input("Please enter a valid number: ")
                if number[0]=='0':                  #2 if number[1]=='0'
                    number=input("First digit cannot be 0, please enter valid number: ")
                    
                s=set(number)
                while len(s)<4:
                    number=input("Plese do not repeat digits: ")
                    if len(number)==4:
                        break
                    if len(number)!=4:
                        number=input("Enter 4 non-repeating digits: ")
            
    
            
            
    elif a=='1':                                        #system generates the number
            l=[]
            number=""
            l.append(random.randrange(1,10))
            while len(l)<4:
                num=random.randrange(0,10)
                if num not in l:
                    l.append(num)
            for i in l:
                number+=str(i)
                    
                        
    '''
    The number to be guessed is ready by this point
    '''

    print('\n'*100)                                   #so that the manually entered number is hidden from player
    guesscount=10                                    #user gets 10 guesses
    
    while guesscount>0:
        positions=0     #3 positions=1                                 #correct position count
        numbers=0                                   #number and posy_orition correct count
        
        guess=input("Enter your guess: ")           #guess input

        while guess.isdigit()==False:               #validating input
            guess=input("Please enter a 4 digit number guess: ")        #4 int()


            

        if len(guess)!=4:
            guess=input("Enter a 4 digit guess: ")


        if len(guess)==4:                           #number and position checking
            for i in range(4):
                if guess[i]==number[i]:
                    positions+=1
                    numbers-=1
            for digit1 in number:
                for digit2 in guess:
                    if digit1==digit2:
                        numbers+=1
            
            print("Guess no.",11-guesscount,"\n",guess,": positions:",positions,"\tnumbers: ",numbers,'\n\n')


        if guess==number:                                       #if guess is right
            print('{:-^133}'.format("Congrats, you have guessed correctly!"))
            print("Would you like to play again?")
            y_or_n=input("Y/N : ")
            break  
        
        guesscount-=1

    if guesscount==0:
        print("You ran out of guesses!")
        print("The correct number is",number)
        print("\n\nWould you like to play again?")
        y_or_n=input("Y/N : ")
            

    while y_or_n.lower()!='Y' and y_or_n.lower()!='n':              #validating input
        y_or_n=input("Enter 'Y' or 'N' : ")         #5 int()
    if y_or_n.lower()=='n':
        print('{:-^133}'.format("Thank you for playing!".upper()))  #quit
    if y_or_n.lower()=='y':                                         #continue
        game()



game()





















