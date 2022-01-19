class Text:
    def __init__(self):
        self._lines = ['']

    def __len__(self):
        return len(self._text)

    def insert_chars(self, char, position):
        # here we handle complexity of multiple lines, rather than in GUI
        self._text = self._text[:position] + char + self._text[position:]

    def delete_chars(self, start, end=None):
        if end:
            self._text = self._text[:start] + self._text[end:]
        else: # deleting from a position until the end
            self._text = self._text[:start]

    def get_lines(self, cursor_position):
        return self._lines
