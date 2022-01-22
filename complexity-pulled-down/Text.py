class Text:
    def __init__(self):
        self._text = ''

    def __len__(self):
        return len(self._text)

    def insert(self, char, position):
        self._text = self._text[:position] + char + self._text[position:]

    def delete(self, start, end=None):
        if end:
            self._text = self._text[:start] + self._text[end:]
        else: # deleting from a position until the end
            self._text = self._text[:start]

    def get_text(self):
        return self._text

    def get_lines(self, cursor_position=-1, line_length=25):
        lines = [''] 
        for char_number, char in enumerate(self._text):
            if char_number == cursor_position:
                lines[-1] += ']' + char
            else:
                lines[-1] += char
            if len(lines[-1]) > line_length:
                lines.append('')
        return lines