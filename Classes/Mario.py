class Mario():
    def move(self):
        print('Mario Moving....')


class Shroom():
    def eat_shroom(self):
        print('Mario is BIG !!')


class BigMario(Mario, Shroom):
    pass

mini = BigMario()
mini.move()
mini.eat_shroom()
