class Enemy:
    life = 3

    def __init__(self, x=3):
        self.life = x

    def attack(self):
        print('Ouch !')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")

enemy1 = Enemy()
enemy1.attack()
enemy1.checkLife()

enemy2 = Enemy(10)
enemy2.attack()
enemy2.checkLife()
