from PySide6.QtWidgets import QGraphicsDropShadowEffect, QLineEdit, QStackedWidget, QToolButton, QWidget
from .app_style import stylesheet
import tools


class UIFunctions(QWidget):            

    def btn_style_applyer(self):
        default_style = stylesheet['btn_default']

        sender_obj = self.sender()
        parent = sender_obj.parent()
        
        self.search_entry_config(sender_obj.objectName(), parent)

        for btn in parent.findChildren(QToolButton):
            if btn.objectName() != sender_obj.objectName():
                btn.setStyleSheet(default_style)
                btn.change_color = True
                
    @staticmethod
    def search_entry_config(clicked_name, parent):
        
        parent = parent.parent().parent()
        
        for entry in parent.findChildren(QLineEdit):
            if entry.objectName() == 'search_entry':
                obj = entry
                
        for stackedwidget in parent.findChildren(QStackedWidget):
            if stackedwidget.objectName() == 'stack_pages':
                pages = stackedwidget
        
        if clicked_name == 'btn_scholars':
            obj.setPlaceholderText('Search by Name or Ronin account')
            tools.set_drop_shadow(pages, blur=20)
        else:
            obj.setPlaceholderText('Find here...')  
            tools.set_drop_shadow(pages, opacity=0)
            