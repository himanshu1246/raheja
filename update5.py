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

replacement_js = """
    const GOOGLE_SCRIPT_URL = "YOUR_GOOGLE_SCRIPT_URL_HERE";
    
    if (GOOGLE_SCRIPT_URL !== "YOUR_GOOGLE_SCRIPT_URL_HERE") {
      const formData = new FormData();
      formData.append('name', lead.name);
      formData.append('phone', lead.phone);
      formData.append('email', lead.email);
      formData.append('country', lead.country);
      formData.append('enquiry', lead.enquiry);
      formData.append('timestamp', lead.timestamp);

      fetch(GOOGLE_SCRIPT_URL, {
        method: 'POST',
        body: formData,
        mode: 'no-cors'
      }).then(function() {
        window.location.href = 'thank-you.html';
      }).catch(function(err) {
        console.error('Submission failed:', err);
        window.location.href = 'thank-you.html';
      });
    } else {
      setTimeout(function() {
        window.location.href = 'thank-you.html';
      }, 800);
    }
"""

for fname in files_to_process:
    path = os.path.join(directory, fname)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace the setTimeout block at the end of the submit handler
    old_code = """    // Simulate a brief delay to feel like a backend submit and redirect
    setTimeout(function() {
      window.location.href = 'thank-you.html';
    }, 800);"""
    
    if old_code in content:
        content = content.replace(old_code, replacement_js)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Update 5 completed.")
