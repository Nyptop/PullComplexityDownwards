from pathlib import Path
class Text:
    def __init__(self):
        myfile = Path('myfile.txt')
        myfile.touch(exist_ok=True)
        with open("myfile.txt", "r") as text_file:
            self._lines = text_file.readlines()
        if not self._lines:
            self._lines = ['']


    def __len__(self):
        return len(self._lines)

    def append_line(self, line):
        # we don't handle complexity of inserting/ deleting across lines at this level
        # also worth mentioning that this method is shallow
        # not a lot of implementation behind this simple interface
        # perhaps simpler to simply have the variable in the UI 
        self._lines.insert(-1, line)

    def replace_line(self, line_index, new_line):
        self._lines[line_index] = new_line


    def delete_line(self, line_index):
        self._lines.remove(line_index)

    def get_line(self, line_index):
        return self._lines[line_index]

    def get_lines(self):
        return self._lines

    def add_cursor(self, current_line_index, cursor_index_in_line):
        self._lines = self._lines[current_line_index][:cursor_index_in_line] + ']' + self._lines[current_line_index][cursor_index_in_line:]
    
    def save(self):
        text_file = open("myfile.txt", "w")
        text_file.writelines(self._lines)
        text_file.close()

        
