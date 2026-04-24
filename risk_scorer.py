# NexaCloud Ltd - GRC Risk Register
# Author: Uttam Yadav
# Framework: NIST SP 800-53 Rev 5
# Purpose: Score and prioritise security risks

import csv

risks = []

risks.append({"id": "R-001", "name": "Phishing Attack", "likelihood": 4, "impact": 4, "nist_control": "IA-2, AT-2", "mitigation": "Enforce MFA on all accounts. Quarterly phishing training.", "owner": "IT Security", "status": "In Progress"})
risks.append({"id": "R-002", "name": "Misconfigured S3 Bucket", "likelihood": 3, "impact": 5, "nist_control": "CM-6, AU-2", "mitigation": "Enable AWS Block Public Access. Config rules to alert on public buckets.", "owner": "Cloud Engineering", "status": "Planned"})
risks.append({"id": "R-003", "name": "Ransomware Attack", "likelihood": 3, "impact": 5, "nist_control": "CP-9, IR-4, SI-3", "mitigation": "Immutable backups tested monthly. EDR on all endpoints. IR runbooks.", "owner": "IT Security", "status": "In Progress"})
risks.append({"id": "R-004", "name": "Insider Threat - Data Exfiltration", "likelihood": 2, "impact": 5, "nist_control": "AC-6, AU-9, PS-4", "mitigation": "Least privilege RBAC. Session recording on admin accounts. 90-day access reviews.", "owner": "HR + IT Security", "status": "Implemented"})
risks.append({"id": "R-005", "name": "DDoS Platform Outage", "likelihood": 3, "impact": 3, "nist_control": "SC-5, CP-8", "mitigation": "Cloudflare Magic Transit enabled. Auto-scaling configured. WAF rate limiting.", "owner": "Platform Engineering", "status": "Implemented"})
risks.append({"id": "R-006", "name": "Third-Party Vendor Breach", "likelihood": 3, "impact": 4, "nist_control": "SR-3, SA-9", "mitigation": "Annual vendor assessments. Contractual breach notification clauses.", "owner": "GRC / Legal", "status": "In Progress"})
risks.append({"id": "R-007", "name": "SQL Injection Vulnerability", "likelihood": 3, "impact": 4, "nist_control": "SI-10, SI-2, SA-11", "mitigation": "Cloudflare WAF blocks OWASP Top 10. SAST scanning in CI/CD pipeline.", "owner": "Application Security", "status": "In Progress"})
risks.append({"id": "R-008", "name": "GDPR Non-Compliance", "likelihood": 2, "impact": 4, "nist_control": "PT-1, PT-2, PM-19", "mitigation": "DSAR workflow implemented. DPO appointed. Annual GDPR training.", "owner": "DPO / Legal", "status": "Implemented"})
risks.append({"id": "R-009", "name": "Shadow IT - Unapproved SaaS", "likelihood": 4, "impact": 3, "nist_control": "CM-8, SA-9, AC-20", "mitigation": "Cloudflare Gateway detects unapproved apps. Approved software catalogue published.", "owner": "IT Security", "status": "Planned"})
risks.append({"id": "R-010", "name": "Business Email Compromise", "likelihood": 3, "impact": 4, "nist_control": "AT-2, SI-8", "mitigation": "DMARC/DKIM/SPF enforced. Dual authorisation for payments over 5000.", "owner": "Finance + IT Security", "status": "In Progress"})


def score_risk(likelihood, impact):
    return likelihood * impact


def get_rating(score):
    if score >= 20:
        return "CRITICAL"
    elif score >= 10:
        return "HIGH"
    elif score >= 6:
        return "MEDIUM"
    else:
        return "LOW"


print("=" * 60)
print("  NEXACLOUD LTD - RISK REGISTER")
print("=" * 60)

critical = 0
high = 0
medium = 0
low = 0

for risk in risks:
    s = score_risk(risk["likelihood"], risk["impact"])
    r = get_rating(s)
    if r == "CRITICAL":
        critical += 1
    elif r == "HIGH":
        high += 1
    elif r == "MEDIUM":
        medium += 1
    else:
        low += 1

print(f"\nTOTAL RISKS: {len(risks)}")
print(f"  CRITICAL : {critical}")
print(f"  HIGH     : {high}")
print(f"  MEDIUM   : {medium}")
print(f"  LOW      : {low}")
print("=" * 60)

sorted_risks = sorted(risks, key=lambda r: r["likelihood"] * r["impact"], reverse=True)

for risk in sorted_risks:
    score = score_risk(risk["likelihood"], risk["impact"])
    rating = get_rating(score)
    print(f"\nID:         {risk['id']}")
    print(f"Risk:       {risk['name']}")
    print(f"Likelihood: {risk['likelihood']}  |  Impact: {risk['impact']}  |  Score: {score}")
    print(f"Rating:     {rating}")
    print(f"Control:    {risk['nist_control']}")
    print(f"Owner:      {risk['owner']}")
    print(f"Status:     {risk['status']}")
    print(f"Mitigation: {risk['mitigation']}")
    print("-" * 60)

with open("risk_register_output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "likelihood", "impact", "score", "rating", "nist_control", "owner", "status", "mitigation"])
    writer.writeheader()
    for risk in sorted_risks:
        score = score_risk(risk["likelihood"], risk["impact"])
        rating = get_rating(score)
        risk["score"] = score
        risk["rating"] = rating
        writer.writerow(risk)

print("\nCSV exported: risk_register_output.csv")