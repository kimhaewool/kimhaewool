from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QToolButton, QLabel
from PyQt5.QtGui import QPixmap, QIcon

from mukchiba import Mukchiba


class MukchibaGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # init score
        self.scoreComputer = 0
        self.scoreUser = 0

        # Layout
        topLayout = QGridLayout()
        statusLayout = QGridLayout()
        selectLayout = QGridLayout()

        # Button - new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)
        topLayout.addWidget(self.newGameButton, 0, 0)
        self.newGameButton.setEnabled(False)

        # Label - title
        title = QLabel('Muk-chi-ba')
        title.setStyleSheet('font-size: 55px;'
                            'font-family: bauhaus 93')
        topLayout.addWidget(title, 0, 1)

        # Label - scoreboard
        scoreboard = QGridLayout()
        self.scoreboardComputer = QLabel('0')
        self.scoreboardComputer.setStyleSheet('color: red')
        scoreboard.addWidget(self.scoreboardComputer, 0, 0)
        Colon = QLabel(':')
        scoreboard.addWidget(Colon, 0, 1)
        self.scoreboardUser = QLabel('0')
        self.scoreboardUser.setStyleSheet('color: blue')
        scoreboard.addWidget(self.scoreboardUser, 0, 2)
        topLayout.addLayout(scoreboard, 0, 2)

        # Label - selected image label
        computerLabel = QLabel('Computer')
        computerLabel.setAlignment(Qt.AlignCenter)
        computerLabel.setStyleSheet('color: red')
        statusLayout.addWidget(computerLabel, 0, 0)
        userLabel = QLabel('User')
        userLabel.setAlignment(Qt.AlignCenter)
        userLabel.setStyleSheet('color: blue')
        statusLayout.addWidget(userLabel, 0, 2)

        # Pixmap
        self.rockPixMap = QPixmap('rock.png')
        self.paperPixMap = QPixmap('paper.png')
        self.scissorsPixMap = QPixmap('scissors.png')
        self.pixMap = {'rock': self.rockPixMap, 'paper': self.paperPixMap, 'scissors': self.scissorsPixMap}

        # Label - selected image
        self.computerImg = QLabel()
        self.computerImg.setPixmap(self.paperPixMap)
        statusLayout.addWidget(self.computerImg, 1, 0)
        self.userImg = QLabel()
        self.userImg.setPixmap(self.paperPixMap)
        statusLayout.addWidget(self.userImg, 1, 2)

        # Label - status
        self.status = QLabel()
        self.status.setFixedWidth(100)
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setStyleSheet('font-size: 26px;''color: green')
        statusLayout.addWidget(self.status, 1, 1)

        # Button - image selection
        self.rockButton = QToolButton()
        self.rockButton.setIconSize(QSize(90, 70))
        self.rockButton.setText('rock')
        self.rockButton.setIcon(QIcon('rock.png'))
        self.rockButton.clicked.connect(self.buttonClicked)
        selectLayout.addWidget(self.rockButton, 0, 0)
        self.paperButton = QToolButton()
        self.paperButton.setIconSize(QSize(90, 70))
        self.paperButton.setText('paper')
        self.paperButton.setIcon(QIcon('paper.png'))
        self.paperButton.clicked.connect(self.buttonClicked)
        selectLayout.addWidget(self.paperButton, 0, 1)
        self.scissorsButton = QToolButton()
        self.scissorsButton.setIconSize(QSize(90, 70))
        self.scissorsButton.setText('scissors')
        self.scissorsButton.setIcon(QIcon('scissors.png'))
        self.scissorsButton.clicked.connect(self.buttonClicked)
        selectLayout.addWidget(self.scissorsButton, 0, 2)

        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(topLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 1, 0)
        mainLayout.addLayout(selectLayout, 2, 0)
        self.setLayout(mainLayout)

        self.setWindowTitle('Muk-chi-ba')

        self.startGame()


    def startGame(self):
        self.mukchiba = Mukchiba()
        self.rspFinished = False
        self.newGameButton.setEnabled(False)
        self.rockButton.setEnabled(True)
        self.paperButton.setEnabled(True)
        self.scissorsButton.setEnabled(True)
        self.status.clear()


    def buttonClicked(self):
        button = self.sender()
        user = button.text()

        self.computerImg.setPixmap(self.pixMap[self.mukchiba.getComputer()])
        self.userImg.setPixmap(self.pixMap[user])
        self.mukchiba.setUser(user)

        if not self.rspFinished:
            result = self.mukchiba.rockScissorsPaper()
            self.status.setText(result)
            if self.mukchiba.rspFinished():
                self.mukchiba.resultToStatus(result)
                self.status.setText(self.mukchiba.getStatus())
                self.rspFinished = True
            return

        status = self.mukchiba.mukchiba()
        self.status.setText(status)
        if self.mukchiba.finished():
            if status == 'win':
                self.scoreUser += 1
                self.scoreboardUser.setText(str(self.scoreUser))
            else:
                self.scoreComputer += 1
                self.scoreboardComputer.setText(str(self.scoreComputer))
            self.newGameButton.setEnabled(True)
            self.rockButton.setEnabled(False)
            self.paperButton.setEnabled(False)
            self.scissorsButton.setEnabled(False)


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = MukchibaGame()
    game.show()
    sys.exit(app.exec_())