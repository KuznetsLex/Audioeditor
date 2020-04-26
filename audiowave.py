from scipy.io.wavfile import read
import matplotlib.pyplot as plt

from pydub import AudioSegment
from pydub.playback import play
import sys
from audio import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)



# read audio samples
input_data = read("myfile.wav")
audio = input_data[1]
# plot the first 1024 samples
plt.plot(audio[0:102400])
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
        # set the title
plt.title("Sample Wav")
        # display the plot
plt.show()



