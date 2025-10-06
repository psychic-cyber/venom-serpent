"""
Base step window class for Venom Serpent
Provides common functionality for all attack step windows
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                            QPushButton, QTextEdit, QFrame, QProgressBar)
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtGui import QPixmap, QFont
from utils.professional_theme import ProfessionalTheme

class BaseStepWindow(QWidget):
    """Base class for attack step windows"""
    
    step_completed = pyqtSignal(str)  # Emitted when step is completed
    next_step_requested = pyqtSignal()  # Emitted when next step is requested
    
    def __init__(self, step_id, step_name, parent=None):
        super().__init__(parent)
        self.step_id = step_id
        self.step_name = step_name
        self.is_completed = False
        self.target_info = None
        
        self.init_ui()
        self.apply_theme()
    
    def init_ui(self):
        """Initialize the UI - to be overridden by subclasses"""
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Header with logo and title (simplified)
        header_widget = self.create_header()
        layout.addWidget(header_widget)
        
        # Main content area
        content_layout = self.create_content_area()
        layout.addLayout(content_layout)
        
        # Control buttons
        button_layout = self.create_button_frame()
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def create_header(self):
        """Create header with step name on left and status on right"""
        # Create header container with background
        header_container = QWidget()
        header_container.setStyleSheet(f"""
            QWidget {{
                background-color: {ProfessionalTheme.BACKGROUND_TERTIARY};
                border: 1px solid {ProfessionalTheme.BORDER_COLOR};
                border-radius: 6px;
                margin: 5px;
            }}
        """)
        
        header_layout = QHBoxLayout(header_container)
        header_layout.setSpacing(0)
        header_layout.setContentsMargins(15, 10, 15, 10)  # Added padding
        
        # Step title - left side
        title_label = QLabel(f"Step: {self.step_name}")
        title_label.setStyleSheet(ProfessionalTheme.get_label_style("title"))
        title_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        header_layout.addWidget(title_label)
        
        header_layout.addStretch()
        
        # Status indicator - right side
        self.status_label = QLabel("Ready")
        self.status_label.setStyleSheet(ProfessionalTheme.get_label_style("normal"))
        self.status_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        header_layout.addWidget(self.status_label)
        
        return header_container
    
    def create_content_area(self):
        """Create main content area with visual enhancements"""
        content_layout = QVBoxLayout()
        content_layout.setSpacing(0)
        content_layout.setContentsMargins(0, 0, 0, 0)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet(ProfessionalTheme.get_progress_bar_style())
        self.progress_bar.setVisible(False)
        content_layout.addWidget(self.progress_bar)
        
        # Main content area with actual content
        main_content = QWidget()
        main_content.setStyleSheet(f"""
            QWidget {{
                background-color: {ProfessionalTheme.BACKGROUND_TERTIARY};
                border: 1px solid {ProfessionalTheme.BORDER_COLOR};
                border-radius: 8px;
                margin: 10px;
            }}
        """)
        
        main_layout = QVBoxLayout(main_content)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Step icon and title
        header_layout = QHBoxLayout()
        step_icons = {
            "Reconnaissance": "🔍",
            "Exploitation": "💥", 
            "Payload Delivery": "📦",
            "Persistence": "🔒",
            "Cover Tracks": "🧹"
        }
        
        icon_label = QLabel(step_icons.get(self.step_name, "⚡"))
        icon_label.setStyleSheet("font-size: 32px; color: #2196F3;")
        header_layout.addWidget(icon_label)
        
        title_label = QLabel(f"{self.step_name} Phase")
        title_label.setStyleSheet(f"""
            QLabel {{
                color: {ProfessionalTheme.TEXT_PRIMARY};
                font-family: {ProfessionalTheme.FONT_FAMILY};
                font-size: 24px;
                font-weight: 700;
                margin-left: 15px;
            }}
        """)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        main_layout.addLayout(header_layout)
        
        # Description
        desc_label = QLabel(f"Execute {self.step_name.lower()} operations to gather intelligence and identify vulnerabilities.")
        desc_label.setStyleSheet(f"""
            QLabel {{
                color: {ProfessionalTheme.TEXT_SECONDARY};
                font-family: {ProfessionalTheme.FONT_FAMILY};
                font-size: 14px;
                margin: 10px 0;
            }}
        """)
        desc_label.setWordWrap(True)
        main_layout.addWidget(desc_label)
        
        # Status info
        status_info = QLabel("Status: Ready to begin • Target: 127.0.0.1 • Mode: Simulation")
        status_info.setStyleSheet(f"""
            QLabel {{
                color: {ProfessionalTheme.SUCCESS};
                font-family: {ProfessionalTheme.FONT_FAMILY};
                font-size: 12px;
                margin: 5px 0;
            }}
        """)
        main_layout.addWidget(status_info)
        
        # Add content to fill empty space
        content_section = QLabel("Click 'Execute Step' to begin the reconnaissance phase and discover open ports, services, and vulnerabilities on the target system.")
        content_section.setStyleSheet(f"""
            QLabel {{
                color: {ProfessionalTheme.TEXT_SECONDARY};
                font-family: {ProfessionalTheme.FONT_FAMILY};
                font-size: 14px;
                margin: 20px 0;
                padding: 15px;
                background-color: {ProfessionalTheme.BACKGROUND_SECONDARY};
                border: 1px solid {ProfessionalTheme.BORDER_COLOR};
                border-radius: 6px;
            }}
        """)
        content_section.setWordWrap(True)
        main_layout.addWidget(content_section)
        
        # Add phase details to fill remaining space
        details_section = QLabel("""
        <b>Reconnaissance Phase Details:</b><br>
        • Port Scanning: Identify open ports and services<br>
        • Service Detection: Determine running services and versions<br>
        • Vulnerability Assessment: Discover potential security weaknesses<br>
        • Network Mapping: Map the target network topology<br>
        • Information Gathering: Collect intelligence about the target
        """)
        details_section.setStyleSheet(f"""
            QLabel {{
                color: {ProfessionalTheme.TEXT_PRIMARY};
                font-family: {ProfessionalTheme.FONT_FAMILY};
                font-size: 13px;
                margin: 10px 0;
                padding: 15px;
                background-color: {ProfessionalTheme.BACKGROUND_TERTIARY};
                border: 1px solid {ProfessionalTheme.BORDER_COLOR};
                border-radius: 6px;
                line-height: 1.4;
            }}
        """)
        details_section.setWordWrap(True)
        main_layout.addWidget(details_section)
        
        content_layout.addWidget(main_content)
        
        # Log output area
        self.log_output = QTextEdit()
        self.log_output.setStyleSheet(ProfessionalTheme.get_log_panel_style())
        self.log_output.setReadOnly(True)
        self.log_output.setMaximumHeight(1500)  # Much larger height for maximum visibility
        content_layout.addWidget(self.log_output)
        
        return content_layout
    
    def create_button_frame(self):
        """Create clean button frame"""
        button_layout = QHBoxLayout()
        button_layout.setSpacing(0)
        button_layout.setContentsMargins(0, 15, 0, 0)  # Added top margin for buttons
        
        # Execute button
        self.execute_btn = QPushButton("Execute Step")
        self.execute_btn.setStyleSheet(ProfessionalTheme.get_button_style("primary"))
        self.execute_btn.clicked.connect(self.execute_step)
        button_layout.addWidget(self.execute_btn)
        
        button_layout.addStretch()
        
        # Next step button
        self.next_btn = QPushButton("Next Step")
        self.next_btn.setStyleSheet(ProfessionalTheme.get_button_style("success"))
        self.next_btn.clicked.connect(self.next_step)
        self.next_btn.setEnabled(False)
        button_layout.addWidget(self.next_btn)
        
        return button_layout
    
    def apply_theme(self):
        """Apply the cyberpunk theme"""
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {ProfessionalTheme.BACKGROUND_PRIMARY};
                color: {ProfessionalTheme.TEXT_PRIMARY};
            }}
        """)
    
    def set_target_info(self, target_info):
        """Set target information for this step"""
        self.target_info = target_info
    
    def execute_step(self):
        """Execute the step - to be overridden by subclasses"""
        self.status_label.setText("Executing...")
        self.status_label.setStyleSheet(ProfessionalTheme.get_label_style("warning"))
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.execute_btn.setEnabled(False)
    
    def next_step(self):
        """Move to next step"""
        self.next_step_requested.emit()
    
    def step_completed_successfully(self):
        """Mark step as completed successfully"""
        self.is_completed = True
        self.status_label.setText("Completed ✓")
        self.status_label.setStyleSheet(ProfessionalTheme.get_label_style("success"))
        self.progress_bar.setValue(100)
        self.next_btn.setEnabled(True)
        self.execute_btn.setText("Re-execute")
        self.execute_btn.setEnabled(True)
        self.step_completed.emit(self.step_id)
    
    def step_failed(self, error_message=""):
        """Mark step as failed"""
        self.status_label.setText(f"Failed: {error_message}")
        self.status_label.setStyleSheet(ProfessionalTheme.get_label_style("error"))
        self.execute_btn.setEnabled(True)
        self.execute_btn.setText("Retry")
    
    def add_log(self, message, log_type="info"):
        """Add a log message to the output"""
        timestamp = QTimer().remainingTime()  # Simple timestamp
        color = self.get_log_color(log_type)
        
        formatted_message = f'<span style="color: {color};">[{timestamp:06d}] {message}</span>'
        self.log_output.append(formatted_message)
        self.log_output.ensureCursorVisible()
    
    def get_log_color(self, log_type):
        """Get color for log message type"""
        colors = {
            "info": ProfessionalTheme.TEXT_SECONDARY,
            "success": ProfessionalTheme.SUCCESS,
            "warning": ProfessionalTheme.WARNING,
            "error": ProfessionalTheme.DANGER,
            "system": ProfessionalTheme.DANGER
        }
        return colors.get(log_type, ProfessionalTheme.TEXT_SECONDARY)
    
    def simulate_progress(self, duration=3000):
        """Simulate progress bar animation"""
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        
        # Animate progress bar
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.update_progress)
        self.progress_timer.start(50)  # Update every 50ms
        
        # Stop after duration
        QTimer.singleShot(duration, self.stop_progress)
    
    def update_progress(self):
        """Update progress bar"""
        current_value = self.progress_bar.value()
        if current_value < 100:
            self.progress_bar.setValue(current_value + 2)
    
    def stop_progress(self):
        """Stop progress animation"""
        if hasattr(self, 'progress_timer'):
            self.progress_timer.stop()
        self.progress_bar.setValue(100)
