class Girl:
    gender = 'female'
    def __init__(self, name):
        self.name = name


mini = Girl('mini')
mini2 = Girl('budhhu mini')
print(mini.gender)
print(mini2.gender)
print(mini.name)
print(mini2.name)
