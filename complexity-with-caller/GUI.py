import pygame

from Text import Text

def get_lines(raw_text, cursor_position, line_length=25):
    lines = [''] 
    for char_number, char in enumerate(text.get_text()):
        if char_number == cursor_position:
            lines[-1] += ']' + char
        else:
            lines[-1] += char
        if len(lines[-1]) > line_length:
            lines.append('')
    return lines

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

    # unavoidable complexity, organising raw text into lines to be displayed 
    # by the editor. Question, whether it is better for it to be here, with the caller, 
    # or whether it should be pulled down into the Text class?

    # show equation of complexity, how often is it going to be used, modified.

    # perhaps ignore gen purp for this video? (although get_lines is still nicely gen purp)

    lines = get_lines(
        raw_text = text.get_text(),
        cursor_position = cursor_position,
    )

    for line_number, line in enumerate(lines):
        textsurface = myfont.render(line, False, (0, 0, 0))
        screen.blit(textsurface,(0,line_number*20))

    pygame.display.flip()

pygame.quit()