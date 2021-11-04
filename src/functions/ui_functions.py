
from PySide6 import QtGui
from PySide6.QtWidgets import QWidget


class UIFunctions:

    @staticmethod
    def set_font(qwidget: QWidget, size: int, font_path: str, bold: bool) -> None:

        # add font to app database
        font_id = QtGui.QFontDatabase.addApplicationFont(f'{font_path}')
        font_name = QtGui.QFontDatabase.applicationFontFamilies(font_id)

        # get font name
        font = QtGui.QFont(font_name[0])
        font.setPointSize(size)
        font.setBold(bold)

        qwidget.setFont(font)