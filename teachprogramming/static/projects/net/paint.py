import pygame
import socket, threading
import json

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock  = pygame.time.Clock()

class callByRef:
    def __init__(self, **args):
        for (key, value) in args.items():
            setattr(self, key, value)
v = callByRef(
    running           = True,
    color_background  = (  0,   0,   0, 255),
    last_draw_pos     = None,
    my_pen_color      = (255, 255, 255),
)

                                                      # VER: recv
def connection(sock):                                 # VER: recv
    while True:                                       # VER: recv
        data_recv = sock.recv(4098)                   # VER: recv
        if not data_recv:                             # VER: recv
            break                                     # VER: recv
        data = json.loads(data_recv)
        if data.get('command')=='line':
            pygame.draw.line(screen, tuple(data['color']), tuple(data['last_pos']), tuple(data['current_pos']))
    sock.close()                                      # VER: recv

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9872))
thread = threading.Thread(target=connection, args=(sock,)) # VER: send_recv
thread.daemon=True                                         # VER: send_recv
thread.start()                                             # VER: send_recv



while v.running:
    clock.tick(60)
    #screen.fill(v.color_background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            v.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            v.last_draw_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            v.last_draw_pos = None
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: v.running = False
    
    mouse = pygame.mouse
    if v.last_draw_pos:
        #pygame.draw.line(screen, (0,255,255), v.last_draw_pos, mouse.get_pos())
        sock.sendall(json.dumps(dict(
            command     = 'line',
            color       = v.my_pen_color,
            last_pos    = v.last_draw_pos,
            current_pos = mouse.get_pos()))+'\n'.encode('utf-8'))
        v.last_draw_pos = mouse.get_pos()
    
    pygame.display.flip()

pygame.quit()