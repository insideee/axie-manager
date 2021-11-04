from PySide6.QtGui import qAlpha
from PySide6.QtWidgets import QMainWindow, QApplication
from ui import Ui_App
import sys


class App(QMainWindow):

    def __init__(self) -> None:
        super(App, self).__init__()
        self.ui = Ui_App()
        self.ui.init_gui(self)
        

        self.move(1750, 250)


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

    