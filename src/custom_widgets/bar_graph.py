from PySide6.QtCore import QSize, Qt, QRectF
from PySide6.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PySide6.QtGui import QPaintEvent, QPainter, QPen, QFont, QColor
from datetime import datetime
import calendar


class BarGraph(QWidget):
    def __init__(self, width, height, font_family='Segoi'):
        super(BarGraph, self).__init__()

        self.width = width
        self.height = height
        self.bar_color = 0xE64C3C
        self.bar_size = 35
        self.graph_data = {
            'graph1': 0,
            'graph2': 0,
            'graph3': 0
        }
        self.shadow = None
        self.shadow_blur_radius = 6

        self.data_text_color = 0xE64C3C

        self.text_color = 0x737373
        self.font = font_family
        self.font_size = 10

        self.border = False
        self.border_width = 5
        self.border_color = 0x737373
        self.border_round_size = 5

        self.graph_line = True
        self.graph_line_color = 0x737373
        self.graph_line_size = 1
        
        self.set_shadow(True)

        self.setMinimumSize(QSize(self.width, self.height))
        self.setMaximumSize(QSize(self.width, self.height))

    def paintEvent(self, event: QPaintEvent) -> None:

        max_extend = 160
        y_pos = max_extend + 20
        base_value = self.get_graph_base_value()
        extend_values = self.get_extend_values(max_extend, base_value, y_pos)

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setFont(QFont(self.font, self.font_size))

        pen = QPen()
        painter.setPen(pen)

        # border rect
        if self.border:
            pen.setColor(self.border_color)
            pen.setWidth(self.border_width)
            rect = QRectF(0, 0, self.width, self.height)
            painter.drawRoundRect(rect, self.border_round_size, self.border_round_size)

        # graph lines
        if self.graph_line:
            pen.setColor(self.graph_line_color)
            pen.setWidth(self.graph_line_size)

            painter.setPen(pen)

            painter.drawLine(10, y_pos + 18, 10, max_extend - self.width)

            painter.drawLine(0, y_pos + 8, 185, y_pos + 8)

        # graph data bar
        pen.setColor(self.bar_color)
        pen.setWidth(self.bar_size)
        pen.setCapStyle(Qt.FlatCap)

        painter.setPen(pen)

        for k, v in extend_values.items():
            if int(v) == y_pos:
                extend_values[k] = int(v) - 1

        painter.drawLine(50, (max_extend + 20), 50, extend_values['graph1'])
        painter.drawLine(100, (max_extend + 20), 100, extend_values['graph2'])
        painter.drawLine(150, (max_extend + 20), 150, extend_values['graph3'])

        # text data values
        pen.setColor(self.data_text_color)
        painter.setPen(pen)
        text_x_pos = self.get_data_text_pos()

        painter.drawText(text_x_pos['graph1'], (extend_values['graph1'] - 5), str(self.graph_data['graph1']))
        painter.drawText(text_x_pos['graph2'], (extend_values['graph2'] - 5), str(self.graph_data['graph2']))
        painter.drawText(text_x_pos['graph3'], (extend_values['graph3'] - 5), str(self.graph_data['graph3']))

        # text months names
        pen.setColor(self.text_color)
        painter.setPen(pen)

        month_name = self.get_month_name()
        painter.drawText(50 - 8, (y_pos + 23), month_name['graph1'])
        painter.drawText(99 - 11, (y_pos + 23), month_name['graph2'])
        painter.drawText(150 - 9, (y_pos + 23), month_name['graph3'])

    def get_graph_base_value(self) -> int:

        base_value = 0

        for k, v in self.graph_data.items():
            if v > base_value:
                base_value = v

        return base_value

    def get_extend_values(self, max_extends: int, base_value: int, y_pos: int) -> dict:

        extend_values = {}

        for k, v in self.graph_data.items():
            try:
                percent = v / base_value
            except ZeroDivisionError:
                percent = 0

            extend_values[k] = y_pos - (percent * max_extends)

        return extend_values

    def get_data_text_pos(self):
        text_x_pos = {
            'graph1': 50,
            'graph2': 99,
            'graph3': 150
        }

        for k, v in self.graph_data.items():
            if v <= 9:
                text_x_pos[k] -= 4
            elif 9 < v < 99:
                text_x_pos[k] -= 6
            elif 99 < v < 999:
                text_x_pos[k] -= 12
            elif 999 < v < 9999:
                text_x_pos[k] -= 15
            elif 9999 < v < 99999:
                text_x_pos[k] -= 19
            elif 99999 < v < 999999:
                text_x_pos[k] -= 23
            else:
                text_x_pos[k] -= 26

        return text_x_pos

    def get_month_name(self) -> dict:
        month_name = {}
        current_month = datetime.today().month
        count = 2

        for k, v in self.graph_data.items():
            month_name[k] = calendar.month_abbr[current_month - count]
            count -= 1

        return month_name

    def set_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect()
            self.shadow.setBlurRadius(self.shadow_blur_radius)
            self.shadow.setOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 90))
            self.setGraphicsEffect(self.shadow)

    def update_value(self, graph1: int, graph2: int, graph3: int) -> None:
        self.graph_data = {
            'graph1': graph1,
            'graph2': graph2,
            'graph3': graph3
        }

        self.repaint()

# ideas
# in the first time wen user ll add a scholar
# the window asking if he want to add manually a partial
# monthly profit because the widget ll show the data after
# the first scholar added
