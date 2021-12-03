import random
from rockscissorspaper import RockScissorsPaper


class Mukchiba(RockScissorsPaper):

    def __init__(self):
        super().__init__()
        self.statusList = ['attack', 'defense']
        self.status = self.randFromStatusList()


    def mukchiba(self):
        c = self.shapes.index(self.computer)
        u = self.shapes.index(self.user)
        s = self.statusList.index(self.status)

        self.computer = self.randFromShapes()
        self.user = self.randFromShapes()
        self.status = self.randFromStatusList()

        if s == 0 and c == u:
            self.status = 'win'
            return self.status

        if s == 1 and c == u:
            self.status = 'lose'
            return self.status

        self.setComputer(self.shapes[c])
        self.setUser(self.shapes[u])
        if self.rockScissorsPaper() == 'win':
            self.status = 'attack'
            return self.status

        self.status = 'defense'
        return self.status


    def finished(self):
        return self.status == 'win' or self.status == 'lose'


    def rspFinished(self):
        return super().finished()


    def getStatus(self):
        return self.status


    def setStatus(self, status):
        self.status = status


    def resultToStatus(self, result):
        self.status = 'attack' if result == 'win' else 'defense'


    def randFromStatusList(self):
        return self.statusList[random.randrange(2)]


    def textGame(self):
        while not self.finished():
            while not self.rspFinished():
                # print('computer:', self.getComputer()) # test
                self.setUser(input('user: '))
                print('computer:', self.getComputer())
                result = self.rockScissorsPaper()
                self.resultToStatus(result)
                print(result)
                print()
            print('status:', self.getStatus())
            print('computer:', self.getComputer()) # test
            self.setUser(input('user: '))
            print('computer:', self.getComputer())
            print(self.mukchiba())
            print()



if __name__ == '__main__':

    m1 = Mukchiba()

    print('1. Test random')
    for i in range(10):
        print('status:', m1.getStatus())
        print('computer:', m1.getComputer())
        print('user:', m1.getUser())
        print(m1.mukchiba())
        print()
        if m1.finished():
            break

    print('2. Test setting status')
    for i in range(10):
        m1.setStatus('defense')
        print('status:', m1.getStatus())
        print('computer:', m1.getComputer())
        print('user:', m1.getUser())
        print(m1.mukchiba())
        print()
        if m1.finished():
            break

    m2 = Mukchiba()

    print('3. Test text-based game')
    m2.textGame() # Uncomment the test in the function
