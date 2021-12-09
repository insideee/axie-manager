import tools
import os
import configs

dir_color = os.path.join(os.path.dirname(configs.__file__), 'colorscheme.json')
colorscheme = tools.read_json(dir_color)

stylesheet = {  'bg':f"""background-color:  {colorscheme['main colors']['application_bg']};
                        """,

                'nav_frame': f"""background-color: {colorscheme['main colors']['main_color']}
                                """,
                
                'user_frame': f"""border-bottom: 2px solid {colorscheme['main colors']['application_bg']};
                                border-right: 8px solid {colorscheme['main colors']['application_bg']};
                                """,                                
               
                'menu_frame': f"""border-bottom: 2px solid {colorscheme['main colors']['application_bg']};
                                border-right: 8px solid {colorscheme['main colors']['application_bg']}
                                """,
                                
                'version_frame': f"""border-right: 8px solid {colorscheme['main colors']['application_bg']}
                                """,

                'version_label': f"""color: {colorscheme['main colors']['application_text']}
                                """,

                'stack_page': """border-radius: 10px
                                """,
                  
                'btn_default': f""" QToolButton{{border-radius: 0px;
                                border-top-left-radius: 12px;
                                border-bottom-left-radius: 12px;
                                border: 0px;
                                padding-left: 15px;
                                color: {colorscheme['main colors']['application_text']};
                                background-color: none}}
                                """,
                                
                'btn_clicked': f"""QToolButton{{border-radius: 0px;
                                border: 0px;
                                border-top-left-radius: 12px;
                                border-bottom-left-radius: 12px;
                                padding-left: 15px;
                                color: {colorscheme['main colors']['application_text']};
                                background-color: qlineargradient(spread:pad, 
                                x1:0.424, y1:0.630773, x2:1, y2:1, stop:0 
                                {colorscheme['main colors']['second_color']}, stop:1 
                                {colorscheme['main colors']['second_color_gradient']});}}
                                """,
                                
                'btn_hover': f"""QToolButton{{border-radius: 0px;
                            border: 0px;
                            border-top-left-radius: 12px;
                            border-bottom-left-radius: 12px;
                            padding-left: 15px;
                            color: {colorscheme['main colors']['second_color']} }}
                            """,
                                
                'title_header_label': """QLabel{background-color= none;
                                        border: 0px;}
                                        """,

                'search_label_frame': """background-color: #FFFFFF;
                                        border-top-left-radius: 15px;
                                        border-bottom-left-radius: 15px;
                                        """,

                'search_entry_frame': """background-color: #FFFFFF;
                                        border-top-right-radius: 15px;
                                        border-bottom-right-radius: 15px;
                                        """,

                'search_entry': f"""color: {colorscheme['search_box']['text']};
                                background-color: #FFFFFF
                                """,

                'scholar_widget': """background-color: qlineargradient(spread:pad, 
                                x1:0.377, y1:0.33, 
                                x2:1, y2:1, stop:0 
                                #1A5071, stop:1 
                                #033F63);
                                border-radius: 15px
                                """,

                'm_profit_widget': """background-color: qlineargradient(spread:pad, 
                                x1:0.377, y1:0.33, 
                                x2:1, y2:1, stop:0 
                                #b4397c, stop:1 
                                #AC256F);
                                border-radius: 15px
                                """,

                'axies_widget': """background-color: qlineargradient(spread:pad, 
                                x1:0.377, y1:0.33, 
                                x2:1, y2:1, stop:0 
                                #674577, stop:1 
                                #583269);
                                border-radius: 15px
                                """,

                'daily_frame': """background-color: #FFFFFF;
                                border-radius: 15px;
                                """,

                'daily_label': """color: rgb(179,177,178)
                                """,
                                
                'daily_graph': """QWidget { border-radius: 15px }
                                """,
                                
                # scholars page
                'scholars_page': """ background-color: #FFFFFF;
                                border: none;
                                border-radius: 10px;
                                """,

                'filter_btn': f"""QToolButton{{background-color: {colorscheme['main colors']['widget_bg']};
                                color: {colorscheme['table_view']['main_color']};
                                padding-left: 5px;
                                border-radius: 5px}}
                                """,

                'table_header': f"""background-color: {colorscheme['table_view']['header_bg']};
                                border-bottom: 1px solid {colorscheme['table_view']['details_color']};
                                """,

                'add_btn': f"""background-color: qlineargradient(spread:paad, 
                                x1:0.377, y1:0.33, 
                                x2:1, y2:1, stop:0 
                                {colorscheme['main colors']['second_color']}, stop:1
                                {colorscheme['main colors']['second_color_gradient']});
                                color: #FFFFFF;
                                border-radius: 5px;
                                """,
                                
                'title_table': f"""color: {colorscheme['main colors']['second_color']}""",
                
                'bottom_info': f"""color: {colorscheme['main colors']['main_color']}
                                """,
                                
                'login_bg': f"""background-color: {colorscheme['main colors']['application_bg']}
                                """,

                'logo_login_frame': f"""background-color: {colorscheme['main colors']['main_color']}
                                        """,
                                        
                'login_title_text': f"""color: {colorscheme['login']['main_color']}
                                        """,

                'login_info_entry': f"""color: {colorscheme['login']['info_text']}
                                        """,
                                        
                'login_entry': f"""QLineEdit{{color: {colorscheme['login']['main_color']};
                                background-color: {colorscheme['main colors']['application_bg']};
                                border: 1px solid {colorscheme['login']['info_text']};
                                border-radius: 7px}}
                                QLineEdit::focus{{border-bottom: 1px solid {colorscheme['login']['main_color']}}}
                                """,
                                
                'login_btn': f"""QPushButton{{color: {colorscheme['main colors']['application_bg']};
                                background-color: {colorscheme['login']['main_color']};
                                border: 1px solid {colorscheme['login']['info_text']};
                                border-radius: 7px}}
                                QPushButton::pressed{{background-color: {colorscheme['login']['click_btn']};}}
                                """,
                                
                'login_question_label': f"""color: {colorscheme['login']['main_color']};
                                        """,
                                        
                'login_question_btn': f"""QPushButton{{color: {colorscheme['login']['second_color']};
                                        background-color: {colorscheme['main colors']['application_bg']};
                                        border: none}},
                                        QPushButton::focus{{border: none}}
                                        """,
                                        
                'rememberme_btn': f"""QRadioButton{{color: {colorscheme['login']['info_text']}
                                        }}
                                        QRadioButton::indicator{{border:1px solid {colorscheme['login']['info_text']};
                                        border-radius: 7px}}
                                        QRadioButton::indicator::checked{{background-color: {colorscheme['login']['info_text']}}}
                                        """,
                
                'forgot_btn': f"""QPushButton{{color: {colorscheme['login']['main_color']};
                                        background-color: {colorscheme['main colors']['application_bg']};
                                        border: none}},
                                        QPushButton::focus{{border: none}}
                                        """,
                                        


                             }
