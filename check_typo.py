import re
path = r'C:\Users\Latifa\Desktop\claude project\xvestora\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
matches = list(re.finditer('xvistora', content, re.IGNORECASE))
print(f'Total Xvistora occurrences: {len(matches)}')
for m in matches[:15]:
    start = max(0, m.start()-80)
    end = min(len(content), m.end()+80)
    print('---')
    print(repr(content[start:end]))
