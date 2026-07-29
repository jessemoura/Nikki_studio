html_path = r'c:\Users\Jesse\OneDrive\Desktop\Nikki Studio\dist\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the escaped quotes
content = content.replace('\\"', '"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
