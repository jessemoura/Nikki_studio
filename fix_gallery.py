import re

html_path = r'c:\Users\Jesse\OneDrive\Desktop\Nikki Studio\dist\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the gallery image wrappers to remove gaps and rounding
new_content = re.sub(
    r'<div class=\"rounded-2xl border border-black hover:-translate-y-2 hover:shadow-xl hover:border-primary hover:shadow-primary/20 transition-all duration-300 overflow-hidden\">',
    r'<div class=\"relative overflow-hidden group\">',
    content
)

# And for the images inside, let's add a hover effect to replace the lost one
new_content = re.sub(
    r'<img src=\"(img/nikki-studio-\d+\.jpeg)\" alt=\"Nail Art\" class=\"w-full h-48 sm:h-64 md:h-72 object-cover\">',
    r'<img src=\"\1\" alt=\"Nail Art\" class=\"w-full h-64 md:h-80 object-cover group-hover:scale-110 transition-transform duration-500\">',
    new_content
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
