# DEC 3, 2021 - dyarovyi
# This is my first command line text editor/viewer app

# README

# Option 1 creates a new file. You can write text that will be saved there.
# Option 2 reads an existing file. It prints the content of this file.
# Option 3 reads an existing file. You can write text to append the file.
# Option 0 exits the app.

class Program:
    INVALID_OPERATION = "ERROR: invalid operation"
    FILE_NOT_FOUND = "ERROR: file was not found"

    def menu(self):
        while True:
            print("...MENU...")
            print("1 - New file")
            print("2 - Open file")
            print("3 - Append file")
            print("0 - Quit")

            try:
                option = int(input("Enter your option: "))

                if option not in (0, 1, 2, 3):
                    raise self.INVALID_OPERATION
            finally:
                if option == 1:
                    self.new_file()
                elif option == 2:
                    self.open_file(self)
                elif option == 3:
                    self.append_file(self)
                else:
                    return

    def new_file():
        filename = input("Enter filename: ")
        with open(filename, 'w') as file:
            content = input("Write:\n")
            file.write(content)
            file.close()

    def open_file(self):
        filename = input("Enter filename: ")
        try:
            with open(filename, 'r') as file:
                print(file.read())
                file.close()
        except FileNotFoundError:
            print(self.FILE_NOT_FOUND)

    def append_file(self):
        filename = input("Enter filename: ")
        try:
            with open(filename, 'r') as file:
                print(file.read())
                file.close()

            with open(filename, 'a') as file:
                content = '\n' + input("Write:\n")
                file.write(content)
                file.close()
        except FileNotFoundError:
            print(self.FILE_NOT_FOUND)

P = Program
P.menu(P)