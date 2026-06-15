import os
import re

directory = r"d:\reheja universal"

files_to_process = [
    "index.html",
    "privacy-policy.html",
    "terms-conditions.html",
    "thank-you.html",
    "thank-you.php",
    "cookies-policy.html"
]

whatsapp_html = """
<!-- WhatsApp Float -->
<a href="https://wa.me/917021989706" class="whatsapp-float" style="position:fixed;width:60px;height:60px;bottom:20px;right:20px;background-color:#25d366;color:#FFF;border-radius:50px;text-align:center;font-size:30px;box-shadow: 2px 2px 3px #999;z-index:1000;display:flex;align-items:center;justify-content:center;" target="_blank" aria-label="Chat on WhatsApp">
    <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-whatsapp" viewBox="0 0 16 16">
      <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
    </svg>
</a>
"""

for fname in files_to_process:
    path = os.path.join(directory, fname)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # If whatsapp_html not in content, we might have already messed up index.html or maybe not. 
    # Let's remove the remaining chat wrappers.
    content = re.sub(r'<div class="chat-wrapper">.*?</div>\s*<!-- Chatbot -->', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- Chatbot -->\s*<div id="chat-square".*?<!-- Chatbot -->', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- Small Chatbot -->.*?<!-- Small Chatbot -->', '', content, flags=re.DOTALL)
    
    # Also remove any stranded bot code:
    content = re.sub(r'<div class="chat-header-name">Pooja</div>', '', content)
    content = re.sub(r'<script src="\./assets/js/chatv27\.js"></script>', '', content)
    content = re.sub(r'<script>\s*var chatbotApiInput = \{.*?\};\s*</script>', '', content, flags=re.DOTALL)

    # For cookies-policy specifically, make sure to replace things we did for others:
    content = re.sub(r'<li class="nav-item"><a class="nav-link" href="#gallery"><i class="mi mi-gallery nav-icon"></i> Gallery</a></li>', '', content)
    content = re.sub(r'<section class="section shadow-sm lazyload" id="gallery">.*?</section>', '', content, flags=re.DOTALL)
    content = re.sub(r'<link rel="stylesheet"\s*href="\./assets/css/chatv25\.css"[^>]*>', '', content, flags=re.DOTALL)
    content = re.sub(r'<link rel="stylesheet" href="\./assets/css/chatv25\.css" />', '', content)
    content = content.replace('+917021989706', '70219 89706')
    content = content.replace("Home Bazaar Services Pvt Ltd", "Millennium Proptech Private Limited")
    content = content.replace("A52000000045", "A51700058018")
    content = re.sub(r',\s*CIN\s*U45400MH2013PTC242930', '', content)

    # Ensure whatsapp float is there (append before </head> or </body> if not present)
    if "whatsapp-float" not in content:
        content = content.replace('</body>', whatsapp_html + '\n</body>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Update 2 completed.")
