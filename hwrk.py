class Subject:

    def __init__(self, name):
        self.name = name

    @property
    def filename(self):
        fname = self.name + '.txt'
        return fname

    def add(self):
        print('Enter your homework.')
        next = input("> ")

        with open(self.filename, 'a+') as f:
            f.write(f'\n* {next}')
            f.close()

    def show(self):

        try:
            with open(self.filename, 'r') as f:
                print(f.read())
                input()
                f.close()

        except:
            print("You haven't added any homework on that subject.")


def main():

    print("Enter (1) to add homework, (2) to view current homework.")
    choice = input("> ")

    if choice == "1":
        print("Enter subject's name.")
        name = input("> ")

        s1 = Subject(name)
        s1.add()


    elif choice == "2":
        print("Enter subject's name.")
        name = input("> ")

        s1 = Subject(name)
        s1.show()

    else:
        print("Couldn't understand that.")

main()
