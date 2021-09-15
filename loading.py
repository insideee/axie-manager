import sys
from PySide2 import QtCore
from PySide2.QtWidgets import *

# import gui and functions
from src.ui_loading import Ui_MainWindow
from src.functions import UIFunctions
from main import MainWindow


class LoadingScreen(QMainWindow):

    def __init__(self):
        super(LoadingScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_functions = UIFunctions()

        self.timer = None
        self.counter = 3

        # window configs
        self.window_gui_configuration()

        # fonts configs
        self.fonts_gui_configuration()

        # temporary
        self.ui.info_label.setText('loading...')

        self.progress_configuration()

        self.show()

    def window_gui_configuration(self):
        # center and config window
        self.ui_functions.config_window(config_widget=self, title='', width=600, height=250, resizeble=False,
                                        minimum_size=True)
        # remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def fonts_gui_configuration(self):
        # title bar
        self.ui_functions.set_font(self.ui.title_1, 25, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False, True)
        self.ui_functions.set_font(self.ui.title_2, 26, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', True, True)

        # info progress
        self.ui_functions.set_font(self.ui.info_label, 12, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False, True)

        # progress bar
        self.ui_functions.set_font(self.ui.progress, 12, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False, False)

    def progress_configuration(self):
        self.timer = QtCore.QTimer()
        self.timer.start(5)

        self.timer.timeout.connect(self.progress_handle)

    def progress_handle(self):

        if self.counter < 100:
            self.timer.setInterval(50)
        elif self.counter == 100:
            self.ui.info_label.setText('initializing...')
            self.timer.setInterval(2000)

        self.ui.progress.setValue(self.counter)

        if self.counter == 101:
            self.timer.stop()
            new_window = MainWindow()
            self.close()

        self.counter += 1


def main():
    app = QApplication(sys.argv)
    window = LoadingScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
