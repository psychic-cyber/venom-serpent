# 🐍 Venom Serpent - Professional Cybersecurity Simulation Tool

**Hold My Venom** - A comprehensive penetration testing simulation platform designed for cybersecurity professionals and students.

## 🎯 Overview

Venom Serpent is a professional-grade cybersecurity simulation tool that demonstrates the complete attack lifecycle in a safe, controlled environment. Built with PyQt5, it provides an intuitive graphical interface for understanding penetration testing methodologies.

## 📸 Screenshots

### Main Interface
![Main Interface](https://github.com/psychic-cyber/venom-serpent/blob/254adfc3bb5ea6c96542fb52c9d19f59a4a16bd1/screenshots/main.png)
*Professional dark theme with attack timeline and step navigation*

### Reconnaissance Phase
![Reconnaissance Phase](https://github.com/psychic-cyber/venom-serpent/blob/254adfc3bb5ea6c96542fb52c9d19f59a4a16bd1/screenshots/reconnaissance.png)
*Port scanning and service detection with real-time log output*

### Exploitation Phase
![Exploitation Phase](https://github.com/psychic-cyber/venom-serpent/blob/35f9bf0e98a0cd60220365c5f7c82f27fbc9f750/screenshots/exploit.png)
*SQL injection and XSS demonstrations with detailed logs*

### Payload Delivery
![Payload Delivery](https://github.com/psychic-cyber/venom-serpent/blob/35f9bf0e98a0cd60220365c5f7c82f27fbc9f750/screenshots/payload.png)
*Reverse shell simulation and payload deployment*

### Persistence Phase
![Persistence](https://github.com/psychic-cyber/venom-serpent/blob/35f9bf0e98a0cd60220365c5f7c82f27fbc9f750/screenshots/persistence.png)
*Execute persistence to gather intelligence and vulnerabilities*

### Cover Tracks Phase
![Cover Paths](https://github.com/psychic-cyber/venom-serpent/blob/35f9bf0e98a0cd60220365c5f7c82f27fbc9f750/screenshots/cover.png)
*Covering tracks and logs*

## ✨ Features

### 🔍 **Step-by-Step Attack Simulation**
- **Reconnaissance**: Port scanning, service detection, vulnerability assessment
- **Exploitation**: SQL injection, XSS, privilege escalation demonstrations
- **Payload Delivery**: Reverse shell simulation and payload deployment
- **Persistence**: Backdoor installation and persistence mechanisms
- **Cover Tracks**: Log cleaning and forensic countermeasures

### 🎨 **Professional Interface**
- **Dark Theme**: Modern, professional dark interface
- **Responsive Design**: Adapts to different screen sizes
- **Interactive Elements**: Hover effects and smooth animations
- **Step Navigation**: Clear progression through attack phases
- **Real-time Logs**: Simulated attack logs with color-coded output

### 📊 **Reporting & Documentation**
- **PDF Reports**: Professional reports with logo and branding
- **HTML Export**: Web-compatible report generation
- **Attack Timeline**: Visual progress tracking
- **Target Configuration**: Customizable target information

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- PyQt5
- ReportLab

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd venom-serpent

# Install dependencies
pip install -r requirements.txt

# Run the application
python main_new.py
```

### Demo Mode
```bash
# Run the demo script
python demo_enhanced_final.py
```

## 🏗️ Project Structure

```
venom_serpent/
├── main_new.py              # Main application entry point
├── demo_enhanced_final.py   # Demo script
├── requirements.txt         # Python dependencies
├── assets/
│   └── logo1.png           # Application logo
├── modules/                 # Attack simulation modules
│   ├── recon.py            # Reconnaissance module
│   ├── exploit.py          # Exploitation module
│   ├── payload.py          # Payload delivery module
│   ├── persistence.py      # Persistence module
│   └── cleanup.py          # Cover tracks module
├── windows/                 # GUI step windows
│   ├── recon_window.py     # Reconnaissance window
│   ├── exploit_window.py   # Exploitation window
│   ├── payload_window.py   # Payload delivery window
│   ├── persistence_window.py # Persistence window
│   └── cleanup_window.py   # Cover tracks window
├── utils/                   # Utility modules
│   ├── professional_theme.py # Professional dark theme
│   ├── simple_report_gen.py  # Report generation
│   ├── splash_screen.py    # Splash screen
│   ├── step_window.py      # Base step window class
│   └── timeline_tracker.py # Attack timeline tracker
└── reports/                 # Generated reports
    └── *.pdf               # PDF reports with logo
```

## 🎮 Usage

### 1. **Configure Target**
- Click "CONFIGURE TARGET" to set target information
- Enter target IP, port range, and attack type
- All simulations are safe and local

### 2. **Start Attack Simulation**
- Click "START ATTACK" to begin the simulation
- Navigate through each attack phase using the step tabs
- Execute each step to see simulated attack logs

### 3. **Monitor Progress**
- Track progress in the Attack Timeline panel
- View real-time logs for each attack phase
- Monitor completion status of each step

### 4. **Generate Reports**
- Click "EXPORT REPORT" to generate PDF/HTML reports
- Reports include attack timeline and key findings
- Professional branding with logo and author information

## 🛡️ Safety Features

- **Simulation Mode**: All attacks are simulated, no real harm
- **Local Testing**: Designed for localhost testing only
- **Educational Purpose**: Intended for learning and demonstration
- **Safe Environment**: No actual network penetration

## 🎨 Customization

### Themes
The application uses a professional dark theme with:
- GitHub Dark-inspired color palette
- Inter font family for modern typography
- Responsive design for different screen sizes
- Professional button hover effects

### Branding
- Customizable logo integration
- Professional report templates
- Consistent branding throughout the interface

## 📋 Requirements

- **Python**: 3.7 or higher
- **PyQt5**: For GUI framework
- **ReportLab**: For PDF report generation
- **Pillow**: For image processing

## 🤝 Contributing

This project is designed for educational and professional demonstration purposes. Contributions are welcome for:
- Additional attack simulation modules
- UI/UX improvements
- Report template enhancements
- Documentation updates

## 📄 License

This project is created for educational and professional demonstration purposes. Please use responsibly and in accordance with applicable laws and regulations.

## 👨‍💻 Author

**Psychic Cyber** - Cybersecurity Professional

---

**⚠️ Disclaimer**: This tool is designed for educational and authorized testing purposes only. Users are responsible for ensuring compliance with applicable laws and regulations. The authors are not responsible for any misuse of this software.

**🐍 Hold My Venom** - Professional Cybersecurity Simulation
