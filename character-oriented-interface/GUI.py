import pygame

from Text import Text

pygame.init()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode([500, 500])

text = Text()
cursor_position = 0

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                text.insert('q', cursor_position)
                cursor_position += 1
            if event.key == pygame.K_w:
                text.insert('w', cursor_position)
                cursor_position += 1
            if event.key == pygame.K_DELETE:
                text.delete(start=-1)
                cursor_position = min(len(text), cursor_position + 1)
            if event.key == pygame.K_BACKSPACE:
                text.delete(start=-1)
                cursor_position = max(0, cursor_position - 1)
            if event.key == pygame.K_LEFT and cursor_position > 0:
                cursor_position -= 1
            if event.key == pygame.K_RIGHT and cursor_position <= len(text):
                cursor_position += 1

    screen.fill((255, 255, 255))

    print(cursor_position)

    lines = [''] 
    for char_number, char in enumerate(text.get_text()):
        if char_number == cursor_position:
            lines[-1] += ']' + char
        else:
            lines[-1] += char
        if len(lines[-1]) > 30:
            lines.append('')

    for line_number, line in enumerate(lines):
        textsurface = myfont.render(line, False, (0, 0, 0))
        screen.blit(textsurface,(0,line_number*20))

    pygame.display.flip()

pygame.quit()
