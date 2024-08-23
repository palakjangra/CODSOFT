import random
print('Winnig rules of the game ROCK PAPAER SCISSORS are :\n'
       + "Rock vs Paper -> Paper wins \n"
       + "Rock vs Scissors -> Rock wins \n"
       + "Paper vs Scissors -> Scissor wins \n")

while True:
   
   print("Enter the choice: \n 1-ROCK\n 2-PAPER\n 3-SCISSOR\n")
    
   choice =  int(input("Enter your choice:")) 

   while choice > 3 or choice < 1:
       choice = int(input('Enter a valid choice please '))
         
   if  choice == 1:
            choice_name = 'Rock'
   elif choice == 2:
             choice_name = 'Paper'
   else:
             choice_name = ' Scissor' 

             print('user choice is: \n ' , choice_name)
             print('Now its computers turn.....')
 
   comp_choice = random.randint(1, 3)

   while comp_choice == choice:
              comp_choice = random.randint(1, 3)

   if comp_choice == 1:
         comp_choice_name = 'Rock'
   elif comp_choice == 2:
              comp_choice_name = 'Paper'
   else:
              comp_choice_name ='Scissor'
              print("Computer choice is:\n", comp_choice_name)
              print("Computer choice is \n", comp_choice_name)
              print(choice_name, 'Vs', comp_choice_name)

   if choice == comp_choice:
              print('Its a Draw', end="")
   result = "DRAW"

   if (choice == 1 and comp_choice == 2):
              print('paper wins =>', end="")
              result = 'paper'
   elif (choice == 2 and comp_choice == 1):
              print('paper wins =>', end="")
              result = 'Paper'

   if (choice == 1 and comp_choice == 3):
               print('Rock wins =>\n', end="")
               result = 'Rock'
   elif (choice == 3 and comp_choice == 1):
               print('Rock wins =>\n', end="")
               result = 'RocK'

   if (choice == 2 and comp_choice == 3):
               print('Scissors wins =>', end="")
               result = 'Scissors'
   elif (choice == 3 and comp_choice == 2):
               print('Scissors wins =>', end="")
               result = 'Rock'
    
   if result == 'DRAW':
        print("<== Its a tie ==>")
   if result == choice_name:
        print("<== User wins ==>")
   else:
        print("<== Computer wins ==>")
        print("Do you want to play again? (Y/N)")
    
   ans = input().lower()
   if ans == 'n':
        break
print("thanks for playing")
