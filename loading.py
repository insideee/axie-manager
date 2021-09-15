import sys
from PySide2 import QtCore
from PySide2.QtWidgets import *

# import gui and functions
from src.ui_loading import Ui_MainWindow
from src.functions import UIFunctions
from main import MainWindow
from updater import *


class LoadingScreen(QMainWindow):

    def __init__(self):
        super(LoadingScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_functions = UIFunctions()

        self.timer = None
        self.counter = 3
        self.update_handle = None

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
        self.timer.setInterval(80)

        self.timer.timeout.connect(self.progress_handle)

    def progress_handle(self):

        # default
        if self.counter == 5:
            self.ui.info_label.setText('Loading...')

        # check update
        if self.counter == 25:
            self.update_handle = Updater(
                url_version='https://raw.githubusercontent.com/axie-manager/axie-manager-updater/main/version.txt',
                url_update='https://github.com/axie-manager/axie-manager-updater/raw/main/src.zip')

            self.ui.info_label.setText('Checking updates...')
            self.timer.setInterval(300)

        # update or not
        if self.counter == 39:
            if self.update_handle.need_update:
                self.update_handle.update_src()
                self.ui.info_label.setText(f'Updating to version {self.update_handle.remote_version}')
            else:
                self.ui.info_label.setText(f'App up to date...')

        # end update
        if self.counter == 46 and self.update_handle.need_update:
            self.ui.info_label.setText(f'Finishing...')

        if self.counter == 55:
            self.ui.info_label.setText('Loading...')
            self.timer.setInterval(80)

        if self.counter == 100:
            self.ui.info_label.setText('Initializing...')
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
