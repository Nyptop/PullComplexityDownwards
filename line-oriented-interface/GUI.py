
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

cursor_position = len(text)
line_length = 25 # this can be made redundant with better design

# this is the file we're likely to work in more often, since we'll be making
# frequent changes, so want to minimise complexity here 
# 
# DONT BE PERFECTIONIST, THIS IS JUST FOR DEMONSTRATION PURPOSE 

# for purpose of video though, probably best to have lines added correctly, making UI fully complex
# means that the contrast in designs will be great

# REDESIGN ALL, with multiline, we only modify all lines after the cursor
# with delete, they all shift left (means we have to treat line like a queue, take off one, put onto other)

running = True
while running:

    cursor_line_index, cursor_index_in_line = divmod(cursor_position, line_length)
    print(cursor_line_index, cursor_index_in_line)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            save_button.handle_click(save, text)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if len(text.get_lines()[-1]) > 24:
                    current_line = 'q'
                    text.append_line(current_line)
                else:
                    current_line = text.get_line(cursor_line_index)
                    current_line += 'q'
                    text.replace_line(cursor_line_index, current_line)
                cursor_position += 1
            if event.key == pygame.K_w:
                if event.key == pygame.K_q:
                if len(text.get_lines()[-1]) > 24:
                    current_line = 'w'
                    text.append_line(current_line)
                else:
                    current_line = text.get_line(cursor_line_index)
                    current_line += 'w'
                    text.replace_line(cursor_line_index, current_line)
                cursor_position += 1
            if event.key == pygame.K_DELETE:
                # delete to the left of cursor
                if cursor_index_in_line == 1:
                    text.delete_line(cursor_line_index)
                else:
                    current_line = text.get_line(cursor_line_index)
                    current_line = current
                cursor_position = min(len(text), cursor_position + 1)
            if event.key == pygame.K_BACKSPACE:
                # add code here
                text.delete(start=-1)
                cursor_position = max(0, cursor_position - 1)
            if event.key == pygame.K_LEFT and cursor_position > 0:
                cursor_position -= 1
            if event.key == pygame.K_RIGHT and cursor_position <= len(text):
                cursor_position += 1

        # need to also ensure that 

    screen.fill((255, 255, 255))

    lines = text.get_lines()

    for line_number, line in enumerate(lines):
        if line_number == cursor_line_index:
            line = line[:cursor_index_in_line] + ']' + line[cursor_index_in_line:]
        textsurface = myfont.render(line, False, (0, 0, 0))
        screen.blit(textsurface,(0,line_number*20))

    save_button.show()
    pygame.display.flip()

pygame.quit()
