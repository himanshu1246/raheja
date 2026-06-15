import os

directory = r"d:\reheja universal"

files_to_process = [
    "index.html",
    "privacy-policy.html",
    "terms-conditions.html",
    "thank-you.html",
    "cookies-policy.html"
]

old_url = "https://script.google.com/macros/s/AKfycbzY3KfSEpb7NIhmUGYq94SzXchtIn9VyWi8nNzUFKT3P_vNyIV29QlDt7qW2oHy5co_uQ/exec"
new_url = "https://script.google.com/macros/s/AKfycbzZ1XjC0GdQ0ilsZY2Jj3JZ9YlcOJRgeqy8QQl-hacCOZwaYzgoSDVWCjGNPYJKzwShTg/exec"

for fname in files_to_process:
    path = os.path.join(directory, fname)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace(old_url, new_url)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Update 8 completed.")
