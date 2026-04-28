import re

def check_email(content):
    score = 0
    reasons = []

    words = ["urgent", "verify", "immediately", "suspend"]
    for w in words:
        if w in content.lower():
            score += 15
            reasons.append(f"Urgency word: {w}")

    links = re.findall(r"http[s]?://\S+", content)
    if len(links) > 1:
        score += 20
        reasons.append("Multiple links")

    if "@" not in content:
        score += 10
        reasons.append("No proper email format")

    if score >= 50:
        risk = "High"
    elif score >= 25:
        risk = "Medium"
    else:
        risk = "Low"

    return score, risk, reasons