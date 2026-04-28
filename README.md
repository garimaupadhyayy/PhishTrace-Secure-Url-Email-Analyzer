# PhishTrace - Secure URL & Email Analyzer

PhishTrace is a rule-based phishing detection system designed to analyze both URLs and email content for potential security threats.
It leverages heuristic techniques to identify suspicious patterns such as insecure protocols, misleading keywords, and social engineering indicators.
The system evaluates multiple features of the input and assigns a weighted risk score based on detected anomalies.
It then classifies the result into Low, Medium, or High risk levels to assist in quick decision-making.
Additionally, it provides clear and explainable reasons behind each detection, making the system transparent and easy to understand.
The project focuses on practical cybersecurity techniques and emphasizes interpretability over black-box models.

## 🚀 Features

### 🔗 URL Analysis

* Detects insecure protocols (HTTP)
* Identifies suspicious keywords (login, verify, bank, secure)
* Flags IP-based URLs
* Analyzes URL length and structure

### 📧 Email Analysis

* Detects urgency language (urgent, immediate action, verify)
* Identifies suspicious links
* Flags abnormal or phishing-like patterns

### 📊 Risk Scoring

* Generates a risk score (0–100)
* Classifies results as:
  * Low Risk
  * Medium Risk
  * High Risk
* Provides clear reasons for each detection

## 🛠️ Tech Stack

* Python
* Regular Expressions (`re`)
* Rule-Based (Heuristic) Analysis

## ▶️ How to Run

```bash
python main.py
```

## 🧪 Sample Inputs

### 🔹 Suspicious URL

```
http://verify-paypal-login.com
```

### 🔹 Suspicious Email

```
URGENT: Verify your account immediately
Click here: http://fake-login.com
```

---

## 💡 Key Concept

This project focuses on **explainable security**, where each detection is based on clear rules rather than black-box models.


## 🔮 Future Improvements

* Machine Learning-based detection
* Integration with threat intelligence APIs (e.g., VirusTotal)
* Web-based interface (Flask/React)


## 👩‍💻 Author

Garima Upadhyay
