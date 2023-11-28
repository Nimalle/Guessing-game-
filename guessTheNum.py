

import sys 
import random 

def guess_number(name = 'PlayerOne'):
    game_count = 0 
    player_wins = 0 
        
    def player_guess_number():
        nonlocal name
        nonlocal player_wins
            
        playerchoice = input(f'\n{name} guess which number i am thinking of retard..... 1, 2 or 3')
            
        if playerchoice not in ['1', '2', '3']:
            print(f'{name}, whatever you said is not what I ASKED FOR!!')
            return player_guess_number
            
            computerchoice = random.choice('123')
            
            print(f'{name} you picked {playerchoice}.')
            print(f'I was thinking about the number {computerchoice}')
            
            player = int(playerchoice)
            computer = int(computerchoice)
            
            def decide_winner(player,computer):
                nonlocal name 
                nonlocal player_wins
                
                if player == computer:
                    player_wins += 1 
                    return f'You win {name}'
                else:
                    return f'sorry, {name} better luck next time'
                game_result = decide_winner (player,computer)
                
                print(game_result)
                
                nonlocal game_countgame
                game_count += 1
                
                print(f'Game count: {game_count}')
                print(f'\n{name}s wins : {player_wins}' )
                print(f'\n Your winning percentage : {player_wins/game_count:.2%}' )
                
                print(f'\n Play again? : {name}')
                
                while True: 
                    playagain = input('\nY for Yes or \nN for No ')
                    if playagain.lower() not in ['y', 'n']:
                        continue
                    else: 
                        break
                    if playagain.lower() == 'y':
                        return player_guess_number
                    else:
                        print('Thank you for playing')        
                        if __name__ == '__main__':
                            sys.exit(f'Bye loser {name}')
                        else:
                            return
                return player_guess_number
            
if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(
        description = 'Provides a personalised game experience i think or whatever' 
    )    
    
    parser.add_argument('-n', '--name ', metavar = 'name',
        required = True, help = 'The name of the person playing the game.'
    )

        
    args = parser.parse_args()
    
    guess_my_number = guess_number(args.name)
    guess_my_number()
