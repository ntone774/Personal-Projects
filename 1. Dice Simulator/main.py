import random

valueAi = [1, 2, 3, 4, 5, 6]
valuePlayer = [1, 2, 3, 4, 5, 6]
aiWinCount = 0
playerWinCount = 0
drawCount = 0

print('Hello, my name is AI and this is Dice Simulator')
name = input('Can you tell me what is your name?')
print(f'Hi, {name}!\nYou are playing Dice Simulator against me. \nIf you roll  higher number than me three times you '
      f'win. '
      f'Otherwise I win')
print('[-----------]')
print('[  0     0  ]')
print('[     0     ]')
print('[ 000000000 ]')
print('[-----------]')

insertCommand = input('Press Y to roll')

while True:
    scoreAi = random.choice(valueAi)
    scorePlayer = random.choice(valuePlayer)

    print('I threw :')
    if scoreAi == 1:
        print('[-----------]')
        print('[           ]')
        print('[     0     ]')
        print('[           ]')
        print('[-----------]')
    elif scoreAi == 2:
        print('[-----------]')
        print('[ 0         ]')
        print('[           ]')
        print('[         0 ]')
        print('[-----------]')
    elif scoreAi == 3:
        print('[-----------]')
        print('[ 0         ]')
        print('[     0     ]')
        print('[         0 ]')
        print('[-----------]')
    elif scoreAi == 4:
        print('[-----------]')
        print('[ 0       0 ]')
        print('[           ]')
        print('[ 0       0 ]')
        print('[-----------]')
    elif scoreAi == 5:
        print('[-----------]')
        print('[ 0       0 ]')
        print('[     0     ]')
        print('[ 0       0 ]')
        print('[-----------]')
    elif scoreAi == 6:
        print('[-----------]')
        print('[ 0       0 ]')
        print('[ 0       0 ]')
        print('[ 0       0 ]')
        print('[-----------]')

    print('You threw :')
    if scorePlayer == 1:
        print('[-----------]')
        print('[           ]')
        print('[     0     ]')
        print('[           ]')
        print('[-----------]')
    elif scorePlayer == 2:
        print('[-----------]')
        print('[ 0         ]')
        print('[           ]')
        print('[         0 ]')
        print('[-----------]')
    elif scorePlayer == 3:
        print('[-----------]')
        print('[ 0         ]')
        print('[     0     ]')
        print('[         0 ]')
        print('[-----------]')
    elif scorePlayer == 4:
        print('[-----------]')
        print('[ 0       0 ]')
        print('[           ]')
        print('[ 0       0 ]')
        print('[-----------]')
    elif scorePlayer == 5:
        print('[-----------]')
        print('[ 0       0 ]')
        print('[     0     ]')
        print('[ 0       0 ]')
        print('[-----------]')
    elif scorePlayer == 6:
        print('[-----------]')
        print('[ 0       0 ]')
        print('[ 0       0 ]')
        print('[ 0       0 ]')
        print('[-----------]')

    if scoreAi > scorePlayer:
        aiWinCount += 1
        print('Yes, I win a point!!')
        print(f'AI: {aiWinCount}, {name}: {playerWinCount}, Draws: {drawCount}')
    elif scoreAi < scorePlayer:
        playerWinCount += 1
        print('Damn, point for you!')
        print(f'AI: {aiWinCount}, {name}: {playerWinCount}, Draws: {drawCount}')
    elif scoreAi == scorePlayer:
        drawCount += 1
        print('It is a draw. Nobody wins a point')
        print(f'AI: {aiWinCount}, {name}: {playerWinCount}, Draws: {drawCount}')

    if aiWinCount == 3:
        print("Yes, i won!!! Better luck next time.")
        print(f'AI: {aiWinCount}, {name}: {playerWinCount}, Draws: {drawCount}')
        break
    elif playerWinCount == 3:
        print("Ohh no, You win! You are just too god")
        print(f'AI: {aiWinCount}, {name}: {playerWinCount}, Draws: {drawCount}')
        break

    print('Do you want to play one more time')
    questionF = input('Type y for Yes or n for No')

    if questionF == 'y':
        continue
    else:
        print('Thank you for playing with me! See you later!')
        break