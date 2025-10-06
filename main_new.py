#!/usr/bin/env python3
"""
Venom Serpent - Professional Dark Cyberpunk GUI
Author: Psychic Cyber
Tagline: "Hold My Venom 🐍"

A professional offensive cybersecurity simulation tool with step-wise windows.
"""

import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QPushButton, QTextEdit, QLabel, 
                            QProgressBar, QStatusBar, QSplitter, QFrame,
                            QSplashScreen, QMessageBox, QFileDialog, QDialog,
                            QLineEdit, QFormLayout, QDialogButtonBox, QGroupBox,
                            QTabWidget, QListWidget, QListWidgetItem)
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QPixmap, QFont, QPalette, QColor, QPainter, QPen, QIcon
import time
import json
from datetime import datetime

# Import our utilities and windows
from utils.professional_theme import ProfessionalTheme
from utils.splash_screen import VenomSplashScreen
from utils.timeline_tracker import AttackTimelineTracker
from utils.simple_report_gen import SimpleReportGenerator
from windows.recon_window import ReconWindow
from windows.exploit_window import ExploitWindow
from windows.payload_window import PayloadWindow
from windows.persistence_window import PersistenceWindow
from windows.cleanup_window import CleanupWindow

class TargetInputDialog(QDialog):
    """Professional target configuration dialog"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Venom Serpent - Target Configuration")
        self.setFixedSize(500, 400)
        # Set window icon (use a smaller version to avoid size issues)
        try:
            icon_pixmap = QPixmap("assets/logo1.png")
            if not icon_pixmap.isNull():
                scaled_icon = icon_pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.setWindowIcon(QIcon(scaled_icon))
        except:
            pass
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Header with logo
        header_layout = QHBoxLayout()
        logo_label = QLabel()
        logo_pixmap = QPixmap("assets/logo1.png")
        if not logo_pixmap.isNull():
            scaled_pixmap = logo_pixmap.scaled(60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            logo_label.setPixmap(scaled_pixmap)
        else:
            logo_label.setText("🐍")
            logo_label.setStyleSheet(ProfessionalTheme.get_label_style("title"))
        header_layout.addWidget(logo_label)
        
        title_layout = QVBoxLayout()
        title_label = QLabel("🎯 Configure Attack Target")
        title_label.setStyleSheet(ProfessionalTheme.get_label_style("title"))
        title_layout.addWidget(title_label)
        
        subtitle_label = QLabel("Venom Serpent - Hold My Venom 🐍")
        subtitle_label.setStyleSheet(ProfessionalTheme.get_label_style("normal"))
        title_layout.addWidget(subtitle_label)
        
        header_layout.addLayout(title_layout)
        header_layout.addStretch()
        layout.addLayout(header_layout)
        
        # Form
        form_layout = QFormLayout()
        
        # Target input
        self.target_input = QLineEdit()
        self.target_input.setPlaceholderText("Enter target (e.g., example.com, 192.168.1.1)")
        self.target_input.setText("127.0.0.1")
        self.target_input.setStyleSheet(ProfessionalTheme.get_input_style())
        form_layout.addRow("Target:", self.target_input)
        
        # Port input
        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("Enter port range (e.g., 1-1000)")
        self.port_input.setText("1-1000")
        self.port_input.setStyleSheet(ProfessionalTheme.get_input_style())
        form_layout.addRow("Port Range:", self.port_input)
        
        # Attack type
        self.attack_type = QLineEdit()
        self.attack_type.setPlaceholderText("Enter attack type (e.g., Web App, Network)")
        self.attack_type.setText("Web Application")
        self.attack_type.setStyleSheet(ProfessionalTheme.get_input_style())
        form_layout.addRow("Attack Type:", self.attack_type)
        
        layout.addLayout(form_layout)
        
        # Info text
        info_text = QLabel("⚠️ This is a simulation tool. No real attacks will be performed.")
        info_text.setStyleSheet(ProfessionalTheme.get_label_style("warning"))
        info_text.setWordWrap(True)
        layout.addWidget(info_text)
        
        # Buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        buttons.setStyleSheet(ProfessionalTheme.get_button_style("primary"))
        layout.addWidget(buttons)
        
        self.setLayout(layout)
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {ProfessionalTheme.BACKGROUND_PRIMARY};
                color: {ProfessionalTheme.TEXT_PRIMARY};
            }}
        """)
    
    def get_target_info(self):
        return {
            'target': self.target_input.text().strip(),
            'port_range': self.port_input.text().strip(),
            'attack_type': self.attack_type.text().strip()
        }

