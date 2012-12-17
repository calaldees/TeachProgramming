import pygame
import socket, threading, json  # VER: network

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
    last_draw_pos     = None,                   # VER: draw_line
    my_pen_color      = (255, 255, 255),        # VER: draw_pixel
)
                                                            # VER: network
def connection(sock):                                       # VER: network
    while True:                                             # VER: network
        data_recv = sock.recv(4098)                         # VER: network
        if not data_recv:                                   # VER: network
            break                                           # VER: network
        data = json.loads(data_recv)                        # VER: network
        #print(data_recv)                                   # VER: network NOT draw_line_network, draw_pixel_network
        if data.get('comment')=='pixel':                            # VER: draw_pixel_network
            screen.set_at(tuple(data['pos'], tuple(data['color']))) # VER: draw_pixel_network
        if data.get('command')=='line':                                                                         # VER: draw_line_network
            pygame.draw.line(screen, tuple(data['color']), tuple(data['last_pos']), tuple(data['current_pos'])) # VER: draw_line_network
    sock.close()                                            # VER: network
                                                            # VER: network
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # VER: network
sock.connect(("localhost", 9872))                           # VER: network
thread = threading.Thread(target=connection, args=(sock,))  # VER: network
thread.daemon=True                                          # VER: network
thread.start()                                              # VER: network
                                                            # VER: network
def send(message):                                          # VER: network
    sock.sendall(json.dumps(message)+'\n'.encode('utf-8'))  # VER: network

screen.fill(v.color_background)
while v.running:
    clock.tick(60)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: v.running = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            v.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # VER: draw_line
            v.last_draw_pos = event.pos            # VER: draw_line
        elif event.type == pygame.MOUSEBUTTONUP:   # VER: draw_line
            v.last_draw_pos = None                 # VER: draw_line
    #                                                          # VER: draw_pixel NOT draw_line, draw_pixel_network
    #if pygame.mouse.get_pressed():                            # VER: draw_pixel NOT draw_line, draw_pixel_network
    #    screen.set_at(pygame.mouse.get_pos(), v.my_pen_color) # VER: draw_pixel NOT draw_line, draw_pixel_network
                                                                                 # VER: draw_line
    if v.last_draw_pos:                                                          # VER: draw_line
        #pygame.draw.line(screen, (0,255,255), v.last_draw_pos, mouse.get_pos()) # VER: draw_line NOT draw_line_network
        send(dict(                                  # VER: draw_line_network
            command     = 'line'                ,   # VER: draw_line_network
            color       = v.my_pen_color        ,   # VER: draw_line_network
            last_pos    = v.last_draw_pos       ,   # VER: draw_line_network
            current_pos = pygame.mouse.get_pos(),   # VER: draw_line_network
        ))                                          # VER: draw_line_network
        v.last_draw_pos = pygame.mouse.get_pos()  # VER: draw_line
    
    pygame.display.flip()

pygame.quit()