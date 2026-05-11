path = r'C:\Users\Latifa\Desktop\claude project\xvestora\index.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find exact badge HTML
idx = content.find('hero-badge-v2')
print(f"Badge found at index: {idx}")
print(repr(content[idx-10:idx+300]))