class VenomSerpentMainWindow(QMainWindow):
    """Main window for Venom Serpent"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Venom Serpent – Hold My Venom 🐍")
        
        # Get screen dimensions for responsive design
        screen = QApplication.desktop().screenGeometry()
        screen_width = screen.width()
        screen_height = screen.height()
        
        # Set window size based on screen size (responsive)
        if screen_width >= 1920:  # Large screens
            self.setGeometry(100, 100, 1600, 1000)
        elif screen_width >= 1366:  # Medium screens
            self.setGeometry(50, 50, 1200, 800)
        else:  # Small screens
            self.setGeometry(20, 20, 1000, 700)
        
        # Set minimum size for usability
        self.setMinimumSize(800, 600)
        
        # Set window icon (use a smaller version to avoid size issues)
        try:
            icon_pixmap = QPixmap("assets/logo1.png")
            if not icon_pixmap.isNull():
                # Scale down the icon to avoid size issues
                scaled_icon = icon_pixmap.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.setWindowIcon(QIcon(scaled_icon))
        except:
            # If logo loading fails, continue without icon
            pass
        
        # Target information
        self.target_info = {
            'target': '127.0.0.1',
            'port_range': '1-1000',
            'attack_type': 'Web Application'
        }
        
        # Attack step windows
        self.step_windows = {}
        self.current_step = 0
        
        # Attack timeline
        self.attack_timeline = []
        
        self.init_ui()
        self.apply_theme()
    
    def init_ui(self):
        """Initialize the user interface"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout - Professional spacing
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(15, 15, 15, 15)
        
        # Create splitter for resizable panels
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)
        
        # Left panel - Timeline and controls
        left_panel = self.create_left_panel()
        splitter.addWidget(left_panel)
        
        # Right panel - Main content
        right_panel = self.create_right_panel()
        splitter.addWidget(right_panel)
        
        # Set responsive splitter proportions based on screen size
        screen_width = QApplication.desktop().screenGeometry().width()
        if screen_width >= 1920:  # Large screens
            splitter.setSizes([400, 1200])
        elif screen_width >= 1366:  # Medium screens
            splitter.setSizes([300, 900])
        else:  # Small screens
            splitter.setSizes([250, 750])
        
        # Enable collapsible panels
        splitter.setChildrenCollapsible(False)
        
        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready - Simulation Mode Active")
        self.status_bar.setStyleSheet(f"""
            QStatusBar {{
                background-color: {ProfessionalTheme.BACKGROUND_SECONDARY};
                color: {ProfessionalTheme.TEXT_PRIMARY};
                border-top: 2px solid {ProfessionalTheme.DANGER};
            }}
        """)
    
    def create_left_panel(self):
        """Create the left panel with timeline and controls - no boxes"""
        panel = QWidget()
        panel.setStyleSheet(ProfessionalTheme.get_panel_style())
        
        layout = QVBoxLayout(panel)
        layout.setSpacing(8)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # Header with logo
        header_layout = QHBoxLayout()
        
        logo_label = QLabel()
        logo_pixmap = QPixmap("assets/logo1.png")
        if not logo_pixmap.isNull():
            scaled_pixmap = logo_pixmap.scaled(60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            logo_label.setPixmap(scaled_pixmap)
        else:
            logo_label.setText("🐍")
            logo_label.setStyleSheet(ProfessionalTheme.get_label_style("title"))
        header_layout.addWidget(logo_label)
        
        title_layout = QVBoxLayout()
        title_label = QLabel("VENOM SERPENT")
        title_label.setStyleSheet(ProfessionalTheme.get_label_style("title"))
        title_layout.addWidget(title_label)
        
        tagline_label = QLabel("Hold My Venom 🐍")
        tagline_label.setStyleSheet(ProfessionalTheme.get_label_style("normal"))
        title_layout.addWidget(tagline_label)
        
        header_layout.addLayout(title_layout)
        header_layout.addStretch()
        layout.addLayout(header_layout)
        
        # Target Information (consolidated)
        target_info_text = f"Target: {self.target_info['target']} | Ports: {self.target_info['port_range']} | Type: {self.target_info['attack_type']}"
        self.target_label = QLabel(target_info_text)
        self.target_label.setStyleSheet(ProfessionalTheme.get_label_style("normal"))
        self.target_label.setWordWrap(True)
        layout.addWidget(self.target_label)
        
        # Attack Timeline (no group box)
        timeline_label = QLabel("Attack Timeline")
        timeline_label.setStyleSheet(ProfessionalTheme.get_label_style("header"))
        layout.addWidget(timeline_label)
        
        self.timeline_tracker = AttackTimelineTracker()
        self.timeline_tracker.step_completed.connect(self.on_step_completed)
        layout.addWidget(self.timeline_tracker)
        
        # Control buttons (consolidated)
        control_layout = QVBoxLayout()
        
        # Configure target button
        self.config_btn = QPushButton("⚙️ CONFIGURE TARGET")
        self.config_btn.setStyleSheet(ProfessionalTheme.get_button_style("secondary"))
        self.config_btn.clicked.connect(self.configure_target)
        control_layout.addWidget(self.config_btn)
        
        # Start attack button
        self.start_btn = QPushButton("🚀 START ATTACK")
        self.start_btn.setStyleSheet(ProfessionalTheme.get_button_style("primary"))
        self.start_btn.clicked.connect(self.start_attack)
        control_layout.addWidget(self.start_btn)
        
        # Export report button
        self.export_btn = QPushButton("📊 EXPORT REPORT")
        self.export_btn.setStyleSheet(ProfessionalTheme.get_button_style("warning"))
        self.export_btn.clicked.connect(self.export_report)
        control_layout.addWidget(self.export_btn)
        
        # Reset button
        self.reset_btn = QPushButton("🔄 RESET ATTACK")
        self.reset_btn.setStyleSheet(ProfessionalTheme.get_button_style("secondary"))
        self.reset_btn.clicked.connect(self.reset_attack)
        control_layout.addWidget(self.reset_btn)
        
        layout.addLayout(control_layout)
        
        layout.addStretch()
        return panel
    
    def create_right_panel(self):
        """Create the right panel with main content - no boxes"""
        panel = QWidget()
        panel.setStyleSheet(ProfessionalTheme.get_panel_style())
        
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # Attack steps tab widget
        self.steps_tab = QTabWidget()
        self.steps_tab.setStyleSheet(ProfessionalTheme.get_tab_widget_style())
        
        # Create step windows
        self.create_step_windows()
        
        layout.addWidget(self.steps_tab)
        
        return panel
    
    def create_step_windows(self):
        """Create all attack step windows"""
        # Step 1: Reconnaissance
        self.step_windows['recon'] = ReconWindow()
        self.step_windows['recon'].step_completed.connect(self.on_step_completed)
        self.step_windows['recon'].next_step_requested.connect(self.next_step)
        self.steps_tab.addTab(self.step_windows['recon'], "1. Reconnaissance")
        
        # Step 2: Exploitation
        self.step_windows['exploit'] = ExploitWindow()
        self.step_windows['exploit'].step_completed.connect(self.on_step_completed)
        self.step_windows['exploit'].next_step_requested.connect(self.next_step)
        self.steps_tab.addTab(self.step_windows['exploit'], "2. Exploitation")
        
        # Step 3: Payload Delivery
        self.step_windows['payload'] = PayloadWindow()
        self.step_windows['payload'].step_completed.connect(self.on_step_completed)
        self.step_windows['payload'].next_step_requested.connect(self.next_step)
        self.steps_tab.addTab(self.step_windows['payload'], "3. Payload Delivery")
        
        # Step 4: Persistence
        self.step_windows['persistence'] = PersistenceWindow()
        self.step_windows['persistence'].step_completed.connect(self.on_step_completed)
        self.step_windows['persistence'].next_step_requested.connect(self.next_step)
        self.steps_tab.addTab(self.step_windows['persistence'], "4. Persistence")
        
        # Step 5: Cleanup
        self.step_windows['cleanup'] = CleanupWindow()
        self.step_windows['cleanup'].step_completed.connect(self.on_step_completed)
        self.step_windows['cleanup'].next_step_requested.connect(self.next_step)
        self.steps_tab.addTab(self.step_windows['cleanup'], "5. Cover Tracks")
        
        # Initially disable all tabs except the first
        for i in range(1, self.steps_tab.count()):
            self.steps_tab.setTabEnabled(i, False)
    
    def apply_theme(self):
        """Apply the professional theme"""
        self.setStyleSheet(ProfessionalTheme.get_main_window_style())
    
    def configure_target(self):
        """Open target configuration dialog"""
        dialog = TargetInputDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.target_info = dialog.get_target_info()
            
            # Update consolidated target display
            target_info_text = f"Target: {self.target_info['target']} | Ports: {self.target_info['port_range']} | Type: {self.target_info['attack_type']}"
            self.target_label.setText(target_info_text)
            
            # Update all step windows
            for window in self.step_windows.values():
                window.set_target_info(self.target_info)
    
    def start_attack(self):
        """Start the attack simulation"""
        self.start_btn.setEnabled(False)
        self.start_btn.setText("ATTACK IN PROGRESS...")
        self.start_btn.setStyleSheet(ProfessionalTheme.get_button_style("warning"))
        
        # Enable first step
        self.steps_tab.setTabEnabled(0, True)
        self.steps_tab.setCurrentIndex(0)
        
        # Update timeline
        self.timeline_tracker.update_step_status("recon", "in_progress")
        
        self.status_bar.showMessage("Attack started - Ready for Step 1: Reconnaissance")
    
    def on_step_completed(self, step_id):
        """Handle step completion"""
        # Update timeline tracker
        self.timeline_tracker.update_step_status(step_id, "completed")
        
        # Record in timeline
        step_window = self.step_windows[step_id]
        self.attack_timeline.append({
            'step': step_id,
            'timestamp': datetime.now().isoformat(),
            'target': self.target_info['target'],
            'logs': step_window.log_output.toPlainText().split('\n')
        })
        
        # Enable next step
        step_order = ['recon', 'exploit', 'payload', 'persistence', 'cleanup']
        current_index = step_order.index(step_id)
        
        if current_index < len(step_order) - 1:
            next_step = step_order[current_index + 1]
            self.steps_tab.setTabEnabled(current_index + 1, True)
            self.steps_tab.setCurrentIndex(current_index + 1)
            self.timeline_tracker.update_step_status(next_step, "in_progress")
        else:
            # All steps completed
            self.status_bar.showMessage("All attack steps completed - Ready for report export")
            self.auto_generate_report()
    
    def next_step(self):
        """Move to next step"""
        current_index = self.steps_tab.currentIndex()
        if current_index < self.steps_tab.count() - 1:
            self.steps_tab.setCurrentIndex(current_index + 1)
    
    def reset_attack(self):
        """Reset the attack simulation"""
        # Reset timeline
        self.timeline_tracker.reset_timeline()
        
        # Reset step windows
        for window in self.step_windows.values():
            window.is_completed = False
            window.log_output.clear()
            window.status_label.setText("Ready")
            window.status_label.setStyleSheet(ProfessionalTheme.get_label_style("normal"))
            window.execute_btn.setEnabled(True)
            window.execute_btn.setText("Execute Step")
            window.next_btn.setEnabled(False)
        
        # Disable all tabs except first
        for i in range(1, self.steps_tab.count()):
            self.steps_tab.setTabEnabled(i, False)
        self.steps_tab.setCurrentIndex(0)
        
        # Reset buttons
        self.start_btn.setEnabled(True)
        self.start_btn.setText("🚀 START ATTACK")
        self.start_btn.setStyleSheet(ProfessionalTheme.get_button_style("primary"))
        
        # Clear timeline
        self.attack_timeline = []
        
        self.status_bar.showMessage("Attack reset - Ready to start")
    
    def auto_generate_report(self):
        """Automatically generate PDF report after all steps are completed"""
        try:
            # Create reports directory if it doesn't exist
            os.makedirs("reports", exist_ok=True)
            
            # Generate meaningful filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            target_name = self.target_info['target'].replace('.', '_').replace(':', '_')
            filename = f"venom_serpent_attack_{target_name}_{timestamp}.pdf"
            file_path = os.path.join("reports", filename)
            
            # Generate PDF report
            generator = SimpleReportGenerator()
            generator.export_pdf(self.attack_timeline, self.target_info, file_path)
            
            # Show success message
            QMessageBox.information(
                self, 
                "Report Generated", 
                f"Attack report has been automatically generated and saved to:\n{file_path}"
            )
            
            self.status_bar.showMessage(f"Report generated: {filename}")
            
        except Exception as e:
            QMessageBox.critical(self, "Report Error", f"Failed to generate report:\n{str(e)}")
    
    def export_report(self):
        """Export attack timeline report"""
        if not self.attack_timeline:
            QMessageBox.warning(self, "No Data", "No attack data to export. Run attack first.")
            return
        
        # Get save location
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Export Attack Report", 
            f"venom_serpent_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html",
            "HTML Files (*.html);;PDF Files (*.pdf)"
        )
        
        if file_path:
            try:
                generator = SimpleReportGenerator()
                if file_path.endswith('.pdf'):
                    generator.export_pdf(self.attack_timeline, self.target_info, file_path)
                else:
                    generator.export_html(self.attack_timeline, self.target_info, file_path)
                
                QMessageBox.information(self, "Success", f"Report exported to: {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to export report: {str(e)}")

def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    
    # Show splash screen
    splash = VenomSplashScreen()
    splash.show()
    app.processEvents()
    
    # Simulate loading time
    QTimer.singleShot(3000, splash.close)
    
    # Create and show main window
    window = VenomSerpentMainWindow()
    QTimer.singleShot(3000, window.show)
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
