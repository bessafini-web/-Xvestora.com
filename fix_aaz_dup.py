path = r'C:\Users\Latifa\Desktop\claude project\xvestora\index.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Count duplicates
count = content.count('<!-- AAZ EL ARAB SECTION -->')
print(f"Aaz sections: {count}")

if count >= 2:
    # Find the two sections
    idx1 = content.find('<!-- AAZ EL ARAB SECTION -->')
    idx2 = content.find('<!-- AAZ EL ARAB SECTION -->', idx1 + 1)
    
    # Find end of second section (before NETWORK SECTION)
    end2 = content.find('<!-- NETWORK SECTION -->', idx2)
    
    # Remove the second duplicate (keep first)
    content = content[:idx2] + content[end2:]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Duplicate removed!")
else:
    print("No duplicate found")

print(f"File: {len(content)//1024} KB")
