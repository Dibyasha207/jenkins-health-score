import random
import os

# Simulate build success & vulnerability score
build_success = random.randint(85, 100)
vulnerabilities = random.randint(0, 5)
final_score = max(0, build_success - vulnerabilities * 5)

# Save HTML report
os.makedirs("reports", exist_ok=True)
with open("reports/index.html", "w") as report:
    report.write(f"<h1>Jenkins Health and Security Score Report</h1>")
    report.write(f"<p><b>Build Success:</b> {build_success}%</p>")
    report.write(f"<p><b>Vulnerabilities Found:</b> {vulnerabilities}</p>")
    report.write(f"<p><b>Final Score:</b> {final_score}</p>")

print("✅ Report generated successfully! Check the 'reports' folder.")