# 🛡️ URL Phishing Detector

A Python-based phishing URL detector that analyzes URLs using multiple cybersecurity techniques. The tool assigns a risk score based on various security checks and provides detailed explanations for why a URL is considered safe or suspicious.

This project was built to strengthen Python programming, networking, and cybersecurity concepts while following a modular software design.

---

## 🚀 Features

- ✅ URL Validation
- ✅ HTTPS Detection
- ✅ URL Length Analysis
- ✅ IP Address Detection
- ✅ '@' Symbol Detection
- ✅ Multiple Dot Detection
- ✅ Hyphen Detection
- ✅ Digit Detection
- ✅ Suspicious Keyword Detection
- ✅ URL Shortener Detection
- ✅ Double Slash Detection
- ✅ Suspicious Top-Level Domain (TLD) Detection
- ✅ Encoded Character Detection
- ✅ Redirect Detection
- ✅ Unicode/Punycode Detection
- ✅ WHOIS Domain Age Detection
- ✅ DNS Resolution Check
- ✅ Risk Score Calculation
- ✅ Detailed Security Report

---

## 🖥️ Technologies Used

- Python 3
- Requests
- urllib.parse
- python-whois
- socket
- datetime
- Regular Expressions (re)
- Git & GitHub

---

## 📂 Project Structure

```
URL-Phishing-Detector/
│
├── main.py              # User interface and program entry point
├── detector.py          # Risk scoring engine
├── url_features.py      # Individual phishing detection features
├── requirements.txt     # Required Python libraries
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/url-phishing-detector.git
```

### Navigate into the project

```bash
cd url-phishing-detector
```

### Install dependencies

```bash
pip install requests python-whois
```

### Run the application

```bash
python main.py
```

---

## 📋 Example Output

```
Status: Suspicious

Risk Score: 35/100

Reasons:

• Uses HTTPS connection.
• URL length is normal.
• URL uses a domain name.
• No '@' symbol found.
• No suspicious keywords detected.
• DNS resolved successfully.
• Resolved IP: 142.xxx.xxx.xxx
• Domain age is 4520 days (appears established).
```

---

## 🧠 Detection Techniques

The detector performs multiple security checks, including:

- URL structure analysis
- HTTPS verification
- Domain age verification using WHOIS
- DNS resolution
- Redirect analysis
- Unicode/Punycode detection
- URL encoding detection
- Suspicious keyword analysis
- Suspicious TLD detection
- URL shortener detection
- IP address detection
- Character pattern analysis

Each check contributes to the final phishing risk score.

---

## 📈 Future Improvements

- 🔒 SSL Certificate Validation
- 🌐 Suspicious Subdomain Detection
- 🛡️ VirusTotal API Integration
- 📄 PDF Scan Reports
- 🎨 Improved GUI
- 🤖 Machine Learning-Based Detection
- 🌍 Blacklist Database Integration

---

## 🎯 Purpose

This project was developed to practice and improve:

- Python Programming
- Networking Fundamentals
- Cybersecurity Concepts
- Secure Coding Practices
- Git & GitHub Workflow
- Software Design

---

## ⚠️ Disclaimer

This project is intended for educational purposes only. It should not be considered a replacement for professional security software or enterprise phishing detection solutions.

---

## 👨‍💻 Author

**Rahul Tewatia**

If you found this project useful, consider giving it a ⭐ on GitHub!
