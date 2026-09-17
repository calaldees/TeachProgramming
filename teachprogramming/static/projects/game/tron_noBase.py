import pygame

pygame.init()
screen = pygame.display.set_mode((480,270), pygame.SCALED | pygame.RESIZABLE)
clock = pygame.time.Clock()

DIRECTION_RIGHT = 0     # VER: keys_direction
DIRECTION_LEFT = 1      # VER: keys_direction
DIRECTION_UP = 2        # VER: keys_direction
DIRECTION_DOWN = 3      # VER: keys_direction
                        # VER: keys_direction
class Player():
    def __init__(self, x:int, y:int, direction:int, color:pygame.Color, keys:tuple[pygame.key, ...]):
        self.start_x = x
        self.start_y = y
        self.start_direction = direction
        self.color = color
        self.keys = keys
        self.crash_count = 0
        self.reset()
    def reset(self) -> None:
        self.x = self.start_x
        self.y = self.start_y
        self.direction = self.start_direction
        self.crashed = False
    def move(self) -> None:
        if self.crashed:
            return
        if self.direction == DIRECTION_RIGHT:
            self.x += 1
        if self.direction == DIRECTION_LEFT:
            self.x -= 1
        if self.direction == DIRECTION_UP:
            self.y -= 1
        if self.direction == DIRECTION_DOWN:
            self.y += 1
    def set_direction_from_keys(self, keys:dict[pygame.keys, bool]) -> None:
        if keys[self.keys[DIRECTION_RIGHT]] and self.direction != DIRECTION_LEFT:
            self.direction = DIRECTION_RIGHT
        if keys[self.keys[DIRECTION_LEFT]] and self.direction != DIRECTION_RIGHT:
            self.direction = DIRECTION_LEFT
        if keys[self.keys[DIRECTION_UP]] and self.direction != DIRECTION_DOWN:
            self.direction = DIRECTION_UP
        if keys[self.keys[DIRECTION_DOWN]] and self.direction != DIRECTION_UP:
            self.direction = DIRECTION_DOWN
    def set_crashed(self):
        self.crashed = True
        self.crash_count += 1

# x = 50
# y = 50
# direction = DIRECTION_RIGHT

START_OFFSET = 50
players = [
    Player(
        START_OFFSET, START_OFFSET, DIRECTION_RIGHT, pygame.Color('yellow'),
        (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN),
    ),
    Player(
        screen.width-START_OFFSET, screen.height-START_OFFSET, DIRECTION_LEFT, pygame.Color('red'),
        (pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s),
    ),
    Player(
        START_OFFSET, screen.height-START_OFFSET, DIRECTION_UP, pygame.Color('green'),
        (pygame.K_k, pygame.K_h, pygame.K_u, pygame.K_j),
    ),
    Player(
        screen.width-START_OFFSET, START_OFFSET, DIRECTION_DOWN, pygame.Color('blue'),
        (pygame.K_KP3, pygame.K_KP1, pygame.K_KP5, pygame.K_KP2),
    ),
]
players = players[:int(input('How many players?: '))]


while True:
    pygame.display.update()
    clock.tick(60)
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break

    # if keys[pygame.K_RIGHT]:   # VER: keys_move NOT keys_direction
    #     x = x + 1              # VER: keys_move NOT keys_direction
    # if keys[pygame.K_LEFT]:    # VER: keys_move NOT keys_direction
    #     x = x - 1              # VER: keys_move NOT keys_direction
    # if keys[pygame.K_UP]:      # VER: keys_move NOT keys_direction
    #     y = y - 1              # VER: keys_move NOT keys_direction
    # if keys[pygame.K_DOWN]:    # VER: keys_move NOT keys_direction
    #     y = y + 1              # VER: keys_move NOT keys_direction
                                 # VER: keys_move NOT keys_direction
    # if keys[pygame.K_RIGHT]:          # VER: keys_direction NOT keys_direction_protect
    #     direction = DIRECTION_RIGHT   # VER: keys_direction NOT keys_direction_protect
    # if keys[pygame.K_LEFT]:           # VER: keys_direction NOT keys_direction_protect
    #     direction = DIRECTION_LEFT    # VER: keys_direction NOT keys_direction_protect
    # if keys[pygame.K_UP]:             # VER: keys_direction NOT keys_direction_protect
    #     direction = DIRECTION_UP      # VER: keys_direction NOT keys_direction_protect
    # if keys[pygame.K_DOWN]:           # VER: keys_direction NOT keys_direction_protect
    #     direction = DIRECTION_DOWN    # VER: keys_direction NOT keys_direction_protect
                                        # VER: keys_direction NOT keys_direction_protect
    # if keys[pygame.K_RIGHT] and direction != DIRECTION_LEFT:  # VER: keys_direction_protect
    #     direction = DIRECTION_RIGHT                           # VER: keys_direction_protect
    # if keys[pygame.K_LEFT] and direction != DIRECTION_RIGHT:  # VER: keys_direction_protect
    #     direction = DIRECTION_LEFT                            # VER: keys_direction_protect
    # if keys[pygame.K_UP] and direction != DIRECTION_DOWN:     # VER: keys_direction_protect
    #     direction = DIRECTION_UP                              # VER: keys_direction_protect
    # if keys[pygame.K_DOWN] and direction != DIRECTION_UP:     # VER: keys_direction_protect
    #     direction = DIRECTION_DOWN                            # VER: keys_direction_protect
                                                                # VER: keys_direction_protect
    # if direction == DIRECTION_RIGHT:  # VER: keys_direction
    #     x = x + 1                     # VER: keys_direction
    # if direction == DIRECTION_LEFT:   # VER: keys_direction
    #     x = x - 1                     # VER: keys_direction
    # if direction == DIRECTION_UP:     # VER: keys_direction
    #     y = y - 1                     # VER: keys_direction
    # if direction == DIRECTION_DOWN:   # VER: keys_direction
    #     y = y + 1                     # VER: keys_direction
                                        # VER: keys_direction
    # pixel = screen.get_at((x, y))         # VER: collision
    # try:                                  # VER: collision
    #     pixel = screen.get_at((x, y))     # VER: collision
    # except:                               # VER: collision
    #     pixel = None                      # VER: collision
                                            # VER: collision
    # if pixel != pygame.Color('black'):    # VER: collision
    #     screen.fill('black')              # VER: collision
    #     x = 50                            # VER: collision
    #     y = 50                            # VER: collision
    #     direction = 2                     # VER: collision
                                            # VER: collision
    for player in players:
        player.set_direction_from_keys(keys)
        player.move()
        try:
            pixel = screen.get_at((player.x, player.y))
        except Exception:
            pixel = None
        if pixel != pygame.Color('black'):
            player.set_crashed()

    for player in players:
        pygame.draw.rect(screen, player.color, (player.x, player.y, 1, 1))

    if len([player for player in players if not player.crashed]) <= 1:
        screen.fill('black')
        for player in players:
            player.reset()

                                                                                # VER: exit_scores
for player in players:                                                          # VER: exit_scores
    print(f'player {player.color} crashed {player.crash_count} times')          # VER: exit_scores
print("Thank you for playing Tron")                                             # VER: exit_scores
