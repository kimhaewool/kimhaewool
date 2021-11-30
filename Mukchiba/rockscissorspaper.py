import random


class RockScissorsPaper:

    def __init__(self):
        self.shapes = ['rock', 'scissors', 'paper']
        self.computer = self.randFromShapes()
        self.user = self.randFromShapes()
        self.result = ''


    def rockScissorsPaper(self):
        c = self.shapes.index(self.computer)
        u = self.shapes.index(self.user)

        self.computer = self.randFromShapes()
        self.user = self.randFromShapes()

        if c == u:
            self.result = 'draw'
            return self.result

        if (c == 0 and u == 1) or (c == 1 and u == 2) or (c == 2 and u == 0):
            self.result = 'lose'
            return self.result

        self.result = 'win'
        return self.result


    def finished(self):
        return self.result == 'win' or self.result == 'lose'


    def getComputer(self):
        return self.computer


    def setComputer(self, computer):
        self.computer = computer


    def getUser(self):
        return self.user


    def setUser(self, user):
        self.user = user


    def randFromShapes(self):
        return self.shapes[random.randrange(3)]


    def textGame(self):
        while not self.finished():
            # print('computer:', self.getComputer()) # test
            self.setUser(input('user: '))
            print('computer:', self.getComputer())
            print(self.rockScissorsPaper())
            print()



if __name__ == '__main__':

    r1 = RockScissorsPaper()

    print('1. Test random')
    for i in range(10):
        print('computer:', r1.getComputer())
        print('user:', r1.getUser())
        print(r1.rockScissorsPaper())
        print()
        if r1.finished():
            break

    print('2. Test setting computer')
    for i in range(10):
        r1.setComputer('rock')
        print('computer:', r1.getComputer())
        print('user:', r1.getUser())
        print(r1.rockScissorsPaper())
        print()

    r2 = RockScissorsPaper()

    print('3. Test text-based game')
    r2.textGame() # Uncomment the test in the function