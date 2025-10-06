"""
Cleanup Step Window
Step 5: Cover tracks and clean up evidence
"""

from PyQt5.QtCore import QTimer
from utils.step_window import BaseStepWindow

class CleanupWindow(BaseStepWindow):
    """Cleanup step window"""
    
    def __init__(self, parent=None):
        super().__init__("cleanup", "Cover Tracks", parent)
        self.setWindowTitle("Venom Serpent - Cover Tracks")
        self.setFixedSize(1000, 700)
    
    def execute_step(self):
        """Execute cleanup step"""
        super().execute_step()
        self.log_output.clear()
        self.simulate_cleanup()
    
    def simulate_cleanup(self):
        """Simulate cleanup activities"""
        target = self.target_info.get('target', '127.0.0.1') if self.target_info else '127.0.0.1'
        
        self.simulate_progress(8000)
        
        self.add_log("🧹 Starting cleanup phase...", "system")
        self.add_log(f"🎯 Target: {target} (Compromised system)", "info")
        self.add_log("📡 Removing forensic evidence...", "info")
        
        QTimer.singleShot(1000, self.simulate_log_cleaning)
        QTimer.singleShot(2000, self.simulate_command_history_cleaning)
        QTimer.singleShot(3000, self.simulate_temp_file_cleanup)
        QTimer.singleShot(4000, self.simulate_process_hiding)
        QTimer.singleShot(5000, self.simulate_timestamp_modification)
        QTimer.singleShot(6000, self.simulate_network_cleanup)
        QTimer.singleShot(7000, self.complete_cleanup)
    
    def simulate_log_cleaning(self):
        """Simulate log file cleaning"""
        self.add_log("", "info")
        self.add_log("📝 Cleaning system logs...", "system")
        self.add_log("Clearing authentication logs...", "info")
        self.add_log("$ > /var/log/auth.log", "warning")
        self.add_log("$ > /var/log/secure", "warning")
        self.add_log("$ > /var/log/wtmp", "warning")
        self.add_log("$ > /var/log/utmp", "warning")
        self.add_log("Response: Authentication logs cleared!", "success")
        
        self.add_log("", "info")
        self.add_log("Clearing web server logs...", "info")
        self.add_log("$ > /var/log/apache2/access.log", "warning")
        self.add_log("$ > /var/log/apache2/error.log", "warning")
        self.add_log("$ > /var/log/nginx/access.log", "warning")
        self.add_log("$ > /var/log/nginx/error.log", "warning")
        self.add_log("Response: Web server logs cleared!", "success")
        
        self.add_log("", "info")
        self.add_log("Clearing system logs...", "info")
        self.add_log("$ > /var/log/syslog", "warning")
        self.add_log("$ > /var/log/messages", "warning")
        self.add_log("$ > /var/log/kern.log", "warning")
        self.add_log("$ > /var/log/dpkg.log", "warning")
        self.add_log("Response: System logs cleared!", "success")
    
    def simulate_command_history_cleaning(self):
        """Simulate command history cleaning"""
        self.add_log("", "info")
        self.add_log("💻 Cleaning command history...", "system")
        self.add_log("$ history -c", "warning")
        self.add_log("$ > ~/.bash_history", "warning")
        self.add_log("$ > ~/.zsh_history", "warning")
        self.add_log("$ > ~/.fish_history", "warning")
        self.add_log("Response: Command history cleared!", "success")
    
    def simulate_temp_file_cleanup(self):
        """Simulate temporary file cleanup"""
        self.add_log("", "info")
        self.add_log("🗑️  Cleaning temporary files...", "system")
        self.add_log("$ rm -rf /tmp/*", "warning")
        self.add_log("$ rm -rf /var/tmp/*", "warning")
        self.add_log("$ rm -rf /tmp/.*", "warning")
        self.add_log("$ rm -rf /var/tmp/.*", "warning")
        self.add_log("Response: Temporary files cleaned!", "success")
    
    def simulate_process_hiding(self):
        """Simulate process hiding"""
        self.add_log("", "info")
        self.add_log("👻 Hiding malicious processes...", "system")
        self.add_log("Renaming processes...", "info")
        self.add_log("$ ps aux | grep venom", "info")
        self.add_log("$ kill -STOP $(pgrep venom)", "warning")
        self.add_log("$ mv /usr/bin/venom /usr/bin/systemd-resolved", "warning")
        self.add_log("Response: Processes hidden!", "success")
    
    def simulate_timestamp_modification(self):
        """Simulate file timestamp modification"""
        self.add_log("", "info")
        self.add_log("⏰ Modifying file timestamps...", "system")
        self.add_log("$ touch -t 202401010000 /var/tmp/.hidden/keylogger.sh", "warning")
        self.add_log("$ touch -t 202401010000 /etc/systemd/system/venom.service", "warning")
        self.add_log("$ touch -t 202401010000 /home/user/.ssh/authorized_keys", "warning")
        self.add_log("Response: File timestamps modified!", "success")
    
    def simulate_network_cleanup(self):
        """Simulate network connection cleanup"""
        self.add_log("", "info")
        self.add_log("🌐 Cleaning network traces...", "system")
        self.add_log("$ iptables -F", "warning")
        self.add_log("$ iptables -X", "warning")
        self.add_log("$ iptables -t nat -F", "warning")
        self.add_log("$ iptables -t nat -X", "warning")
        self.add_log("$ iptables -t mangle -F", "warning")
        self.add_log("$ iptables -t mangle -X", "warning")
        self.add_log("Response: Network traces cleaned!", "success")
    
    def complete_cleanup(self):
        """Complete cleanup step"""
        self.add_log("", "info")
        self.add_log("⚙️  Cleaning configuration files...", "system")
        self.add_log("Removing cron job traces...", "info")
        self.add_log("$ crontab -l | grep -v venom | crontab -", "warning")
        self.add_log("Response: Cron job traces removed!", "success")
        
        self.add_log("", "info")
        self.add_log("Cleaning systemd traces...", "info")
        self.add_log("$ systemctl disable venom.service", "warning")
        self.add_log("$ systemctl stop venom.service", "warning")
        self.add_log("$ rm -f /etc/systemd/system/venom.service", "warning")
        self.add_log("$ systemctl daemon-reload", "info")
        self.add_log("Response: Systemd traces cleaned!", "success")
        
        self.add_log("", "info")
        self.add_log("🔐 Modifying file permissions...", "system")
        self.add_log("$ chmod 600 /home/user/.ssh/authorized_keys", "info")
        self.add_log("$ chmod 700 /var/tmp/.hidden", "info")
        self.add_log("$ chmod 755 /var/tmp/.hidden/keylogger.sh", "info")
        self.add_log("Response: File permissions modified!", "success")
        
        self.add_log("", "info")
        self.add_log("🕵️  Applying anti-forensics techniques...", "system")
        self.add_log("Overwriting deleted files...", "info")
        self.add_log("$ shred -vfz -n 3 /tmp/deleted_files/*", "warning")
        self.add_log("$ dd if=/dev/zero of=/tmp/free_space bs=1M", "warning")
        self.add_log("$ rm -f /tmp/free_space", "info")
        self.add_log("Response: Anti-forensics techniques applied!", "success")
        
        self.add_log("", "info")
        self.add_log("🧠 Cleaning memory traces...", "system")
        self.add_log("$ sync", "info")
        self.add_log("$ echo 3 > /proc/sys/vm/drop_caches", "warning")
        self.add_log("$ swapoff -a && swapon -a", "warning")
        self.add_log("Response: Memory traces cleaned!", "success")
        
        self.add_log("", "info")
        self.add_log("✅ Verifying cleanup completion...", "system")
        self.add_log("Checking log files...", "info")
        self.add_log("$ ls -la /var/log/ | grep -E '\\.log$' | wc -l", "info")
        self.add_log("0", "success")
        self.add_log("Response: All log files cleared!", "success")
        
        self.add_log("", "info")
        self.add_log("Checking process list...", "info")
        self.add_log("$ ps aux | grep -i venom", "info")
        self.add_log("(no results)", "success")
        self.add_log("Response: No malicious processes found!", "success")
        
        self.add_log("", "info")
        self.add_log("Checking network connections...", "info")
        self.add_log("$ netstat -tulpn | grep 4444", "info")
        self.add_log("(no results)", "success")
        self.add_log("Response: No suspicious network connections!", "success")
        
        self.add_log("", "info")
        self.add_log("📊 Cleanup Summary Report", "system")
        self.add_log("┌─────────────────────────────────────────┐", "info")
        self.add_log("│            CLEANUP COMPLETED            │", "info")
        self.add_log("└─────────────────────────────────────────┘", "info")
        self.add_log("✅ System logs cleared", "success")
        self.add_log("✅ Command history cleared", "success")
        self.add_log("✅ Temporary files removed", "success")
        self.add_log("✅ Process traces hidden", "success")
        self.add_log("✅ File timestamps modified", "success")
        self.add_log("✅ Network traces cleaned", "success")
        self.add_log("✅ Configuration files cleaned", "success")
        self.add_log("✅ Anti-forensics techniques applied", "success")
        self.add_log("✅ Memory traces cleaned", "success")
        self.add_log("──────────────────────────────────────────", "info")
        self.add_log("🎯 Footprints Removed Successfully ✅", "success")
        
        self.add_log("", "info")
        self.add_log("✅ Cleanup phase completed!", "success")
        self.add_log("📊 Summary: All forensic evidence removed", "info")
        self.add_log("🎯 Status: Attack traces successfully covered", "success")
        self.add_log("🔒 Persistence: Backdoors remain active", "warning")
        self.add_log("🕵️  Forensics: Evidence successfully obfuscated", "success")
        
        self.step_completed_successfully()
