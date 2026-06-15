import os
import re

directory = r"d:\reheja universal"

files_to_process = [
    "index.html",
    "privacy-policy.html",
    "terms-conditions.html",
    "thank-you.html",
    "cookies-policy.html"
]

for fname in files_to_process:
    path = os.path.join(directory, fname)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The problem is that lead.name, lead.phone etc. are being accessed outside their block scope.
    # The original variables `name`, `phone`, `email`, `country`, `enquiredFor` are available.
    
    old_code = """    // Convert to URL parameters for better compatibility with Apps Script no-cors
    const params = new URLSearchParams();
    params.append('name', lead.name);
    params.append('phone', lead.phone);
    params.append('email', lead.email);
    params.append('country', lead.country);
    params.append('enquiry', lead.enquiry);
    params.append('timestamp', lead.timestamp);"""
    
    new_code = """    // Convert to URL parameters for better compatibility with Apps Script no-cors
    const params = new URLSearchParams();
    params.append('name', name ? name.trim() : "N/A");
    params.append('phone', phone ? phone.trim() : "N/A");
    params.append('email', email ? email.trim() : "N/A");
    params.append('country', country || "India");
    params.append('enquiry', enquiredFor || "N/A");
    params.append('timestamp', new Date().toLocaleString());"""

    content = content.replace(old_code, new_code)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Update 11 completed.")
