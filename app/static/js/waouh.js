// L'Effet Waouh - Animations JS
document.addEventListener('DOMContentLoaded', () => {
  // Topbar scroll effect
  const topbar = document.querySelector('.topbar');
  if (topbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) topbar.classList.add('scrolled');
      else topbar.classList.remove('scrolled');
    });
  }

  // Reveal on scroll
  const reveals = document.querySelectorAll('.reveal');
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('active');
        obs.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });
  reveals.forEach(r => obs.observe(r));

  // Product card 3D tilt
  document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const cx = rect.width / 2;
      const cy = rect.height / 2;
      const rx = (y - cy) / 20;
      const ry = (cx - x) / 20;
      card.style.transform = `translateY(-8px) rotateX(${rx}deg) rotateY(${ry}deg)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });

  // Gender reveal interaction
  const gr = document.querySelector('.gender-reveal');
  if (gr) {
    let revealed = false;
    gr.addEventListener('click', () => {
      if (revealed) return;
      revealed = true;
      const isRose = Math.random() > 0.5;
      gr.classList.add(isRose ? 'rose' : 'bleu');
      createConfetti(isRose ? '#FF6B8A' : '#4FC3F7', 80);
      gr.querySelector('.hint').textContent = isRose ? "C'est une fille ! ♀" : "C'est un garçon ! ♂";
      setTimeout(() => {
        gr.style.transform = 'scale(1.05)';
        setTimeout(() => gr.style.transform = '', 200);
      }, 300);
    });
  }

  // Bubbles background
  function createBubble() {
    const b = document.createElement('div');
    b.className = 'bubble';
    b.style.left = Math.random() * 100 + 'vw';
    b.style.width = b.style.height = (10 + Math.random() * 30) + 'px';
    b.style.animationDuration = (6 + Math.random() * 6) + 's';
    b.style.animationDelay = Math.random() * 2 + 's';
    document.body.appendChild(b);
    setTimeout(() => b.remove(), 12000);
  }
  if (document.querySelector('.hero')) {
    setInterval(createBubble, 800);
  }

  // Add to cart confetti
  document.querySelectorAll('form[action="/cart/add"]').forEach(form => {
    form.addEventListener('submit', (e) => {
      // Let form submit, but show confetti
      setTimeout(() => createConfetti('#D9A441', 30), 100);
    });
  });

  // Variant pills
  document.querySelectorAll('.variant-pill').forEach(pill => {
    pill.addEventListener('click', () => {
      const group = pill.parentElement;
      group.querySelectorAll('.variant-pill').forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      // Update hidden input
      const input = group.querySelector('input[type="hidden"][name="variant_id"]') || document.querySelector('select[name="variant_id"]');
      if (input) {
        if (input.tagName === 'SELECT') {
          input.value = pill.dataset.variantId;
        } else {
          input.value = pill.dataset.variantId;
        }
      }
      // Gender reveal color switch
      const gr = document.querySelector('.gender-reveal');
      if (gr && pill.dataset.color) {
        gr.className = 'gender-reveal ' + pill.dataset.color;
      }
    });
  });

  // Gallery thumbs
  document.querySelectorAll('.thumb').forEach(thumb => {
    thumb.addEventListener('click', () => {
      document.querySelectorAll('.thumb').forEach(t => t.classList.remove('active'));
      thumb.classList.add('active');
      const mainImg = document.querySelector('.gallery-main img');
      if (mainImg && thumb.dataset.img) {
        mainImg.style.opacity = '0';
        setTimeout(() => {
          mainImg.src = thumb.dataset.img;
          mainImg.style.opacity = '1';
        }, 200);
      }
    });
  });
});

function createConfetti(color, count = 50) {
  const colors = color ? [color] : ['#D9A441', '#B0764A', '#FF6B8A', '#4FC3F7', '#7A8B6F'];
  for (let i = 0; i < count; i++) {
    const c = document.createElement('div');
    c.className = 'confetti';
    c.style.left = Math.random() * 100 + 'vw';
    c.style.top = '-10px';
    c.style.background = colors[Math.floor(Math.random() * colors.length)];
    c.style.width = (6 + Math.random() * 8) + 'px';
    c.style.height = c.style.width;
    c.style.borderRadius = Math.random() > 0.5 ? '50%' : '2px';
    c.style.transform = `rotate(${Math.random() * 360}deg)`;
    c.style.animationDelay = Math.random() * 0.5 + 's';
    c.style.animationDuration = (2 + Math.random() * 2) + 's';
    document.body.appendChild(c);
    setTimeout(() => c.remove(), 4000);
  }
}

// Expose for inline calls
window.createConfetti = createConfetti;
