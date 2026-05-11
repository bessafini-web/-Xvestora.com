path = r'C:\Users\Latifa\Desktop\claude project\xvestora\index.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Count Aaz El Arab sections
count = content.count('<!-- AAZ EL ARAB SECTION -->')
print(f"Aaz El Arab sections found: {count}")

# Find positions
idx1 = content.find('<!-- AAZ EL ARAB SECTION -->')
idx2 = content.find('<!-- AAZ EL ARAB SECTION -->', idx1 + 1)
print(f"First at: {idx1}")
print(f"Second at: {idx2}")
