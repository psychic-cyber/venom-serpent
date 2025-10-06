"""
Attack Timeline Tracker for Venom Serpent
Tracks progress of all attack phases with visual indicators
"""

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                            QListWidget, QListWidgetItem, QFrame)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QColor, QIcon
from utils.professional_theme import ProfessionalTheme

class AttackTimelineTracker(QWidget):
    """Timeline tracker widget for attack phases"""
    
    step_completed = pyqtSignal(str)  # Emitted when a step is completed
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.steps = [
            {"id": "recon", "name": "Reconnaissance", "status": "pending"},
            {"id": "exploit", "name": "Exploitation", "status": "pending"},
            {"id": "payload", "name": "Payload Delivery", "status": "pending"},
            {"id": "persistence", "name": "Persistence", "status": "pending"},
            {"id": "cleanup", "name": "Cover Tracks", "status": "pending"}
        ]
        self.init_ui()
    
    def init_ui(self):
        """Initialize the timeline UI"""
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        # Header
        header = QLabel("ATTACK TIMELINE")
        header.setStyleSheet(ProfessionalTheme.get_label_style("header"))
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Timeline list
        self.timeline_list = QListWidget()
        self.timeline_list.setStyleSheet(ProfessionalTheme.get_timeline_style())
        self.timeline_list.setMaximumHeight(300)
        layout.addWidget(self.timeline_list)
        
        # Populate timeline
        self.populate_timeline()
        
        # Status summary
        self.status_frame = QFrame()
        self.status_frame.setStyleSheet(ProfessionalTheme.get_panel_style())
        status_layout = QVBoxLayout()
        
        self.status_label = QLabel("Status: Ready to Begin")
        self.status_label.setStyleSheet(ProfessionalTheme.get_label_style("normal"))
        self.status_label.setAlignment(Qt.AlignCenter)
        status_layout.addWidget(self.status_label)
        
        self.progress_label = QLabel("Progress: 0/5 Steps")
        self.progress_label.setStyleSheet(ProfessionalTheme.get_label_style("normal"))
        self.progress_label.setAlignment(Qt.AlignCenter)
        status_layout.addWidget(self.progress_label)
        
        self.status_frame.setLayout(status_layout)
        layout.addWidget(self.status_frame)
        
        self.setLayout(layout)
        self.setStyleSheet(ProfessionalTheme.get_panel_style())
    
    def populate_timeline(self):
        """Populate the timeline with attack steps"""
        self.timeline_list.clear()
        
        for i, step in enumerate(self.steps):
            item = QListWidgetItem()
            
            # Create step text with status indicator
            status_icon = self.get_status_icon(step["status"])
            step_text = f"{status_icon} {step['name']}"
            
            item.setText(step_text)
            item.setData(Qt.UserRole, step["id"])
            
            # Set item styling based on status
            if step["status"] == "completed":
                item.setBackground(QColor(ProfessionalTheme.SUCCESS + "20"))
                item.setForeground(QColor(ProfessionalTheme.SUCCESS))
            elif step["status"] == "failed":
                item.setBackground(QColor(ProfessionalTheme.DANGER + "20"))
                item.setForeground(QColor(ProfessionalTheme.DANGER))
            elif step["status"] == "in_progress":
                item.setBackground(QColor(ProfessionalTheme.WARNING + "20"))
                item.setForeground(QColor(ProfessionalTheme.WARNING))
            else:  # pending
                item.setBackground(QColor(ProfessionalTheme.BACKGROUND_TERTIARY + "20"))
                item.setForeground(QColor(ProfessionalTheme.TEXT_SECONDARY))
            
            self.timeline_list.addItem(item)
    
    def get_status_icon(self, status):
        """Get status icon for timeline"""
        icons = {
            "completed": "✓",
            "failed": "✗",
            "in_progress": "▶",
            "pending": "○"
        }
        return icons.get(status, "○")
    
    def update_step_status(self, step_id, status):
        """Update the status of a specific step"""
        for step in self.steps:
            if step["id"] == step_id:
                step["status"] = status
                break
        
        self.populate_timeline()
        self.update_status_summary()
    
    def update_status_summary(self):
        """Update the status summary"""
        completed = sum(1 for step in self.steps if step["status"] == "completed")
        failed = sum(1 for step in self.steps if step["status"] == "failed")
        in_progress = sum(1 for step in self.steps if step["status"] == "in_progress")
        
        if completed == len(self.steps):
            self.status_label.setText("Status: All Steps Completed!")
            self.status_label.setStyleSheet(ProfessionalTheme.get_label_style("success"))
        elif failed > 0:
            self.status_label.setText(f"Status: {failed} Step(s) Failed")
            self.status_label.setStyleSheet(ProfessionalTheme.get_label_style("error"))
        elif in_progress > 0:
            self.status_label.setText("Status: Attack in Progress")
            self.status_label.setStyleSheet(ProfessionalTheme.get_label_style("warning"))
        else:
            self.status_label.setText("Status: Ready to Begin")
            self.status_label.setStyleSheet(ProfessionalTheme.get_label_style("normal"))
        
        self.progress_label.setText(f"Progress: {completed}/{len(self.steps)} Steps")
    
    def reset_timeline(self):
        """Reset the timeline to initial state"""
        for step in self.steps:
            step["status"] = "pending"
        
        self.populate_timeline()
        self.update_status_summary()
    
    def get_completed_steps(self):
        """Get list of completed steps"""
        return [step["id"] for step in self.steps if step["status"] == "completed"]
    
    def get_failed_steps(self):
        """Get list of failed steps"""
        return [step["id"] for step in self.steps if step["status"] == "failed"]
    
    def is_attack_complete(self):
        """Check if all steps are completed"""
        return all(step["status"] == "completed" for step in self.steps)
    
    def get_next_pending_step(self):
        """Get the next pending step"""
        for step in self.steps:
            if step["status"] == "pending":
                return step["id"]
        return None
