import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 200, 0)

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Player1': 300,
    'Player2': 300,
    'Player1Shot': 1,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy2': 60,
    'Enemy3': 50,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
    'Enemy3Shot': 1
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200,
    'Enemy3': 100

}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 1,
    'Level1Bg4': 1,
    'Player1': 3,
    'Player2': 3,
    'Player1Shot': 4,
    'Player2Shot': 5,
    'Enemy1': 2,
    'Enemy2': 1,
    'Enemy3': 2,
    'Enemy1Shot': 5,
    'Enemy2Shot': 2,
    'Enemy3Shot': 4
}

EVENT_ENEMY = pygame.USEREVENT + 1

MENU_OPTION = ('NEW GAME',
               'NEW GAME - COOPERATIVE',
               'NEW GAME - COMPETITIVE',
               'SCORE',
               'EXIT')

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                 'Player2': pygame.K_LCTRL}

SPAWN_TIME = 4000

WIN_WIDTH = 576
WIN_HEIGHT = 324