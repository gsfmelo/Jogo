import pygame

ORANGE = (255, 128, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 200, 0)
GREEN = (0, 128, 0)
CYAN = (0, 128, 128)
BLUE = (37, 222, 214)

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Player1': 1,
    'Player2': 1,
    'Player1Shot': 25,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
    'Enemy1Shot': 20,
    'Enemy2Shot': 15,
    'Enemy3Shot': 15
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Player1': 0,
    'Player2': 0,
    'Player1Shot': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy2': 125,
    'Enemy3': 130,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0,
    'Enemy3Shot': 0
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Player1': 200,
    'Player2': 200,
    'Player1Shot': 1,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy2': 60,
    'Enemy3': 60,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
    'Enemy3Shot': 1
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 100,
    'Enemy2': 100,
    'Enemy3': 140

}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 1,
    'Level1Bg4': 3,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 1,
    'Level2Bg3': 2,
    'Player1': 3,
    'Player2': 3,
    'Player1Shot': 5,
    'Player2Shot': 5,
    'Enemy1': 2,
    'Enemy1Shot': 4,
    'Enemy2': 2,
    'Enemy2Shot': 4,
    'Enemy3': 2,
    'Enemy3Shot': 4
}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

MENU_OPTION = ('NEW GAME',
               'NEW GAME - COOPERATIVE',
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

SPAWN_TIME = 3500

WIN_WIDTH = 600
WIN_HEIGHT = 338

SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 40),
    'TypeName': (WIN_WIDTH / 2, 80),
    'Label': (WIN_WIDTH / 2, 90),
    'Name': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110),
    1: (WIN_WIDTH / 2, 130),
    2: (WIN_WIDTH / 2, 150),
    3: (WIN_WIDTH / 2, 170),
    4: (WIN_WIDTH / 2, 190)
}
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000