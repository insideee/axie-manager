from PySide6.QtCharts import QBarCategoryAxis, QBarSet, QChart, QChartView, QStackedBarSeries, QValueAxis
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QFont, QFontDatabase, QGradient, QLinearGradient, QPainter, QPalette, qRgb, qRgba
from PySide6.QtWidgets import QToolTip, QVBoxLayout, QWidget

    
class GraphReports(QWidget):
    
    def __init__(self):
        super(GraphReports, self).__init__()
        self.setObjectName('graph_reports')
        self.setStyleSheet('QWidget { border-radius: 15px }')
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        
        # 100 scholars 180 daily goal each
        self.daily_goal = 18000
        self.min_month = 10400
        self.max_month = 21500
        
        self.min = QBarSet('Déficit')
        self.max = QBarSet('Profit')
        self.month_values = []
        # append month values
        self.min.append([(14000 - self.daily_goal), 0, -0, (12400 - self.daily_goal), -0 ,(17500 - self.daily_goal)])
        self.max.append([0, (21000 - self.daily_goal), (19650 - self.daily_goal), 0, (18200 -self.daily_goal), 0])
        
        self.series = QStackedBarSeries()
        self.series.append(self.min)
        self.series.append(self.max)
        
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setBackgroundBrush(QColor('#F4F4F4'))
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        
        # x & y
        self.categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]                
        self.axisX = QBarCategoryAxis()
        self.axisX.append(self.categories)
        self.chart.addAxis(self.axisX, Qt.AlignBottom)
        
        self.axisY = QValueAxis()
        # lower and higher month value - daily goal
        self.axisY.setRange(int(self.min_month - self.daily_goal), int(self.max_month - self.daily_goal))
        self.chart.addAxis(self.axisY, Qt.AlignLeft)
        
        self.series.attachAxis(self.axisX)
        self.series.attachAxis(self.axisY)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chart.layout().setContentsMargins(0, 0, 0, 0)    
        self.chart.setBackgroundRoundness(15)    
        
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.layout.addWidget(self.chart_view)
        
        self.graph_customization(deficit_profit=True)
        
    def graph_customization(self, deficit_profit=False):
        """Customize the axis according with the selected graph

        Args:
            deficit_profit (bool, optional): Deficit/profit model. Defaults to False.
        """
        
        if deficit_profit:
            # add font to app database
            font_id = QFontDatabase.addApplicationFont(':/fonts/fonts/Montserrat-Medium.ttf')
            font_name = QFontDatabase.applicationFontFamilies(font_id)

            # get font name
            font = QFont(font_name[1])
            font.setPointSize(10)
            font.setBold(True)
            font.setStyleStrategy(QFont.PreferAntialias)
            
            
            
            self.axisX.setLabelsFont(font)
            self.axisY.setLabelsFont(font)
            brush = QBrush(qRgb(179,177,178))
            self.axisY.setLabelsBrush(brush)
            self.axisX.setLabelsBrush(brush)
            self.axisX.setGridLineVisible(False)
            
            self.chart.legend().setFont(font)
            self.chart.legend().setLabelBrush(brush)
            
            brush = QBrush(self.gradient_color(qRgb(0, 199, 255), qRgb(56, 160, 255)))
            self.max.setBrush(brush)
            
            brush = QBrush(self.gradient_color(qRgb(193,160,203), qRgb(166,118,178)))
            self.min.setBrush(brush)
            
    def gradient_color(self, color_1, color_2):
        """Return a gradient color

        Args:
            color_1 (qRgb): Color value 1
            color_2 (qRgb): Color value 2

        Returns:
            QLinearGradient
        """
        color_gradient = QLinearGradient(0, 0, 640, 120)
        color_gradient.setSpread(QGradient.PadSpread)
        color_gradient.setColorAt(0, color_1)
        color_gradient.setColorAt(1, color_2)
        
        return color_gradient
