
from PySide6 import QtGui
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QToolButton, QWidget
from .style import Style


class UIFunctions(QWidget):

    @staticmethod
    def set_font(qwidget: QWidget, size: int, font_path: str, bold: bool, index: int=0) -> None:

        # add font to app database
        font_id = QtGui.QFontDatabase.addApplicationFont(f'{font_path}')
        font_name = QtGui.QFontDatabase.applicationFontFamilies(font_id)

        # get font name
        font = QtGui.QFont(font_name[index])
        font.setPointSize(size)
        font.setBold(bold)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        
        qwidget.setFont(font)
            

    def btn_style_applyer(self):
        default_style = Style.btn_default
        clicked_style = Style.btn_clicked

        sender_obj = self.sender()
        parent = sender_obj.parent()

        for btn in parent.findChildren(QToolButton):
            if btn.objectName() != sender_obj.objectName():
                btn.setStyleSheet(default_style)
                btn.change_color = True
            elif btn.objectName() != 'btn_toggle':
                btn.setStyleSheet(clicked_style)

    @staticmethod
    def paint_image(image: str, color) -> QtGui.QPixmap:


        new_image = QtGui.QPixmap(image)
        paint = QtGui.QPainter(new_image)
        paint.setRenderHint(QtGui.QPainter.Antialiasing)
        paint.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
        paint.fillRect(new_image.rect(), color)
        paint.end()

        return new_image

    @staticmethod
    def set_drop_shadow(*args: QWidget, blur: int=6, opacity: int=35) -> None:

        for element in args:
            drop_shadow = QGraphicsDropShadowEffect(element)
            drop_shadow.setBlurRadius(blur)
            drop_shadow.setOffset(0)
            drop_shadow.setColor(QtGui.QColor(0, 0, 0, opacity))
            element.setGraphicsEffect(drop_shadow)