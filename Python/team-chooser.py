from random import choice

players = ['Harry', 'Hermione', 'Neville', 'Ginny']
print(players)

# define the teams
team_A = []
team_B = []

player_A = choice(players)
print(player_A)
team_A.append(player_A)
players.remove(player_A)
print('Players left: ', players)

player_B = choice(players)
print(player_B)
team_B.append(player_B)
players.remove(player_B)
print('Players left: ', players)

print('Team A', team_A)
print('Team B', team_B)


print(players[0])
print(players[1])

print(choice(players))