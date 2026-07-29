import re

html_path = r'c:\Users\Jesse\OneDrive\Desktop\Nikki Studio\dist\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace wrapper classes
new_content = re.sub(
    r'bg-pink-50 p-2 sm:p-3 rounded-2xl border-2 border-pink-200 shadow-sm hover:-translate-y-2 hover:shadow-md hover:border-primary transition-all duration-300',
    r'rounded-2xl border-2 border-[#FF2E93]/70 hover:-translate-y-2 hover:shadow-xl hover:border-primary hover:shadow-primary/20 transition-all duration-300 overflow-hidden',
    content
)

# Remove rounded-xl from images so they fill the wrapper cleanly
new_content = re.sub(
    r'(<img src="img/nikki-studio-\d+\.jpeg" alt="Nail Art" class="w-full h-48 sm:h-64 md:h-72 object-cover) rounded-xl(">)',
    r'\1\2',
    new_content
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
