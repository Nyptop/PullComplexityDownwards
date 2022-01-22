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