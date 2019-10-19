# Name of code: simpleRPG
# Author of code: Alec J. Davidson
# Version of the code and the date of it’s last revision: 9001 10/19/19
# Summary/Goal of the code: This is a simple text RPG battle game I wrote for fun.

### List of imports ###
import math # Allows the further mathmatical computation.
import random # Allows the generation of random numbers.

### What this RPG needs to be able to do. ###

# Create a hero class that asks the player to name the hero and defines
# the hero's stats such as name, hp, attack, defense, level, exp, and move set.

class Hero:
	def __init__(self,name,hp,attack,defense,level,exp):
		self.name = name
		self.hp = hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.exp = exp
# Inherits from the Hero class to create the Hero character.
hero = ('Hero',50,5,3,1,0)

# Create the Hero's move set.

class Hero_Moves:
	def __init__(self,move_name,hp_taken):
		self.move_name = move_name # Name of the attack.
		self.hp_taken = hp_taken # Amount of hp that gets taken.
slash = ('slash',5) # Attack name is slash, takes 5 hp from enemy.
defend = ('defend',0) # Attack name is defend, takes 0 hp from enemy. Reduces damage taken.
cure = ('cure',2)
hero_move_list = [slash,defend,cure] # Stores the hero's moves in a list.

# Create an enemy class that defines the same stat parameters for the enemies.

class Enemy:
	def __init__(self,name,hp,attack,defense,level,exp):
		self.name = name
		self.hp = hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.exp = exp
# Inherits from the Hero class to create the Hero character.
enemy_list = [] # Creates a list to store the enemies in.
goblin = ('Goblin',30,4,2,1,0) # Creates the Goblin enemy.
enemy_list.append(goblin) # Adds goblin to list of enemies.

ghoul = ('Ghoul',30,4,2,1,0) # Creates the Ghoul enemy.
enemy_list.append(ghoul) # Adds goblin to list of enemies.

troll = ('Troll',30,4,2,1,0) # Creates the Troll enemy.
enemy_list.append(troll) # Adds goblin to list of enemies.
#print(enemy_list[0],enemy_list[1],enemy_list[2]) # Tests append of enemy list.


# Create the Enemies moves set.

class Enemy_Moves:
	def __init__(self,move_name,hp_taken):
		self.move_name = move_name # Name of the attack.
		self.hp_taken = hp_taken # Amount of hp that gets taken.
flail = ('flail',5) # Attack name is flail, takes 5 hp from enemy.
defend = ('defend',0) # Attack name is defend, takes 0 hp from enemy. Reduces damage taken.
enemy_move_list = [flail,defend] # Stores enemy moves in a list.

# Create 5 Dungeons starting at level 1 and going up to level 25.

# Create a way for the player to encounter a random enemy.
def enemy_encounter():
	chance = random.randint(0,len(enemy_list)) # Generates a random integer based on how many enemies there are.
	if chance == 0:
		enemy_selected = goblin
	if chance == 1:
		enemy_selected = ghoul
	if chance == 2:
		enemy_selected = troll
	return(enemy_selected)

def enemy_decision():
	enemy_atk = random.randint(0,len(enemy_move_list))
	return enemy_atk # Returns the enemies attack.

# Create a battle sequence
def battle_sequence():
	enemy = enemy_encounter() # Assigns the returned value of the enemy_encounter function to the enemy variable.
	print('Your enemy is a(n) ',enemy) # Alerts user of the type of enemy.
	hero_hp = hero[1] # Assigns the hero classes hp to mutable variable.
	enemy_hp = enemy[1] # Assigns the selected enemies hp to mutable variable.
	while hero_hp and enemy_hp != 0:
		print('Hero HP',hero_hp) # Prints current hp level of hero.
		print('Enemy HP',enemy_hp) # Prints current hp level of enemy.
		print('Move List:')
		print(hero_move_list)
		hero_atk = input('What move would you like to use?')
		if hero_atk == '0':
			print('Hero used slash!')
			hero_atk = hero_move_list[0] # slash
			enemy_hp = enemy_hp - slash[1] # Subracts the attack damage from the enemies hp.
		if hero_atk == '1':
			print('Hero used defend!')
			hero_atk = hero_move_list[1] # defend
		if hero_atk == '2':
			print('Hero used cure!')
			hero_atk = hero_move_list[2] # cure
			hero_hp = hero_hp + cure[1] # Adds cure value to the hero's health.
			if hero_hp >= hero[1]: # Prevents healing past the HP limit
				hero_hp = hero[1]
		enemy_atk = enemy_decision()
		if enemy_atk == 0:
			print(enemy,'used flail!')
			enemy_atk = enemy_move_list[0] # flail
			hero_hp = hero_hp - flail[1] # Subracts the attack damage from the enemies hp.
		if enemy_atk == 1:
			print(enemy,'used defend!')
			enemy_atk = enemy_move_list[1] # defend


	if hero_hp == 0:
		print('You Died!')
	if enemy_hp == 0:
		print('You killed the ',enemy)

# Once the battle is over, update the character.

# Create a menu that allows the player to start a new game, and manage
# the below functions that make the game playable.

def game_menu(): # Defines game menu function.
	### Welcome statement ###
	print('Welcome to my simple dungeon crawler rpg!')
	print(''''I hope that you like to grind because that's''')
	print('all that you do in this game! ver. 1.0')
	### Would you like to start a new game? ###
	start_game = input('''Would you like to start a new game? (y/n) ''')
	if start_game == 'n':
		exit() # Calls the game meny function to reset the game.
	if start_game == 'y':
		print('You will now start the game!')
		print('You have now encountered and enemy')
		battle_sequence()
	else:
		print('''That is not a valid response. Please enter 'y' or 'n'.''')
game_menu()