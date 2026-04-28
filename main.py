from url_checker import check_url
from email_checker import check_email

print("=== Phishing Detector ===")

choice = input("1. Check URL\n2. Check Email\nChoose: ")

if choice == "1":
    url = input("\nEnter URL: ")
    score, risk, reasons = check_url(url)

elif choice == "2":
    try:
        with open("email.txt", "r", encoding="utf-8") as f:
            content = f.read()
        score, risk, reasons = check_email(content)
    except:
        print("Error reading email.txt")
        exit()

else:
    print("Invalid choice")
    exit()

print("\n==============================")
print("   PHISHING ANALYSIS REPORT")
print("==============================")

print(f"Risk Score: {score}/100")
print(f"Risk Level: {risk}")

print("\nReasons:")
if reasons:
    for r in reasons:
        print(" -", r)
else:
    print(" - No suspicious indicators found")

print("==============================")