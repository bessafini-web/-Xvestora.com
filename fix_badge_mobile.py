path = r'C:\Users\Latifa\Desktop\claude project\xvestora\index.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix badge - one line, smaller
old_badge_html = '''      <div class="hero-badge-v2">
        <span class="hero-badge-dot"></span>
        <span>Accès Privé · Maroc</span>
        <span class="hero-badge-sep">|</span>
        <span>Investisseurs Qualifiés Uniquement</span>
      </div>'''

new_badge_html = '''      <div class="hero-badge-v2">
        <span class="hero-badge-dot"></span>
        <span>Accès Privé · Maroc &nbsp;|&nbsp; Investisseurs Qualifiés Uniquement</span>
      </div>'''

if old_badge_html in content:
    content = content.replace(old_badge_html, new_badge_html)
    print("✅ Badge fixed - one line")
else:
    print("❌ Badge not found")

# Fix badge CSS - nowrap
old_badge_css = '.hero-badge-v2{display:inline-flex;align-items:center;gap:8px;border:1px solid rgba(168,123,69,0.18);background:rgba(168,123,69,0.04);color:rgba(255,255,255,0.35);font-size:8px;letter-spacing:2.5px;text-transform:uppercase;padding:5px 12px;margin-bottom:22px;backdrop-filter:blur(8px)}'
new_badge_css = '.hero-badge-v2{display:inline-flex;align-items:center;gap:8px;border:1px solid rgba(168,123,69,0.18);background:rgba(168,123,69,0.04);color:rgba(255,255,255,0.35);font-size:8px;letter-spacing:2px;text-transform:uppercase;padding:5px 14px;margin-bottom:22px;backdrop-filter:blur(8px);white-space:nowrap}'

if old_badge_css in content:
    content = content.replace(old_badge_css, new_badge_css)
    print("✅ Badge CSS - nowrap added")
else:
    print("❌ Badge CSS not found")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Done! {len(content)//1024} KB")
