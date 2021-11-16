from PySide6.QtCore import QEvent
from PySide6.QtWidgets import QFrame, QMainWindow, QApplication
from PySide6.QtGui import QMouseEvent
from ui import Ui_App
import sys


class App(QMainWindow):

    def __init__(self) -> None:
        super(App, self).__init__()
        self.ui = Ui_App()
        self.ui.init_gui(self)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        
        # remove cursor when search lose focus
        focus_widget = QApplication.focusWidget()

        if hasattr(focus_widget, 'objectName'):
            if focus_widget.objectName() == 'search_entry':
                focus_widget.clearFocus()
                
        return super().mousePressEvent(event)  

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
