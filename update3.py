import os
import re
import urllib.parse

directory = r"d:\reheja universal"

files_to_process = [
    "index.html",
    "privacy-policy.html",
    "terms-conditions.html",
    "thank-you.html",
    "thank-you.php",
    "cookies-policy.html"
]

prompt_text = urllib.parse.quote("Hi! I would like to know more about Raheja Lunaris.")

for fname in files_to_process:
    path = os.path.join(directory, fname)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Move to left:20px to avoid sidebar on right, and increase z-index to ensure visibility
    content = content.replace('right:20px;', 'left:20px;')
    # Increase z-index even more just in case
    content = content.replace('z-index:1000;', 'z-index:999999;')
    
    # Add pre-filled text prompt if not already present
    if "text=Hi" not in content:
        content = content.replace('https://wa.me/917021989706', f'https://wa.me/917021989706?text={prompt_text}')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Update 3 completed.")
