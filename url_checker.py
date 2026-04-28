import re

def check_url(url):
    score = 0
    reasons = []

    if not url.startswith("https"):
        score += 30
        reasons.append("No HTTPS")

    if len(url) > 50:
        score += 10
        reasons.append("Long URL")

    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        score += 25
        reasons.append("IP address used")

    keywords = ["login", "verify", "secure", "bank"]
    for k in keywords:
        if k in url.lower():
            score += 15
            reasons.append(f"Suspicious keyword: {k}")

    if score >= 60:
        risk = "High"
    elif score >= 30:
        risk = "Medium"
    else:
        risk = "Low"

    return score, risk, reasons