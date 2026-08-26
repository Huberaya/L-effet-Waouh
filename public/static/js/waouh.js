// L'Effet Waouh - Éditorial Minimal Animations (inspiré Baya Hubert)
document.addEventListener('DOMContentLoaded', () => {
  const topbar = document.getElementById('topbar');
  if (topbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 100) topbar.classList.add('light');
      else topbar.classList.remove('light');
    });
  }

  const reveals = document.querySelectorAll('.reveal');
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('active');
        obs.unobserve(e.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
  reveals.forEach(r => obs.observe(r));

  // Gender reveal
  document.querySelectorAll('.gender-stage').forEach(gr => {
    let done = false;
    gr.addEventListener('click', () => {
      if (done) return;
      done = true;
      const isRose = Math.random() > 0.5;
      gr.classList.add(isRose ? 'rose' : 'bleu');
      createConfetti(isRose ? '#FF6B8A' : '#4FC3F7', 90);
      const hint = gr.querySelector('.hint');
      if (hint) hint.textContent = isRose ? "C'est une fille ! ♀" : "C'est un garçon ! ♂";
    });
  });

  // Smooth scroll for anchor
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', (e) => {
      const href = a.getAttribute('href');
      if (href.length > 1) {
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    });
  });
});

function createConfetti(color, count = 60) {
  const colors = color ? [color] : ['#C9A86A', '#B0764A', '#FF6B8A', '#4FC3F7'];
  for (let i = 0; i < count; i++) {
    const c = document.createElement('div');
    c.className = 'confetti';
    c.style.left = Math.random() * 100 + 'vw';
    c.style.top = '-10px';
    c.style.background = colors[Math.floor(Math.random() * colors.length)];
    c.style.width = (6 + Math.random() * 10) + 'px';
    c.style.height = c.style.width;
    c.style.borderRadius = Math.random() > 0.5 ? '50%' : '2px';
    c.style.transform = `rotate(${Math.random() * 360}deg)`;
    const dur = 2 + Math.random() * 2.5;
    const delay = Math.random() * 0.4;
    c.animate([
      { transform: `translateY(0) translateX(0) rotate(0deg)`, opacity: 1 },
      { transform: `translateY(${window.innerHeight + 100}px) translateX(${(Math.random()-0.5)*200}px) rotate(${720 + Math.random()*720}deg)`, opacity: 0 }
    ], { duration: dur * 1000, delay: delay * 1000, easing: 'cubic-bezier(.25,.46,.45,.94)' });
    document.body.appendChild(c);
    setTimeout(() => c.remove(), (dur + delay) * 1000 + 500);
  }
}
window.createConfetti = createConfetti;
