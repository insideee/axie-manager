from PySide6.QtCore import QObject, QSize, Qt
from PySide6.QtGui import QColor, QPainter, QPixmap
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QWidget
import json
import ast

class Functions(QWidget):   

    @staticmethod
    def paint_image(image: str, color: QColor, size: QSize) -> QPixmap:
        """Paint, resize and return a QPixmap image.
        """
        
        
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
    def set_drop_shadow(*args: QObject, blur: int=6, opacity: int=35) -> None:
        """Set a drop shadow effect to the target element.
        """

        for element in args:
            drop_shadow = QGraphicsDropShadowEffect(element)
            drop_shadow.setBlurRadius(blur)
            drop_shadow.setOffset(0)
            drop_shadow.setColor(QColor(0, 0, 0, opacity))
            element.setGraphicsEffect(drop_shadow)
            
    @staticmethod
    def read_json(file_path: str) -> dict:
        """Load a json file and return a dict.
        """
        
        with open(file_path, 'r') as json_file:
            
            return json.loads(json_file.read())