# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
goal_0 = 32
goal_1 = 54
player0 = 'Ruud Gullit'
player1= 'Marco van Basten'
scorers = player0 +' '+ str(goal_0) +', ' + player1 + ' ' +str(goal_1)
#scorers = f'{player0} {goal_0}, {player1} {goal_1}'
report = f"""{player0} scored in the {goal_0}nd minute
{player1} scored in the {goal_1}th minute"""

player = 'Frank Rijkaard'
x = str.split(player)

first_name = x[0]

last_name_len = len(x[1])
last_name = x[1]
name_short = f'{player[0]}. {last_name}'

chant_0= (f'{first_name}! ' * len(first_name))
chant = chant_0[0:len(chant_0)-1]
good_chant = (chant[len(chant)-1] != ' ')

