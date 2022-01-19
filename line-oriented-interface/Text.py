from pathlib import Path
from copy import copy

# whole point is that it is easy to read in with lines

# this video may be silly because best to just have char attribute, rather than lines
# this way you wouldn't need to handle lines in the UI or the text class
# or actually if you have characters attribute, ask viewers to look past this
# or make a note at the end. Doesn't need to be perfect, doesn't need to stop me making video.

class Text:
    def __init__(self):
        myfile = Path('myfile.txt')
        myfile.touch(exist_ok=True)
        self._lines = ['']
        with open('myfile.txt', 'r') as text_file:
            for line in text_file:
                line = line.strip('\n')
                self._lines.append(line)

    def __len__(self):
        text_length = 0
        for line in self._lines:
            text_length += len(line)
        return text_length

    def append_line(self, line):
        # we don't handle complexity of inserting/ deleting across lines at this level
        # also worth mentioning that this method is shallow
        # not a lot of implementation behind this simple interface
        # perhaps simpler to simply have the variable in the UI 
        self._lines.append(line)

    def replace_line(self, line_index, new_line):
        self._lines[line_index] = new_line

    def delete_line(self, line_index):
        self._lines.remove(line_index)

    def get_line(self, line_index):
        return self._lines[line_index]

    def get_lines(self):
        return copy(self._lines)
    
    def save(self):
        with open("myfile.txt", "w") as text_file:
            text_file.write('\n'.join(self._lines) + '\n')
            print('lines written')

# is it still general purpose if we pull complexity (line stuff) down?
# yes because all text is organised into lines. still gen purp. 


        
