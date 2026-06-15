import os

directory = r"d:\reheja universal"

files_to_process = [
    "index.html",
    "privacy-policy.html",
    "terms-conditions.html",
    "thank-you.html",
    "cookies-policy.html"
]

script_url = "https://script.google.com/macros/s/AKfycbzY3KfSEpb7NIhmUGYq94SzXchtIn9VyWi8nNzUFKT3P_vNyIV29QlDt7qW2oHy5co_uQ/exec"

# Instead of relying on a broken IF, let's just forcefully replace the whole block again.
new_code = f"""
    const GOOGLE_SCRIPT_URL = "{script_url}";
    
    // Convert to URL parameters for better compatibility with Apps Script no-cors
    const params = new URLSearchParams();
    params.append('name', lead.name);
    params.append('phone', lead.phone);
    params.append('email', lead.email);
    params.append('country', lead.country);
    params.append('enquiry', lead.enquiry);
    params.append('timestamp', lead.timestamp);

    fetch(GOOGLE_SCRIPT_URL, {{
      method: 'POST',
      body: params,
      mode: 'no-cors',
      headers: {{
        'Content-Type': 'application/x-www-form-urlencoded'
      }}
    }}).then(function() {{
      window.location.href = 'thank-you.html';
    }}).catch(function(err) {{
      console.error('Submission failed:', err);
      window.location.href = 'thank-you.html';
    }});
"""

# We'll use a regex to replace everything from `const GOOGLE_SCRIPT_URL` to the end of the `catch`/`else` block
import re

for fname in files_to_process:
    path = os.path.join(directory, fname)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the block starting with const GOOGLE_SCRIPT_URL = "https://..." and ending with the else block's }, 800); }
    pattern = r'const GOOGLE_SCRIPT_URL = "https://script\.google\.com.*?\n\s*\}\);\s*\}\s*else\s*\{\s*setTimeout\(function\(\)\s*\{\s*window\.location\.href\s*=\s*\'thank-you\.html\';\s*\},\s*800\);\s*\}'
    
    content = re.sub(pattern, new_code.strip(), content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Update 7 completed.")
