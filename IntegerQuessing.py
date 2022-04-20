#Try to quess random int in range from 1 to Random_Range_Int

#Importing random
from random import randint

#Range upper limit

Random_Range_Int = 5

RandomInt = randint(1, Random_Range_Int)

UserQuess = -1

#Table to keep users quesses history
UserQuessHistory =[]

print('Try to quess a number between 1 and', Random_Range_Int)


while UserQuess != RandomInt:
    UserQuess = int(input('Your quess: '))
    UserQuessHistory.append(UserQuess) #Keep UserQuess in history table
    print('Please try again, your recent quesses:', UserQuessHistory)
print('Great job. The random number is', UserQuess)
