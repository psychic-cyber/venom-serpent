#!/usr/bin/env python3
"""
Final Enhanced Venom Serpent Demo
Demonstrates the professional dark cyberpunk GUI with step-wise windows
"""

import sys
import time
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

# Import our enhanced application
from main_new import VenomSerpentMainWindow

class EnhancedDemoRunner:
    def __init__(self, gui):
        self.gui = gui
        self.step = 0
        self.steps = ['recon', 'exploit', 'payload', 'persistence', 'cleanup']
        
    def run_demo(self):
        """Run enhanced demo with professional features"""
        print("🐍 Starting Venom Serpent Professional Edition Demo...")
        print("   Hold My Venom 🐍")
        print("   Author: Psychic Cyber")
        print("=" * 50)
        print("⏱️  Demo will showcase professional features:")
        print("   • Dark cyberpunk theme")
        print("   • Step-wise attack windows")
        print("   • Timeline tracker")
        print("   • Interactive terminal")
        print("   • Auto report generation")
        print("🛑 Press Ctrl+C to stop the demo\n")
        
        # Configure target first
        self.gui.target_info = {
            'target': 'example.com',
            'port_range': '1-1000',
            'attack_type': 'Web Application'
        }
        
        # Update target display
        self.gui.target_label.setText(f"Target: {self.gui.target_info['target']}")
        self.gui.port_label.setText(f"Ports: {self.gui.target_info['port_range']}")
        self.gui.type_label.setText(f"Type: {self.gui.target_info['attack_type']}")
        
        print(f"🎯 Target configured: {self.gui.target_info['target']}")
        
        # Start attack
        self.gui.start_attack()
        
        # Set up timer for automated execution
        self.timer = QTimer()
        self.timer.timeout.connect(self.execute_next_step)
        self.timer.start(5000)  # 5 seconds between steps
    
    def execute_next_step(self):
        """Execute next attack step"""
        if self.step < len(self.steps):
            step_id = self.steps[self.step]
            step_names = {
                'recon': 'Reconnaissance',
                'exploit': 'Exploitation',
                'payload': 'Payload Delivery',
                'persistence': 'Persistence',
                'cleanup': 'Cover Tracks'
            }
            print(f"🎯 Executing Step {self.step + 1}: {step_names[step_id]}")
            
            # Get the step window and execute
            step_window = self.gui.step_windows[step_id]
            step_window.set_target_info(self.gui.target_info)
            step_window.execute_step()
            
            self.step += 1
        else:
            print("\n✅ Enhanced demo completed! All attack phases executed.")
            print("📊 Professional features demonstrated:")
            print("   • Dark cyberpunk theme applied")
            print("   • Step-wise windows functional")
            print("   • Timeline tracker updated")
            print("   • Interactive terminal simulated")
            print("   • PDF report should be auto-generated")
            print("🎯 Professional Venom Serpent is ready for use!")
            self.timer.stop()

def main():
    """Main demo function"""
    app = QApplication(sys.argv)
    
    # Create enhanced GUI
    gui = VenomSerpentMainWindow()
    gui.show()
    
    # Create and run enhanced demo
    demo = EnhancedDemoRunner(gui)
    
    # Start demo after a short delay
    QTimer.singleShot(2000, demo.run_demo)
    
    # Run application
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
