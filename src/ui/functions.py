from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor, QFont, QFontDatabase, QPainter, QPixmap
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QLineEdit, QStackedWidget, QToolButton, QWidget
from .app_style import stylesheet


class UIFunctions(QWidget):

    @staticmethod
    def set_font(qwidget: QWidget, size: int, font_path: str, bold: bool, index: int=0) -> None:

        # add font to app database
        font_id = QFontDatabase.addApplicationFont(f'{font_path}')
        font_name = QFontDatabase.applicationFontFamilies(font_id)

        # get font name
        font = QFont(font_name[index])
        font.setPointSize(size)
        font.setBold(bold)
        font.setStyleStrategy(QFont.PreferAntialias)
        
        qwidget.setFont(font)
            

    def btn_style_applyer(self):
        default_style = stylesheet['btn_default']

        sender_obj = self.sender()
        parent = sender_obj.parent()
        
        self.search_entry_config(sender_obj.objectName(), parent)

        for btn in parent.findChildren(QToolButton):
            if btn.objectName() != sender_obj.objectName():
                btn.setStyleSheet(default_style)
                btn.change_color = True
                
    def search_entry_config(self, clicked_name, parent):
        
        parent = parent.parent().parent()
        
        for entry in parent.findChildren(QLineEdit):
            if entry.objectName() == 'search_entry':
                obj = entry
                
        for stackedwidget in parent.findChildren(QStackedWidget):
            if stackedwidget.objectName() == 'stack_pages':
                pages = stackedwidget
        
        if clicked_name == 'btn_scholars':
            obj.setPlaceholderText('Search by Name or Ronin account')
            self.set_drop_shadow(pages, blur=20)
        else:
            obj.setPlaceholderText('Find here...')  
            self.set_drop_shadow(pages, opacity=0)

    @staticmethod
    def paint_image(image: str, color: QColor, size: QSize) -> QPixmap:
        
        svg_render = QSvgRenderer(image)   
        new_image = QPixmap(QSize(size))
        
        painter = QPainter()
        
        new_image.fill(Qt.transparent)
        
        painter.begin(new_image)
        svg_render.render(painter)
        painter.end()
        
        paint = QPainter(new_image)
        paint.setRenderHint(QPainter.Antialiasing)
        paint.setCompositionMode(QPainter.CompositionMode_SourceIn)
        paint.fillRect(new_image.rect(), color)
        paint.end()
        
        return new_image

    @staticmethod
    def set_drop_shadow(*args: QWidget, blur: int=6, opacity: int=35) -> None:

        for element in args:
            drop_shadow = QGraphicsDropShadowEffect(element)
            drop_shadow.setBlurRadius(blur)
            drop_shadow.setOffset(0)
            drop_shadow.setColor(QColor(0, 0, 0, opacity))
            element.setGraphicsEffect(drop_shadow)
            