from pydub import AudioSegment
from pydub.playback import play
import sys
from audio import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)





class MyWin(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.pushButton.clicked.connect(self.slice)
        self.ui.pushButton_2.clicked.connect(self.fade)
        self.ui.pushButton_3.clicked.connect(self.play)
        self.ui.pushButton_4.clicked.connect(self.repeat)
        self.ui.pushButton_5.clicked.connect(self.converter)



    def slice(self):
        text, ok = QInputDialog.getInt(self, 'Input Dialog',
            'Введите продолжительность трека (отрицательное число, если необходимо считать с конца):')
        if ok:

            sound = AudioSegment.from_wav('myfile.wav')
            if text>=0:
                duration = sound[:text*1000]
            if text<=0:
                duration = sound[text*1000:]
            return(duration.export('myfile.wav', format='wav'))


    def volume(self):
        text, ok = QInputDialog.getInt(self, 'Input Dialog',
            'Как вы хотите изменить звук?:')
        if ok:
            sound = AudioSegment.from_wav('myfile.wav')
            vol = sound + text
            return (vol.export('myfile.wav', format='wav'))


    def repeat(self):
        text, ok = QInputDialog.getInt(self, 'Input Dialog',
            'Введите число повторений:')
        if ok:
            if text<11:
                sound = AudioSegment.from_wav('myfile.wav')
                do_it_over = sound * text
                return(do_it_over.export('myfile.wav', format='wav'))


    def fade(self):
        text1, ok = QInputDialog.getInt(self, 'Input Dialog',
            'Введите время постепенного появления:')
        text2, ok = QInputDialog.getInt(self, 'Input Dialog',
            'Введите время затухания:')
        if ok:
            sound = AudioSegment.from_wav('myfile.wav')
            fin = sound.fade_in(text1*1000).fade_out(text2*1000)
            return(fin.export('myfile.wav', format='wav'))

    def play(self):
            sound = AudioSegment.from_wav('myfile.wav')
            play(sound)


    def converter(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
            'Введите формат (без точки):')
        if ok:
            sound = AudioSegment.from_wav('myfile.wav')
            return(sound.export('myfile.'+text, format=tex))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())


