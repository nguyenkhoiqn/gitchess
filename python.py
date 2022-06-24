import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
starter = False
while starter == False:
  pygame.display.set_caption('CHESS')
  background_game = pygame.image.load('background_game.jpg').convert_alpha()
  background_game = pygame.transform.scale(background_game, (500, 500))
  screen.blit(background_game, (0, 0))
  start = pygame.image.load('button.png')
  start = pygame.transform.scale(start, (100, 100))
  screen.blit(start, (200, 200))  
  mouse_x, mouse_y = pygame.mouse.get_pos()
  #print(pygame.mouse.get_rel())
  #print(pygame.MOUSEMOTION)
  #print(mouse_x, mouse_y)
  for eventf in pygame.event.get():
    if eventf.type == pygame.QUIT:
      starter = True
    if eventf.type == pygame.MOUSEBUTTONDOWN:
      print(eventf.pos)
      if eventf.button == 1:
        if mouse_x > 200 and mouse_x < 300:
          if mouse_y > 200 and mouse_y < 300:
            print('click')
            starter = True
  pygame.display.flip()
  pygame.display.update()
class status:
  def __init__(self, via, x, y, status):
    self.via = via
    self.x = x
    self.y = y
    self.status = status
    self.scope = self.x + 63, self.y + 63
    pygame.transform.scale(self.via, (63, 63))
    screen.blit(self.via, (self.x, self.y))
grid = []
for row in range(8):
    grid.append([])
    for column in range(8):
        grid[row].append(0)
print(grid)
running = True
while running:
  pygame.display.set_caption('CHESS')
  move = False
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEWHEEL:
      print(event)
      print(event.x, event.y)
      print(event.flipped)
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      column = pos[0] // (63 + 0)
      row = pos[1] // (63 + 0)
      print(column, row)
      move = True
  vt = pygame.image.load('vua trắng.png')
  vd = pygame.image.load('vua đen.png')
  ht = pygame.image.load('hậu trắng.png')
  hd = pygame.image.load('hậu đen.png')
  tt = pygame.image.load('tượng trắng.png')
  td = pygame.image.load('tượng đen .png')
  nt = pygame.image.load('ngựa tráng.png')
  nd = pygame.image.load('ngựa đen.png')
  xt = pygame.image.load('xe trắng.png')
  xd = pygame.image.load('xe đen.png')
  cd = pygame.image.load('chốt đen.png')
  cd1 = pygame.image.load('chốt đen.png')
  cd2 = pygame.image.load('chốt đen.png')
  cd3 = pygame.image.load('chốt đen.png')
  cd4 = pygame.image.load('chốt đen.png')
  cd5 = pygame.image.load('chốt đen.png')
  cd6 = pygame.image.load('chốt đen.png')
  cd7 = pygame.image.load('chốt đen.png')
  ct = pygame.image.load('chốt trắng.png')
  ct1 = pygame.image.load('chốt trắng.png')
  ct2 = pygame.image.load('chốt trắng.png')
  ct3 = pygame.image.load('chốt trắng.png')
  ct4 = pygame.image.load('chốt trắng.png')
  ct5 = pygame.image.load('chốt trắng.png')
  ct6 = pygame.image.load('chốt trắng.png')
  ct7 = pygame.image.load('chốt trắng.png')
  xd1 = pygame.image.load('xe đen 1.png')
  xt1 = pygame.image.load('xe trắng 1.png')
  td1 = pygame.image.load('tượng đen 1.png')
  tt1 = pygame.image.load('tượng trắng 1.png')
  nd1 = pygame.image.load('ngựa đen 1.png')
  nt1 = pygame.image.load('ngựa tráng 1.png')
  board = pygame.image.load('chess.png').convert_alpha()
  board = pygame.transform.scale(board, (500, 500))
  screen.blit(board, (0, 0))
  xd = status(xd, 0, 63*7, True)
  xt = status(xt, 0, 0, True)
  nd = status(nd, 63, 63*7, True)
  nt = status(nt, 63, 0, True)
  td = status(td, 63*2,63*7, True)
  tt = status(tt, 63*2,0, True)
  hd = status(hd, 63*3, 63*7, True)
  ht = status(ht, 63*4, 0, True)
  vd = status(vd, 63*4, 63*7, True)
  vt = status(vt, 63*3, 0, True)
  xd1 = status(xd1, 63*7, 63*7, True)
  xt1 = status(xt1, 63*7, 0, True)
  nd1 = status(nd1, 63*6, 63*7, True)
  nt1 = status(nt1, 63*6, 0, True)
  td1 = status(td1, 63*5,63*7, True)
  tt1 = status(tt1, 63*5,0, True)
  cd = status(cd, 0, 63*6, True)
  cd1 = status(cd1, 63, 63*6, True)
  cd2 = status(cd2, 63*2, 63*6, True)
  cd3 = status(cd3, 63*3, 63*6, True)
  cd4 = status(cd4, 63*4, 63*6, True)
  cd5 = status(cd5, 63*5, 63*6, True)
  cd6 = status(cd6, 63*6, 63*6, True)
  cd7 = status(cd7, 63*7, 63*6, True)
  ct = status(ct, 0, 63, True)
  ct1 = status(ct1, 63, 63, True)
  ct2 = status(ct2, 63*2, 63, True)
  ct3 = status(ct3, 63*3, 63, True)
  ct4 = status(ct4, 63*4, 63, True)
  ct5 = status(ct5, 63*5, 63, True)
  ct6 = status(ct6, 63*6, 63, True)
  ct7 = status(ct7, 63*7, 63, True)
  mouse_x2, mouse_y2 = pygame.mouse.get_pos()
  #print(xd.scope)
  #print(xd)
  #print(mouse_x2, mouse_y2)
  pygame.display.flip()
  pygame.display.update()
pygame.quit()
