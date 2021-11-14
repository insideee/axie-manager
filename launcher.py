import sys
from PySide6 import QtCore
from PySide6.QtWidgets import *
import importlib

# import gui and functions
from updater.ui.ui_loading import Ui_MainWindow
from updater.function import UIFunctions
from updater import *

class LoadingScreen(QMainWindow):

    def __init__(self) -> None:
        super(LoadingScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_functions = UIFunctions()

        self.timer = None
        self.counter = 3
        self.update_handle = None
        self.log_list = None
        self.log_step = None
        self.log_loop_init = 25
        self.old_log = 0
        self.need_show_log = False

        # window configs
        self.window_gui_configuration()

        # fonts configs
        self.fonts_gui_configuration()

        self.progress_configuration()

        self.show()

    def window_gui_configuration(self) -> None:
        # center and config window
        self.ui_functions.config_window(config_widget=self, title='', width=600, height=250, resizeble=False,
                                        minimum_size=True)
        # remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def fonts_gui_configuration(self) -> None:
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

    def progress_handle(self) -> None:

        # default
        if self.counter == 5:
            self.ui.info_label.setText('Loading...')

        # check update
        if self.counter == 25:
            self.ui.info_label.setText('Checking updates...')
            self.timer.setInterval(300)

            self.update_handle = Updater()
            self.log_list, self.log_step, self.old_log = self.get_log_and_step(self.update_handle,
                                                                               self.old_log)

        if self.counter > 25 and self.counter <= 50:

            for counter in range(self.log_loop_init, 50, self.log_step):
                if self.counter == counter:
                    if len(self.log_list) > 0:
                        self.ui.info_label.setText(self.log_list[0])
                        self.log_list.pop(0)
                        self.log_loop_init += self.log_step

        if self.counter == 46:
            if not self.update_handle.valid_src:
                self.update_handle.create_src()
                self.need_show_log = True
                self.log_list, self.log_step, self.old_log = self.get_log_and_step(self.update_handle,
                                                                                   self.old_log)

            elif self.update_handle.valid_src and not self.update_handle.valid_version:
                self.update_handle.update_src()
                self.need_show_log = True
                self.log_list, self.log_step, self.old_log = self.get_log_and_step(self.update_handle,
                                                                                   self.old_log)

            elif self.update_handle.valid_version and self.update_handle.valid_version:
                if self.update_handle.update_needed:
                    self.update_handle.update_src()
                    self.need_show_log = True
                    self.log_list, self.log_step, self.old_log = self.get_log_and_step(self.update_handle,
                                                                                       self.old_log)
                if not self.update_handle.update_needed:
                    self.timer.setInterval(80)

        if self.counter > 46 and self.counter <= 75:
            if self.need_show_log:
                for counter in range(self.log_loop_init, 75, self.log_step):
                    if self.counter == counter:
                        if len(self.log_list) > 0:
                            self.ui.info_label.setText(self.log_list[0])
                            self.log_list.pop(0)
                            self.log_loop_init += self.log_step

        if self.counter == 76:
            self.ui.info_label.setText('Loading...')
            self.timer.setInterval(80)

        if self.counter == 100:
            self.ui.info_label.setText('Initializing...')
            self.timer.setInterval(2000)

        self.ui.progress.setValue(self.counter)

        if self.counter == 101:
            self.timer.stop()
            new_window = getattr(importlib.import_module('src'), 'MainWindow')
            show = new_window()
            self.close()

        self.counter += 1

    def get_log_and_step(self, updater_handle, old_log):
        list_log = updater_handle.get_log()

        if old_log != 0:
            list_log = list_log[old_log:]

        step = int(23 / len(list_log))
        old_log = len(list_log)

        return list_log, step, old_log


def main():
    app = QApplication(sys.argv)
    window = LoadingScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
