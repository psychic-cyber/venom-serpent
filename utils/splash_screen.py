"""
Splash screen for Venom Serpent
Professional startup screen with logo and branding
"""

from PyQt5.QtWidgets import QSplashScreen, QApplication
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QPainter, QFont, QPen, QColor
from utils.professional_theme import ProfessionalTheme

class VenomSplashScreen(QSplashScreen):
    """Professional splash screen for Venom Serpent"""
    
    def __init__(self):
        # Create splash screen pixmap
        pixmap = QPixmap(800, 600)
        pixmap.fill(QColor(ProfessionalTheme.BACKGROUND_PRIMARY))
        
        super().__init__(pixmap)
        
        # Draw splash content
        self.draw_splash_content(pixmap)
        self.setPixmap(pixmap)
        
        # Set window properties
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.SplashScreen | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, False)
        
        # Center on screen
        self.center_on_screen()
    
    def draw_splash_content(self, pixmap):
        """Draw the splash screen content"""
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Draw background gradient effect
        self.draw_background_gradient(painter, pixmap.rect())
        
        # Draw logo
        self.draw_logo(painter, pixmap.rect())
        
        # Draw title and branding
        self.draw_title_and_branding(painter, pixmap.rect())
        
        # Draw loading animation area
        self.draw_loading_area(painter, pixmap.rect())
        
        painter.end()
    
    def draw_background_gradient(self, painter, rect):
        """Draw background with gradient effect"""
        # Create a subtle gradient from jet black to dark gray
        from PyQt5.QtGui import QLinearGradient
        gradient = QLinearGradient(0, 0, 0, rect.height())
        gradient.setColorAt(0, QColor(ProfessionalTheme.BACKGROUND_PRIMARY))
        gradient.setColorAt(1, QColor(ProfessionalTheme.BACKGROUND_SECONDARY))
        
        painter.fillRect(rect, gradient)
        
        # Add some cyberpunk-style grid lines
        painter.setPen(QPen(QColor(ProfessionalTheme.BORDER_COLOR), 1))
        for i in range(0, rect.width(), 50):
            painter.drawLine(i, 0, i, rect.height())
        for i in range(0, rect.height(), 50):
            painter.drawLine(0, i, rect.width(), i)
    
    def draw_logo(self, painter, rect):
        """Draw the logo"""
        # Try to load the logo
        logo_pixmap = QPixmap("assets/logo1.png")
        if not logo_pixmap.isNull():
            # Scale logo to appropriate size
            logo_size = 120
            scaled_logo = logo_pixmap.scaled(
                logo_size, logo_size, 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            
            # Position logo in center-top area
            logo_x = (rect.width() - logo_size) // 2
            logo_y = 80
            painter.drawPixmap(logo_x, logo_y, scaled_logo)
        else:
            # Draw a placeholder if logo not found
            painter.setPen(QPen(QColor(ProfessionalTheme.DANGER), 3))
            painter.setFont(QFont("Arial", 48, QFont.Bold))
            painter.drawText(rect, Qt.AlignCenter, "🐍")
    
    def draw_title_and_branding(self, painter, rect):
        """Draw title and branding text"""
        # Main title
        painter.setPen(QPen(QColor(ProfessionalTheme.DANGER), 2))
        painter.setFont(QFont("Arial", 36, QFont.Bold))
        title_rect = rect.adjusted(0, 200, 0, -200)
        painter.drawText(title_rect, Qt.AlignCenter, "VENOM SERPENT")
        
        # Tagline
        painter.setPen(QPen(QColor(ProfessionalTheme.SUCCESS), 1))
        painter.setFont(QFont("Arial", 18, QFont.Bold))
        tagline_rect = rect.adjusted(0, 250, 0, -150)
        painter.drawText(tagline_rect, Qt.AlignCenter, "Hold My Venom 🐍")
        
        # Author
        painter.setPen(QPen(QColor(ProfessionalTheme.TEXT_SECONDARY), 1))
        painter.setFont(QFont("Arial", 14))
        author_rect = rect.adjusted(0, 280, 0, -120)
        painter.drawText(author_rect, Qt.AlignCenter, "Author: Psychic Cyber")
        
        # Version
        painter.setPen(QPen(QColor(ProfessionalTheme.WARNING), 1))
        painter.setFont(QFont("Arial", 12))
        version_rect = rect.adjusted(0, 300, 0, -100)
        painter.drawText(version_rect, Qt.AlignCenter, "v2.0 - Professional Edition")
    
    def draw_loading_area(self, painter, rect):
        """Draw loading animation area"""
        # Loading text
        painter.setPen(QPen(QColor(ProfessionalTheme.TEXT_SECONDARY), 1))
        painter.setFont(QFont("Consolas", 12))
        loading_rect = rect.adjusted(0, 400, 0, -50)
        painter.drawText(loading_rect, Qt.AlignCenter, "Initializing Attack Simulation...")
        
        # Loading bar background
        bar_rect = rect.adjusted(150, 450, -150, -30)
        painter.setPen(QPen(QColor(ProfessionalTheme.BORDER_COLOR), 2))
        painter.setBrush(QColor(ProfessionalTheme.BACKGROUND_TERTIARY))
        painter.drawRoundedRect(bar_rect, 5, 5)
        
        # Loading bar progress (animated)
        progress_width = int(bar_rect.width() * 0.3)  # 30% progress
        progress_rect = bar_rect.adjusted(0, 0, -(bar_rect.width() - progress_width), 0)
        painter.setPen(QPen(QColor(ProfessionalTheme.SUCCESS), 2))
        painter.setBrush(QColor(ProfessionalTheme.SUCCESS))
        painter.drawRoundedRect(progress_rect, 5, 5)
    
    def center_on_screen(self):
        """Center the splash screen on the screen"""
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
    
    def show_with_timer(self, duration=3000):
        """Show splash screen for specified duration"""
        self.show()
        QApplication.processEvents()
        
        # Set up timer to close splash screen
        self.timer = QTimer()
        self.timer.timeout.connect(self.close)
        self.timer.start(duration)
        
        return self.timer
