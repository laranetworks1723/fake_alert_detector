# fake_alert_detector
Python-based Fake Alert Detector that scans log files and categorizes failed login attempts as REAL or FAKE.  Uses file handling and conditional logic to generate automated security reports with threat counts.
>>> Fake Login Detector

A Python-based security tool that detects and categorizes fake/suspicious login attempts from log files. Built as my first step into cybersecurity + automation.

>>>>What it does
This script scans a `sample.log` file, identifies login entries, and flags them as **REAL** or **FAKE** based on username patterns. It then gives you a quick summary of total real vs fake attempts.

Perfect for learning: File I/O, String manipulation, Conditional logic, and Basic security concepts.

>>>Tech Stack
- **Language**: Python 3
- **Concepts**: File Handling, Loops, if/else, String `in` operator

>>>How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/fake-login-detector.git
   cd fake-login-detector
   Make sure sample.log is in the same folder. Example content
      user: admin - login: REAL
   user: xyz123 - login: FAKE
   user: root - login: REAL
   Run the script:
      python fake_detector.py
    Sample Output:
   REAL: user: admin - login: REAL
FAKE: user: xyz123 - login: FAKE
REAL: user: root - login: REAL

Summary:
Real Logins: 2
Fake Logins: 1
