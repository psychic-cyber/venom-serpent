"""
Payload Delivery Step Window
Step 3: Payload delivery simulation
"""

from PyQt5.QtWidgets import (QHBoxLayout, QLineEdit, QPushButton, QSplitter, 
                            QTextEdit, QFrame, QVBoxLayout, QLabel, QWidget, QProgressBar)
from PyQt5.QtCore import Qt, QTimer
from utils.step_window import BaseStepWindow
from utils.professional_theme import ProfessionalTheme

class PayloadWindow(BaseStepWindow):
    """Payload delivery step window"""
    
    def __init__(self, parent=None):
        super().__init__("payload", "Payload Delivery", parent)
    
    def execute_step(self):
        """Execute payload delivery step"""
        super().execute_step()
        self.log_output.clear()
        self.simulate_payload_delivery()
    
    def simulate_payload_delivery(self):
        """Simulate payload delivery activities"""
        target = self.target_info.get('target', '127.0.0.1') if self.target_info else '127.0.0.1'
        
        self.simulate_progress(4000)
        
        self.add_log("🚀 Starting payload delivery phase...", "system")
        self.add_log(f"🎯 Target: {target}:4444", "info")
        self.add_log("📡 Deploying payload to target system...", "info")
        
        QTimer.singleShot(1000, lambda: self.add_log("✅ Payload deployed successfully", "success"))
        QTimer.singleShot(2000, lambda: self.add_log("📡 Establishing reverse shell connection...", "info"))
        QTimer.singleShot(3000, lambda: self.add_log("✅ Reverse shell established on port 4444", "success"))
        QTimer.singleShot(4000, lambda: self.add_log("💻 Executing payload commands...", "info"))
        QTimer.singleShot(5000, lambda: self.add_log("✅ System access gained", "success"))
        QTimer.singleShot(6000, lambda: self.add_log("✅ Command execution successful", "success"))
        QTimer.singleShot(7000, lambda: self.complete_payload_delivery())
    
    def complete_payload_delivery(self):
        """Complete payload delivery step"""
        self.add_log("", "info")
        self.add_log("🎉 Payload delivery phase completed successfully!", "success")
        self.add_log("🔒 System access established and maintained", "success")
        self.add_log("📊 Ready for persistence phase...", "info")
        
        # Complete the step using parent class method
        self.step_completed.emit(self.step_id)
        self.execute_btn.setEnabled(False)
        self.next_btn.setEnabled(True)
        self.status_label.setText("Completed")
        self.status_label.setStyleSheet(ProfessionalTheme.get_label_style("success"))