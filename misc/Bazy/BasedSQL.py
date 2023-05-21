import _io

class Table:
    def __init__(self, name):
        self.name = name
        self.titles = []
        self.values = []

    def insert_data(self, file: _io.TextIOWrapper, spacer: str, first_is_title=True):
        with open(file) as data:
            if first_is_title:
                self.titles.append(data.readline().rstrip().split(spacer))
            for i in data:
                self.values.append(i.rstrip().split(spacer))

uzytkownicy=Table('uzytkownicy')
uzytkownicy.insert_data('uzytkownicy.txt', spacer='\t')
