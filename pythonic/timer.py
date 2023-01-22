import time
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QVBoxLayout
import sys

class Timer(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.finish()

    def finish(self):
        self.start = 0
        self.end = 0
        self.stop = 0

    def initUI(self):
        self.btn1 = QPushButton('Start', self)
        self.btn1.setCheckable(True)
        self.btn1.toggled.connect(self.startEvent)

        self.btn2 = QPushButton('Pause', self)
        self.btn2.setCheckable(True)
        self.btn2.toggled.connect(self.pauseEvent)

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)

        self.setLayout(vbox)
        self.setWindowTitle('Timer')
        self.resize(400, 200)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def startEvent(self, state):
        # pause는 start가 안눌린채로는 눌릴 수 없다.
        if not state and self.start == -1:
            print("pause 상태입니다.")
            self.btn1.toggle()

        if self.start != -1:
            if state:
                print("### start")
                self.start = time.time()
            else:
                print("### end")
                self.end = time.time()
                self.time_print()
                self.finish()

    def pauseEvent(self, state):
        if state and not self.start:
            print("start를 안한 상태입니다.")
            self.btn2.toggle()
        
        if self.start:
            if state:
                print("### pause")
                self.stop += time.time() - self.start
                self.start = -1
            else:
                print("### play")
                self.start = time.time() 

    def time_print(self):
        play_time = self.end - self.start
        if self.stop:
            play_time += self.stop

        if play_time > 60:
            minute = int(play_time//60)
            second = play_time%60
            print(f"@@@ running_time ==> {minute}분 {second:.0f}초")
        else:
            print(f"@@@ running_time ==> {play_time:.0f}초")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Timer()
    sys.exit(app.exec_())