import random as r
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
choices = [rock, paper, scissors]
player = int(input('1.rock\n2.paper\n3.scissors\n'))
cpu = choices[r.randint(0,2)]
if player == 0 and cpu == 0:
    print('player\n')
    print(choices[player])
    print('CPU\n')
    print(choices[cpu])
    print('Draw')
elif player == 0 and  cpu == 1:
    print('player\n')
    print(choices[player])
    print('CPU\n')
    print(choices[cpu])
    print('You lose')
elif player == 0 and cpu == 2:
    print('player\n')
    print(choices[player])
    print('CPU\n')
    print(choices[cpu])
    print('You win')
elif player == 1 and cpu == 0:
    print('player\n')
    print(choices[player])
    print('CPU\n')
    print(choices[cpu])
    print('You win')
elif player == 1 and cpu == 1:
    print('player\n')
    print(choices[player])
    print('CPU\n')
    print(choices[cpu])
    print('Draw')
elif player == 1 and cpu == 2:
    print('player\n')
    print(choices[player])
    print('CPU\n')
    print(choices[cpu])
    print('You lose')
elif player == 2 and cpu == 0:
    print('player\n')
    print(choices[player])
    print('CPU\n')
    print(choices[cpu])
    print('You lose')
elif player == 2 and cpu == 1:
    print('player\n')
    print(choices[player])
    print('CPU\n')
    print(choices[cpu])
    print('You win')
elif player == 2 and cpu == 2:
    print('player\n')
    print(choices[player])
    print('CPU\n')
    print(choices[cpu])
    print('Draw')