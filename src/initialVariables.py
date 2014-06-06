# initialVariables.py

import pygame



# GRAPHIC VARIABLES-------------------------------

SCREEN_DIMENSIONS_X = 1000 #1366
SCREEN_DIMENSIONS_Y = 600 #768
SCREEN_BG_COLOR     = (125,125,100)

screen = pygame.display.set_mode((SCREEN_DIMENSIONS_X, SCREEN_DIMENSIONS_Y), 0, 32)

P_TIMER_FONT_SIZE  = 18
P_TIMER_FONT_COLOR = (255,255,255)
P_TIMER_X          = 4
P_TIMER_Y          = 27

TIMER_FONT_SIZE  = 50
TIMER_FONT_COLOR = (255,255,255)

FPS_FONT_SIZE  = 12
FPS_FONT_COLOR = (255,255,255)

KILLS_FONT_SIZE  = 35
KILLS_FONT_COLOR = (255,255,255)

ENDGAME_FONT_SIZE  = 100
ENDGAME_FONT_COLOR = (255,255,0)

ENDGAME_BG_COLOR = (150,0,0)


# BUTTON VARIABLES--------------------------------

#BUTTON_FONT  = pygame.font.Font('freesansbold.ttf', 14)
#BUTTON_COLOR = (212,208,200)


# GRAPHICS----------------------------------------

bif = "bg.jpg"
mif = "src/ball.png"

#uncomment for custom background
#background = pygame.image.load(bif).convert()

mouse_c = pygame.image.load(mif).convert_alpha()

#keyboard_c = pygame.image.load(mif).convert_alpha()


# OBJECT VARIABLES--------------------------------

# PLAYER

PLAYER_MOVE_SPEED = 2.5
PLAYER_RADIUS     = 25
PLAYER_COLOR      = (0,0,150)

# SHOT_BASIC

SHOT_BASIC_MOVE_SPEED = 14
SHOT_BASIC_RADIUS     = 5
SHOT_BASIC_COLOR      = (255,255,255)

# SHOT_DOUBLE

SHOT_DOUBLE_MOVE_SPEED = 18
SHOT_DOUBLE_RADIUS     = 3
SHOT_DOUBLE_COLOR      = (0,0,150)
SHOT_DOUBLE_TIMER      = 10

# SHOT_CONE

SHOT_CONE_MOVE_SPEED = 7
SHOT_CONE_RADIUS     = 7
SHOT_CONE_COLOR      = (200,20,20)
SHOT_CONE_TIMER      = 7
SHOT_CONE_SPREAD     = 0.02

# POWERUP

POWERUP_RADIUS = 8

# POWERUP_DOUBLE

POWERUP_DOUBLE_RADIUS       = 8
POWERUP_DOUBLE_EXPIRE_TIMER = 7
POWERUP_DOUBLE_COLOR        = (200,200,0)
POWERUP_DOUBLE_SPAWN_RATE   = 10

# POWERUP_CONE

POWERUP_CONE_RADIUS       = 10
POWERUP_CONE_EXPIRE_TIMER = 7
POWERUP_CONE_COLOR        = (200,20,20)
POWERUP_CONE_SPAWN_RATE   = 5

# ZOMBIE

ZOMBIE_MOVE_SPEED  = 2
ZOMBIE_RADIUS      = 14
ZOMBIE_COLOR       = (30,30,30)
ZOMBIE_HP          = 1
ZOMBIE_SPAWN_RATE  = 160
ZOMBIE_SPAWN_DELAY = 0

# GHOUL

GHOUL_MOVE_SPEED  = 2.5
GHOUL_RADIUS      = 18
GHOUL_COLOR       = (160,30,30)
GHOUL_HP          = 2
GHOUL_SPAWN_RATE  = 80
GHOUL_SPAWN_DELAY = 10

GHOUL_ACCELERATE  = 250

# ABOMINATION

ABOM_MOVE_SPEED  = 1
ABOM_RADIUS      = 30
ABOM_COLOR       = (30,150,30)
ABOM_HP          = 5
ABOM_SPAWN_RATE  = 40
ABOM_SPAWN_DELAY = 25

# BAT

BAT_MOVE_SPEED  = 1.5
BAT_RADIUS      = 9
BAT_COLOR       = (0,0,0)
BAT_HP          = 1
BAT_SPAWN_RATE  = 40
BAT_SPAWN_DELAY = 50

BAT_TIMER       = 3
BAT_BOOST_SPEED = 4


# MISCELLANEOUS-----------------------------------

CLOCK_TICK = 60
seconds = pygame.time.get_ticks()//1000



