"""
Simplified Report Generation Utility
Generates simplified HTML and PDF reports with main details only
"""

import os
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import base64

class SimpleReportGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.setup_custom_styles()
    
    def setup_custom_styles(self):
        """Setup custom styles for the report"""
        # Title style
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Title'],
            fontSize=24,
            fontName='Helvetica-Bold',
            textColor=colors.red,
            alignment=TA_CENTER,
            spaceAfter=20
        )
        
        # Header style
        self.header_style = ParagraphStyle(
            'CustomHeader',
            parent=self.styles['Heading2'],
            fontSize=16,
            fontName='Helvetica-Bold',
            textColor=colors.green,
            spaceAfter=10
        )
        
        # Normal style
        self.normal_style = ParagraphStyle(
            'CustomNormal',
            parent=self.styles['Normal'],
            fontSize=12,
            fontName='Helvetica',
            textColor=colors.black,
            spaceAfter=6
        )
    
    def export_html(self, attack_timeline, target_info, file_path):
        """Export simplified HTML report"""
        html_content = self.generate_html_content(attack_timeline, target_info)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
    
    def generate_html_content(self, attack_timeline, target_info):
        """Generate simplified HTML report content"""
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Venom Serpent - Attack Report</title>
            <style>
                body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 0; padding: 20px; background: #0D1117; color: #F0F6FC; }}
                .header {{ text-align: center; margin-bottom: 30px; border-bottom: 2px solid #D32F2F; padding-bottom: 20px; }}
                .title {{ color: #D32F2F; font-size: 28px; margin: 0; }}
                .subtitle {{ color: #00FF41; font-size: 16px; margin: 5px 0; }}
                .author {{ color: #B0BEC5; font-size: 14px; }}
                .section {{ margin: 20px 0; padding: 15px; background: #1A1A1A; border-radius: 8px; border-left: 4px solid #D32F2F; }}
                .section h3 {{ color: #00FF41; margin-top: 0; }}
                .step-summary {{ margin: 15px 0; padding: 15px; background: #2D2D2D; border-radius: 5px; }}
                .step-title {{ color: #00FF41; font-size: 18px; margin-bottom: 10px; }}
                .step-details {{ color: #B0BEC5; margin: 5px 0; }}
                .footer {{ text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #2D2D2D; color: #B0BEC5; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1 class="title">VENOM SERPENT</h1>
                <p class="subtitle">Hold My Venom 🐍</p>
                <p class="author">by Psychic Cyber</p>
            </div>
            
            <div class="section">
                <h3>🎯 Target Information</h3>
                <p><strong>Target:</strong> {target_info.get('target', 'N/A')}</p>
                <p><strong>Port Range:</strong> {target_info.get('port_range', 'N/A')}</p>
                <p><strong>Attack Type:</strong> {target_info.get('attack_type', 'N/A')}</p>
                <p><strong>Report Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            
            <div class="section">
                <h3>📊 Attack Summary</h3>
        """
        
        # Simplified step summaries
        step_summaries = {
            'recon': {
                'title': '1. Reconnaissance',
                'details': [
                    '• Port scanning completed',
                    '• Open ports identified',
                    '• Services and protocols detected',
                    '• Vulnerabilities discovered'
                ]
            },
            'exploit': {
                'title': '2. Exploitation',
                'details': [
                    '• SQL injection vulnerabilities found',
                    '• XSS vulnerabilities identified',
                    '• Authentication bypass attempted',
                    '• Initial access gained'
                ]
            },
            'payload': {
                'title': '3. Payload Delivery',
                'details': [
                    '• Reverse shell payload deployed',
                    '• Command execution successful',
                    '• System access established',
                    '• Remote control achieved'
                ]
            },
            'persistence': {
                'title': '4. Persistence & Exfiltration',
                'details': [
                    '• Backdoor installation completed',
                    '• Scheduled tasks created',
                    '• Data exfiltration initiated',
                    '• Persistence mechanisms established'
                ]
            },
            'cleanup': {
                'title': '5. Cover Tracks',
                'details': [
                    '• Log files cleaned',
                    '• Evidence removed',
                    '• Traces eliminated',
                    '• Stealth maintained'
                ]
            }
        }
        
        for item in attack_timeline:
            step_id = item.get('step', '')
            if step_id in step_summaries:
                summary = step_summaries[step_id]
                html_content += f"""
                    <div class="step-summary">
                        <div class="step-title">{summary['title']}</div>
                """
                for detail in summary['details']:
                    html_content += f'<div class="step-details">{detail}</div>'
                html_content += "</div>"
        
        html_content += """
            </div>
            
            <div class="footer">
                <p>Generated by Venom Serpent - Professional Cybersecurity Tool</p>
                <p>© 2024 Psychic Cyber - Hold My Venom 🐍</p>
            </div>
        </body>
        </html>
        """
        
        return html_content
    
    def export_pdf(self, attack_timeline, target_info, file_path):
        """Export simplified PDF report"""
        doc = SimpleDocTemplate(file_path, pagesize=A4)
        story = []
        
        # Title
        story.append(Paragraph("VENOM SERPENT", self.title_style))
        story.append(Paragraph("Hold My Venom 🐍", self.header_style))
        story.append(Paragraph("by Psychic Cyber", self.normal_style))
        story.append(Spacer(1, 20))
        
        # Target Information
        story.append(Paragraph("Target Information", self.header_style))
        target_data = [
            ['Target:', target_info.get('target', 'N/A')],
            ['Port Range:', target_info.get('port_range', 'N/A')],
            ['Attack Type:', target_info.get('attack_type', 'N/A')],
            ['Report Generated:', datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
        ]
        
        target_table = Table(target_data, colWidths=[2*inch, 4*inch])
        target_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('BACKGROUND', (1, 0), (1, -1), colors.beige),
        ]))
        
        story.append(target_table)
        story.append(Spacer(1, 20))
        
        # Attack Summary
        story.append(Paragraph("Attack Summary", self.header_style))
        
        # Simplified step summaries
        step_summaries = {
            'recon': {
                'title': '1. Reconnaissance',
                'details': [
                    '• Port scanning completed',
                    '• Open ports identified',
                    '• Services and protocols detected',
                    '• Vulnerabilities discovered'
                ]
            },
            'exploit': {
                'title': '2. Exploitation',
                'details': [
                    '• SQL injection vulnerabilities found',
                    '• XSS vulnerabilities identified',
                    '• Authentication bypass attempted',
                    '• Initial access gained'
                ]
            },
            'payload': {
                'title': '3. Payload Delivery',
                'details': [
                    '• Reverse shell payload deployed',
                    '• Command execution successful',
                    '• System access established',
                    '• Remote control achieved'
                ]
            },
            'persistence': {
                'title': '4. Persistence & Exfiltration',
                'details': [
                    '• Backdoor installation completed',
                    '• Scheduled tasks created',
                    '• Data exfiltration initiated',
                    '• Persistence mechanisms established'
                ]
            },
            'cleanup': {
                'title': '5. Cover Tracks',
                'details': [
                    '• Log files cleaned',
                    '• Evidence removed',
                    '• Traces eliminated',
                    '• Stealth maintained'
                ]
            }
        }
        
        for item in attack_timeline:
            step_id = item.get('step', '')
            if step_id in step_summaries:
                summary = step_summaries[step_id]
                story.append(Paragraph(summary['title'], self.header_style))
                for detail in summary['details']:
                    story.append(Paragraph(detail, self.normal_style))
                story.append(Spacer(1, 10))
        
        # Footer with logo
        story.append(Spacer(1, 30))
        
        # Add logo if it exists
        logo_path = "assets/logo1.png"
        if os.path.exists(logo_path):
            try:
                logo = Image(logo_path, width=1*inch, height=1*inch)
                logo.hAlign = 'CENTER'
                story.append(logo)
                story.append(Spacer(1, 10))
            except:
                # If logo fails to load, continue without it
                pass
        
        story.append(Paragraph("Generated by Venom Serpent - Professional Cybersecurity Tool", self.normal_style))
        story.append(Paragraph("© 2024 Psychic Cyber - Hold My Venom 🐍", self.normal_style))
        
        doc.build(story)
