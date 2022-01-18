
import pygame

from Text import Text
from Button import Button
from GUI_utils import save

pygame.init()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode([500, 500])

save_button = Button(screen, 100, 100, 100, 100, 'save')
text = Text()

cursor_position = 0
line_length = 25 # this can be made redundant with better design

# this is the file we're likely to work in more often, since we'll be making
# frequent changes, so want to minimise complexity here  

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            text.save()
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            save_button.handle_click(save, text)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                current_line_index = cursor_position // line_length
                cursor_index_in_line = cursor_position % line_length
                if cursor_index_in_line == 0:
                    current_line = 'q'
                    text.append_line(current_line)
                else:
                    current_line = text.get_line(current_line_index)
                    current_line += 'q'
                    text.replace_line(current_line_index, current_line)
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

    current_line_index = cursor_position // line_length
    cursor_index_in_line = cursor_position % line_length

    text.add_cursor(current_line_index, cursor_index_in_line)

    lines = text.get_lines()

    for line_number, line in enumerate(lines):
        textsurface = myfont.render(line, False, (0, 0, 0))
        screen.blit(textsurface,(0,line_number*20))

    save_button.show()
    pygame.display.flip()

pygame.quit()
