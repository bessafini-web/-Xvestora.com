path = r'C:\Users\Latifa\Desktop\claude project\xvestora\index.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix badge on mobile - hide it completely or simplify
old_mobile = '''@media(max-width:640px){
  .nav-menu{display:none}
  .nav-ham{display:flex}
  .intel-strip{display:none}
  .nav{top:0}
  #hero-v2{margin-top:72px}
  .page-hero{margin-top:72px;padding:130px 6% 56px}
  .sectors-grid{grid-template-columns:1fr}
  .sector-card:first-child{grid-column:span 1}
  .process-steps{grid-template-columns:1fr}
  .frow{grid-template-columns:1fr}
  .cta-band{flex-direction:column;text-align:center}
  .footer-top{grid-template-columns:1fr}
  .section{padding:64px 6%}
  .wa-float span{display:none}
  .wa-float{padding:13px;border-radius:50%}
  .scroll-cue{display:none}
  .tagline-band p{font-size:16px}
  .trust-metrics{flex-direction:column}
  .trust-metric-sep{display:none}
  .trust-metric{padding:32px 6%;border-bottom:1px solid rgba(255,255,255,0.04)}
  .trust-statement{padding:44px 6%}
  .hti-sep{display:none}
  .market-band{grid-template-columns:1fr}
  .market-band-item{border-right:none;border-bottom:1px solid rgba(255,255,255,0.04);padding:24px 0}
  .process-v2{grid-template-columns:1fr}
  .services-v2{grid-template-columns:1fr}
  .morocco-regions{grid-template-columns:1fr}
  .about-stat-row{grid-template-columns:1fr}
}'''

new_mobile = '''@media(max-width:640px){
  .nav-menu{display:none}
  .nav-ham{display:flex}
  .intel-strip{display:none}
  .nav{top:0}
  #hero-v2{margin-top:72px}
  .page-hero{margin-top:72px;padding:130px 6% 56px}
  .sectors-grid{grid-template-columns:1fr}
  .sector-card:first-child{grid-column:span 1}
  .process-steps{grid-template-columns:1fr}
  .frow{grid-template-columns:1fr}
  .cta-band{flex-direction:column;text-align:center}
  .footer-top{grid-template-columns:1fr}
  .section{padding:64px 6%}
  .wa-float span{display:none}
  .wa-float{padding:13px;border-radius:50%}
  .scroll-cue{display:none}
  .tagline-band p{font-size:16px}
  .trust-metrics{flex-direction:column}
  .trust-metric-sep{display:none}
  .trust-metric{padding:32px 6%;border-bottom:1px solid rgba(255,255,255,0.04)}
  .trust-statement{padding:44px 6%}
  .hti-sep{display:none}
  .market-band{grid-template-columns:1fr}
  .market-band-item{border-right:none;border-bottom:1px solid rgba(255,255,255,0.04);padding:24px 0}
  .process-v2{grid-template-columns:1fr}
  .services-v2{grid-template-columns:1fr}
  .morocco-regions{grid-template-columns:1fr}
  .about-stat-row{grid-template-columns:1fr}
  .hero-badge-v2{display:none}
  .hero-h1-v2{font-size:clamp(28px,8vw,40px)}
  .hero-sub-v2{font-size:13px}
}'''

if old_mobile in content:
    content = content.replace(old_mobile, new_mobile)
    print("✅ Badge hidden on mobile + hero font fixed")
else:
    print("❌ Mobile CSS not found")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Done! {len(content)//1024} KB")
