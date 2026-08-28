/* ═══════════════════════════════════════
   XVESTORA — script.js v2
═══════════════════════════════════════ */

// ─── LANGUAGE SWITCHER ───────────────────
const html      = document.documentElement;
const langBtns  = document.querySelectorAll('[data-lang-set]');

function setLanguage(lang) {
  html.setAttribute('data-lang', lang);
  html.setAttribute('lang', lang);

  // Show/hide .lang-fr / .lang-en blocks
  document.querySelectorAll('.lang-fr, .lang-en').forEach(el => {
    el.hidden = !el.classList.contains(`lang-${lang}`);
  });

  // Swap data-fr / data-en text content on elements that have both
  document.querySelectorAll('[data-fr][data-en]').forEach(el => {
    if (el.tagName !== 'SELECT') {
      el.textContent = el.getAttribute(`data-${lang}`);
    }
  });

  // Update active button state
  langBtns.forEach(btn => {
    btn.classList.toggle('active', btn.dataset.langSet === lang);
  });

  // Persist choice
  try { localStorage.setItem('xv-lang', lang); } catch (_) {}
}

langBtns.forEach(btn => {
  btn.addEventListener('click', () => setLanguage(btn.dataset.langSet));
});

// Restore saved preference
try {
  const saved = localStorage.getItem('xv-lang');
  if (saved && (saved === 'fr' || saved === 'en')) setLanguage(saved);
} catch (_) {}


// ─── TICKER PAUSE ON HOVER ───────────────
const tickerTrack = document.querySelector('.ticker__track');
if (tickerTrack) {
  tickerTrack.addEventListener('mouseenter', () => {
    tickerTrack.style.animationPlayState = 'paused';
  });
  tickerTrack.addEventListener('mouseleave', () => {
    tickerTrack.style.animationPlayState = 'running';
  });
}


// ─── NAV: SCROLL + ACTIVE LINKS ──────────
const nav      = document.getElementById('nav');
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav__links a');

function onScroll() {
  // Scrolled state — solid glassmorphism
  nav.classList.toggle('scrolled', window.scrollY > 50);

  // Active nav link highlight
  let current = '';
  sections.forEach(sec => {
    if (window.scrollY >= sec.offsetTop - 120) current = sec.id;
  });

  navLinks.forEach(link => {
    const href = link.getAttribute('href')?.replace('#', '');
    link.classList.toggle('active', href === current);
  });
}

window.addEventListener('scroll', onScroll, { passive: true });
onScroll(); // run once on load


// ─── MOBILE MENU ─────────────────────────
const burger     = document.getElementById('burger');
const mobileMenu = document.getElementById('mobileMenu');

if (burger && mobileMenu) {
  burger.addEventListener('click', () => {
    const isOpen = mobileMenu.classList.toggle('open');
    burger.classList.toggle('open', isOpen);
    burger.setAttribute('aria-expanded', isOpen);
  });

  // Close on link click
  mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      mobileMenu.classList.remove('open');
      burger.classList.remove('open');
    });
  });

  // Close on outside click
  document.addEventListener('click', e => {
    if (nav && !nav.contains(e.target)) {
      mobileMenu.classList.remove('open');
      burger.classList.remove('open');
    }
  });
}


// ─── VIDEO SLIDESHOW ─────────────────────
(function () {
  var slides   = document.querySelectorAll('.hero-slide');
  var labelEl  = document.getElementById('slideLabel');
  var fillEl   = document.getElementById('heroProgress');
  var current  = 0;
  var duration = 7000;
  var startTime;
  var raf;

  function activateSlide(idx) {
    // disabled: 4 hero videos replaced by hero-mix.mp4
    slides.forEach(function (s, i) {
      var vid = s.querySelector('video');
      if (i === idx) {
        s.classList.add('active');
        // if (vid) { vid.currentTime = 0; vid.play().catch(function () {}); }
        if (labelEl) labelEl.textContent = s.dataset.label || '';
      } else {
        s.classList.remove('active');
        // if (vid) vid.pause();
      }
    });
  }

  function animateProgress(ts) {
    if (!startTime) startTime = ts;
    var pct = Math.min(((ts - startTime) / duration) * 100, 100);
    if (fillEl) fillEl.style.width = pct + '%';
    if (pct < 100) {
      raf = requestAnimationFrame(animateProgress);
    } else {
      current = (current + 1) % slides.length;
      activateSlide(current);
      startTime = null;
      raf = requestAnimationFrame(animateProgress);
    }
  }

  if (slides.length) {
    activateSlide(0);
    raf = requestAnimationFrame(animateProgress);
  }
})();


// ─── REVEAL ON SCROLL ────────────────────
const revealEls = document.querySelectorAll('.reveal');

const revealObserver = new IntersectionObserver(
  entries => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(
          () => entry.target.classList.add('visible'),
          i * 55
        );
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.1, rootMargin: '0px 0px -32px 0px' }
);

revealEls.forEach(el => revealObserver.observe(el));

// Hero elements animate in immediately
document.querySelectorAll('.hero .reveal').forEach((el, i) => {
  setTimeout(() => el.classList.add('visible'), 180 + i * 110);
});


// ─── FORM SUBMISSION ─────────────────────
const form    = document.getElementById('accessForm');
const success = document.getElementById('formSuccess');

if (form) {
  form.addEventListener('submit', e => {
    e.preventDefault();

    const btn = form.querySelector('.btn--primary');
    const lang = html.getAttribute('data-lang') || 'fr';
    btn.textContent = lang === 'fr' ? 'Envoi en cours…' : 'Submitting…';
    btn.disabled = true;

    // Simulate async submit — replace with real endpoint
    setTimeout(() => {
      form.style.transition = 'opacity 0.4s, transform 0.4s';
      form.style.opacity    = '0';
      form.style.transform  = 'translateY(-8px)';
      setTimeout(() => {
        form.style.display = 'none';
        success.classList.add('visible');
      }, 400);
    }, 900);
  });
}


// ─── SMOOTH SCROLL for anchor links ──────
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', e => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    const offset = 108 + 20; // ticker + nav + buffer
    const top = target.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top, behavior: 'smooth' });
  });
});


// ─── STICKY MOBILE CTA ───────────────────
const mobileCta = document.getElementById('mobileCta');
if (mobileCta) {
  window.addEventListener('scroll', () => {
    mobileCta.classList.toggle('visible', window.scrollY > 300);
    mobileCta.setAttribute('aria-hidden', window.scrollY <= 300);
  }, { passive: true });
}


// ─── CURSOR LINE — subtle gold line on nav hover ──
// (micro-interaction: underline follows mouse across nav)
navLinks.forEach(link => {
  link.addEventListener('mouseenter', () => {
    navLinks.forEach(l => {
      if (l !== link) l.style.opacity = '0.55';
    });
  });
  link.addEventListener('mouseleave', () => {
    navLinks.forEach(l => { l.style.opacity = ''; });
  });
});
