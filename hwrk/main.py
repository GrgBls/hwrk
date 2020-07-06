from sys import argv
import os

prompt = """
Usage: hwrk [option] [subject]
[option]: add, view, remove

example: hwrk view math
or: hwrk add math "exercises 4,6,7 on page 103"
or: hwrk remove math
"""

class Subject:
    def __init__(self, name):
        self.name = name

    @property
    def filename(self):
        fname = self.name + '.txt'
        return fname

    def add(self, homework):
        with open(self.filename, 'a+') as f:
            f.write(f'\n* {homework}')
            print('Done.')

    def view(self):
        try:
            with open(self.filename, 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print("You haven't added any homework to that specific subject.")

    def remove(self):
        try:
            os.remove(self.filename)
            print('Done.')
        except FileNotFoundError:
            print('Subject hasn\'t been created.')

def main():    
    if len(argv) == 1:
        print(prompt)

    elif len(argv) > 1:
        if argv[1] == "view":
            try:
                s1 = Subject(argv[2])
                s1.view()
            except IndexError:
                print(prompt)

        elif argv[1] == "add":
            try:
                s1 = Subject(argv[2])
                s1.add(argv[3])

            except IndexError:
                print(prompt)

        elif argv[1] == "remove":
            try:
                s1 = Subject(argv[2])
                s1.remove()
            except IndexError:
                print(prompt)
           
        else:
            print(prompt)

