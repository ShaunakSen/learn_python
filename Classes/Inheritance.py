class Parent:

    def print_last_name(self):
        print('Sen')


class Child(Parent):

    def print_first_name(self):
        print('Shaunak')
    def print_last_name(self):
        print('blaaah blaaah')


shaunak = Child()

shaunak.print_first_name()
shaunak.print_last_name()
