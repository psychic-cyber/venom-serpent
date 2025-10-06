"""
Professional Enterprise Theme for Venom Serpent
Modern, clean, enterprise-grade styling
"""

from PyQt5.QtGui import QPalette, QColor, QFont

class ProfessionalTheme:
    """Professional enterprise theme for Venom Serpent"""
    
    # Professional Color Palette
    BACKGROUND_PRIMARY = "#0D1117"      # GitHub dark
    BACKGROUND_SECONDARY = "#161B22"    # Slightly lighter
    BACKGROUND_TERTIARY = "#21262D"     # Card background
    BORDER_COLOR = "#30363D"            # Subtle borders
    BORDER_ACCENT = "#58A6FF"           # Blue accent
    
    # Text Colors
    TEXT_PRIMARY = "#F0F6FC"            # Primary text
    TEXT_SECONDARY = "#8B949E"          # Secondary text
    TEXT_MUTED = "#6E7681"              # Muted text
    
    # Status Colors
    SUCCESS = "#3FB950"                 # Green
    WARNING = "#D29922"                 # Orange
    DANGER = "#F85149"                  # Red
    INFO = "#58A6FF"                    # Blue
    
    # Interactive Colors
    PRIMARY = "#238636"                 # GitHub green
    PRIMARY_HOVER = "#2EA043"
    PRIMARY_ACTIVE = "#1A7F37"
    
    SECONDARY = "#21262D"               # Gray
    SECONDARY_HOVER = "#30363D"
    SECONDARY_ACTIVE = "#161B22"
    
    # Fonts
    FONT_FAMILY = "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    FONT_MONO = "JetBrains Mono, Consolas, Monaco, monospace"
    
    @staticmethod
    def get_main_window_style():
        """Main window styling"""
        return f"""
        QMainWindow {{
            background-color: {ProfessionalTheme.BACKGROUND_PRIMARY};
            color: {ProfessionalTheme.TEXT_PRIMARY};
            font-family: {ProfessionalTheme.FONT_FAMILY};
        }}
        QWidget {{
            background-color: {ProfessionalTheme.BACKGROUND_PRIMARY};
            color: {ProfessionalTheme.TEXT_PRIMARY};
            font-family: {ProfessionalTheme.FONT_FAMILY};
        }}
        QSplitter::handle {{
            background-color: {ProfessionalTheme.BORDER_COLOR};
            width: 1px;
        }}
        QSplitter::handle:hover {{
            background-color: {ProfessionalTheme.BORDER_ACCENT};
        }}
        """
    
    @staticmethod
    def get_panel_style():
        """Panel styling - clean and minimal"""
        return f"""
        QFrame {{
            background-color: {ProfessionalTheme.BACKGROUND_SECONDARY};
            border: 1px solid {ProfessionalTheme.BORDER_COLOR};
            border-radius: 8px;
            padding: 16px;
        }}
        """
    
    @staticmethod
    def get_button_style(button_type="primary"):
        """Professional button styling"""
        if button_type == "primary":
            return f"""
            QPushButton {{
                background-color: {ProfessionalTheme.PRIMARY};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                font-family: {ProfessionalTheme.FONT_FAMILY};
                font-size: 13px;
                font-weight: 600;
                min-height: 36px;
            }}
            QPushButton:hover {{
                background-color: {ProfessionalTheme.PRIMARY_HOVER};
                border: 2px solid {ProfessionalTheme.PRIMARY};
            }}
            QPushButton:pressed {{
                background-color: {ProfessionalTheme.PRIMARY_ACTIVE};
                border: 2px solid {ProfessionalTheme.PRIMARY_ACTIVE};
            }}
            QPushButton:disabled {{
                background-color: {ProfessionalTheme.BACKGROUND_TERTIARY};
                color: {ProfessionalTheme.TEXT_MUTED};
            }}
            """
        elif button_type == "success":
            return f"""
            QPushButton {{
                background-color: {ProfessionalTheme.SUCCESS};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                font-family: {ProfessionalTheme.FONT_FAMILY};
                font-size: 13px;
                font-weight: 600;
                min-height: 36px;
            }}
            QPushButton:hover {{
                background-color: #4CC35A;
                border: 2px solid #4CC35A;
            }}
            QPushButton:pressed {{
                background-color: #2D9A3D;
                border: 2px solid #2D9A3D;
            }}
            """
        elif button_type == "warning":
            return f"""
            QPushButton {{
                background-color: {ProfessionalTheme.WARNING};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                font-family: {ProfessionalTheme.FONT_FAMILY};
                font-size: 13px;
                font-weight: 600;
                min-height: 36px;
            }}
            QPushButton:hover {{
                background-color: #E6A23C;
                border: 2px solid #E6A23C;
            }}
            QPushButton:pressed {{
                background-color: #B8860B;
                border: 2px solid #B8860B;
            }}
            """
        else:  # secondary
            return f"""
            QPushButton {{
                background-color: {ProfessionalTheme.SECONDARY};
                color: {ProfessionalTheme.TEXT_PRIMARY};
                border: 1px solid {ProfessionalTheme.BORDER_COLOR};
                border-radius: 6px;
                padding: 10px 20px;
                font-family: {ProfessionalTheme.FONT_FAMILY};
                font-size: 13px;
                font-weight: 500;
                min-height: 36px;
            }}
            QPushButton:hover {{
                background-color: {ProfessionalTheme.SECONDARY_HOVER};
                border: 2px solid {ProfessionalTheme.BORDER_ACCENT};
            }}
            QPushButton:pressed {{
                background-color: {ProfessionalTheme.SECONDARY_ACTIVE};
                border: 2px solid {ProfessionalTheme.SECONDARY_ACTIVE};
            }}
            """
    
    @staticmethod
    def get_label_style(label_type="normal", screen_width=1920):
        """Professional label styling with responsive sizing"""
        # Responsive font sizes based on screen width
        if screen_width >= 1920:  # Large screens
            title_size = "18px"
            header_size = "16px"
            normal_size = "13px"
        elif screen_width >= 1366:  # Medium screens
            title_size = "16px"
            header_size = "14px"
            normal_size = "12px"
        else:  # Small screens
            title_size = "14px"
            header_size = "12px"
            normal_size = "11px"
            
        if label_type == "title":
            return f"""
            QLabel {{
                color: {ProfessionalTheme.TEXT_PRIMARY};
                font-family: {ProfessionalTheme.FONT_FAMILY};
                font-size: {title_size};
                font-weight: 700;
                margin: 0;
                padding: 0;
            }}
            """
        elif label_type == "header":
            return f"""
            QLabel {{
                color: {ProfessionalTheme.TEXT_PRIMARY};
                font-family: {ProfessionalTheme.FONT_FAMILY};
                font-size: {header_size};
                font-weight: 600;
                margin: 0 0 12px 0;
            }}
            """
        elif label_type == "subtitle":
            return f"""
            QLabel {{
                color: {ProfessionalTheme.TEXT_SECONDARY};
                font-family: {ProfessionalTheme.FONT_FAMILY};
                font-size: {normal_size};
                font-weight: 500;
                margin: 0 0 8px 0;
            }}
            """
        else:  # normal
            return f"""
            QLabel {{
                color: {ProfessionalTheme.TEXT_PRIMARY};
                font-family: {ProfessionalTheme.FONT_FAMILY};
                font-size: {normal_size};
                font-weight: 400;
                margin: 0;
                padding: 0;
            }}
            """
    
    @staticmethod
    def get_input_style():
        """Professional input styling"""
        return f"""
        QLineEdit, QTextEdit {{
            background-color: {ProfessionalTheme.BACKGROUND_TERTIARY};
            color: {ProfessionalTheme.TEXT_PRIMARY};
            border: 1px solid {ProfessionalTheme.BORDER_COLOR};
            border-radius: 6px;
            padding: 8px 12px;
            font-family: {ProfessionalTheme.FONT_FAMILY};
            font-size: 13px;
        }}
        QLineEdit:focus, QTextEdit:focus {{
            border-color: {ProfessionalTheme.BORDER_ACCENT};
            outline: none;
        }}
        QLineEdit::placeholder, QTextEdit::placeholder {{
            color: {ProfessionalTheme.TEXT_MUTED};
        }}
        """
    
    @staticmethod
    def get_tab_widget_style():
        """Professional tab widget styling"""
        return f"""
        QTabWidget::pane {{
            border: 1px solid {ProfessionalTheme.BORDER_COLOR};
            border-radius: 8px;
            background-color: {ProfessionalTheme.BACKGROUND_SECONDARY};
        }}
        QTabBar::tab {{
            background-color: {ProfessionalTheme.BACKGROUND_TERTIARY};
            color: {ProfessionalTheme.TEXT_SECONDARY};
            border: 1px solid {ProfessionalTheme.BORDER_COLOR};
            border-bottom: none;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
            padding: 12px 20px;
            margin-right: 2px;
            font-family: {ProfessionalTheme.FONT_FAMILY};
            font-size: 13px;
            font-weight: 500;
            min-width: 120px;
        }}
        QTabBar::tab:selected {{
            background-color: {ProfessionalTheme.BACKGROUND_SECONDARY};
            color: {ProfessionalTheme.TEXT_PRIMARY};
            border-color: {ProfessionalTheme.BORDER_ACCENT};
        }}
        QTabBar::tab:hover {{
            background-color: {ProfessionalTheme.BACKGROUND_TERTIARY};
            color: {ProfessionalTheme.TEXT_PRIMARY};
        }}
        """
    
    @staticmethod
    def get_progress_bar_style():
        """Professional progress bar styling"""
        return f"""
        QProgressBar {{
            border: 1px solid {ProfessionalTheme.BORDER_COLOR};
            border-radius: 4px;
            text-align: center;
            background-color: {ProfessionalTheme.BACKGROUND_TERTIARY};
            color: {ProfessionalTheme.TEXT_PRIMARY};
            font-family: {ProfessionalTheme.FONT_FAMILY};
            font-size: 12px;
            font-weight: 500;
            height: 20px;
        }}
        QProgressBar::chunk {{
            background-color: {ProfessionalTheme.SUCCESS};
            border-radius: 3px;
        }}
        """
    
    @staticmethod
    def get_log_panel_style():
        """Professional log panel styling"""
        return f"""
        QTextEdit {{
            background-color: {ProfessionalTheme.BACKGROUND_TERTIARY};
            color: {ProfessionalTheme.TEXT_PRIMARY};
            border: 1px solid {ProfessionalTheme.BORDER_COLOR};
            border-radius: 6px;
            padding: 12px;
            font-family: {ProfessionalTheme.FONT_MONO};
            font-size: 12px;
            line-height: 1.4;
        }}
        QScrollBar:vertical {{
            background-color: {ProfessionalTheme.BACKGROUND_TERTIARY};
            width: 12px;
            border-radius: 6px;
        }}
        QScrollBar::handle:vertical {{
            background-color: {ProfessionalTheme.BORDER_COLOR};
            border-radius: 6px;
            min-height: 20px;
        }}
        QScrollBar::handle:vertical:hover {{
            background-color: {ProfessionalTheme.BORDER_ACCENT};
        }}
        """
    
    @staticmethod
    def get_group_box_style():
        """Professional group box styling"""
        return f"""
        QGroupBox {{
            color: {ProfessionalTheme.TEXT_PRIMARY};
            font-family: {ProfessionalTheme.FONT_FAMILY};
            font-size: 14px;
            font-weight: 600;
            border: 1px solid {ProfessionalTheme.BORDER_COLOR};
            border-radius: 8px;
            margin-top: 12px;
            padding-top: 12px;
        }}
        QGroupBox::title {{
            subcontrol-origin: margin;
            left: 12px;
            padding: 0 8px;
            background-color: {ProfessionalTheme.BACKGROUND_SECONDARY};
        }}
        """
    
    @staticmethod
    def get_timeline_style():
        """Professional timeline styling"""
        return f"""
        QListWidget {{
            background-color: {ProfessionalTheme.BACKGROUND_TERTIARY};
            border: 1px solid {ProfessionalTheme.BORDER_COLOR};
            border-radius: 6px;
            padding: 8px;
            font-family: {ProfessionalTheme.FONT_FAMILY};
            font-size: 13px;
        }}
        QListWidget::item {{
            background-color: transparent;
            color: {ProfessionalTheme.TEXT_PRIMARY};
            padding: 8px 12px;
            border-radius: 4px;
            margin: 2px 0;
        }}
        QListWidget::item:hover {{
            background-color: {ProfessionalTheme.BACKGROUND_SECONDARY};
        }}
        QListWidget::item:selected {{
            background-color: {ProfessionalTheme.PRIMARY};
            color: white;
        }}
        QScrollBar:vertical {{
            background-color: {ProfessionalTheme.BACKGROUND_TERTIARY};
            width: 12px;
            border-radius: 6px;
        }}
        QScrollBar::handle:vertical {{
            background-color: {ProfessionalTheme.BORDER_COLOR};
            border-radius: 6px;
            min-height: 20px;
        }}
        QScrollBar::handle:vertical:hover {{
            background-color: {ProfessionalTheme.BORDER_ACCENT};
        }}
        """
