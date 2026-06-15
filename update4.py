import os

directory = r"d:\reheja universal"

files_to_process = [
    "index.html",
    "privacy-policy.html",
    "terms-conditions.html",
    "thank-you.html",
    "thank-you.php",
    "cookies-policy.html"
]

for fname in files_to_process:
    path = os.path.join(directory, fname)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Move from left to right
    content = content.replace('bottom:20px;left:20px;', 'bottom:20px;right:20px;')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Update 4 completed.")
