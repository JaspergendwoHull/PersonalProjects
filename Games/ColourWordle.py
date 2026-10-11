```cs
import random

colours = ['red','yellow','green','blue']
answer = []

for x in range(4):
    colour = (random.choice(colours))
    answer.append(colour) 

GameOver = False
while GameOver == False:

    CorrectColours = 0
    CorrectPositions = 0
    answerColours = []
    answerColours.extend(answer)

    print('')
    print('The possible colours in the answer are:',colours)

    print('')
    UserInput1 = input('Enter the 1st colour: ')
    UserInput2 = input('Enter the 2nd colour: ')
    UserInput3 = input('Enter the 3rd colour: ')
    UserInput4 = input('Enter the 4th colour: ')

    if UserInput1 in answerColours:
        CorrectColours += 1
        answerColours.remove(UserInput1)
    if UserInput2 in answerColours:
        CorrectColours += 1
        answerColours.remove(UserInput2)
    if UserInput3 in answerColours:
        CorrectColours += 1
        answerColours.remove(UserInput3)
    if UserInput4 in answerColours:
        CorrectColours += 1
        answerColours.remove(UserInput4)

    if UserInput1 == answer[0]:
        CorrectPositions += 1
    if UserInput2 == answer[1]:
        CorrectPositions += 1
    if UserInput3 == answer[2]:
        CorrectPositions += 1
    if UserInput4 == answer[3]:
        CorrectPositions += 1

    print('')
    print('Number of correct colours present:' ,CorrectColours)
    print('Number of colours in the right place:' ,CorrectPositions)

    if CorrectPositions == 4:
        GameOver = True

print('')
print('Congrats, you win!')
```
