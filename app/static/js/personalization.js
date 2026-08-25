/**
 * Personalization Canvas Live Preview - V3
 * Axe stratégique: Produit → Personnalisation → Aperçu → Commande
 */
class PersonalizationPreview {
  constructor(canvasId, inputs) {
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas ? this.canvas.getContext('2d') : null;
    this.inputs = inputs || {};
    this.init();
  }

  init() {
    if (!this.canvas) return;
    // Bind inputs
    Object.keys(this.inputs).forEach(key => {
      const el = document.getElementById(this.inputs[key]);
      if (el) {
        el.addEventListener('input', () => this.render());
      }
    });
    this.render();
  }

  render() {
    if (!this.ctx) return;
    const prenom = document.getElementById(this.inputs.prenom)?.value || 'Léon';
    const date = document.getElementById(this.inputs.date)?.value || '12.03.2026';
    const poids = document.getElementById(this.inputs.poids)?.value || '3.2kg — 50cm — 14h32';
    const message = document.getElementById(this.inputs.message)?.value || '';

    const w = this.canvas.width;
    const h = this.canvas.height;

    // Background cream
    this.ctx.fillStyle = '#FFFBF5';
    this.ctx.fillRect(0, 0, w, h);

    // Border
    this.ctx.strokeStyle = '#EDE6DC';
    this.ctx.lineWidth = 1;
    this.ctx.strokeRect(0, 0, w, h);

    // Prénom - serif large
    this.ctx.fillStyle = '#121212';
    this.ctx.font = 'bold 48px Georgia, serif';
    this.ctx.textAlign = 'center';
    this.ctx.fillText(prenom, w/2, h/2 - 20);

    // Date + poids - sans small caps
    this.ctx.font = '12px -apple-system, sans-serif';
    this.ctx.fillStyle = '#999';
    this.ctx.letterSpacing = '2px';
    this.ctx.fillText(`${date} — ${poids}`, w/2, h/2 + 20);

    // Message if exists
    if (message) {
      this.ctx.font = '14px Georgia, serif';
      this.ctx.fillStyle = '#666';
      this.ctx.fillText(message.slice(0, 40), w/2, h/2 + 50);
    }

    // Decorative line
    this.ctx.strokeStyle = '#EDE6DC';
    this.ctx.beginPath();
    this.ctx.moveTo(w/2 - 30, h/2 + 40);
    this.ctx.lineTo(w/2 + 30, h/2 + 40);
    this.ctx.stroke();

    // Footer
    this.ctx.font = '10px sans-serif';
    this.ctx.fillStyle = '#BBB';
    this.ctx.fillText('Affiche A4 — Design minimal — Impression haute qualité', w/2, h - 20);
  }

  // Export as image for POD
  exportAsDataURL() {
    return this.canvas ? this.canvas.toDataURL('image/png') : null;
  }

  // Generate PDF data (for print)
  generatePrintData() {
    return {
      prenom: document.getElementById(this.inputs.prenom)?.value || '',
      date: document.getElementById(this.inputs.date)?.value || '',
      poids: document.getElementById(this.inputs.poids)?.value || '',
      message: document.getElementById(this.inputs.message)?.value || '',
      preview: this.exportAsDataURL(),
      timestamp: new Date().toISOString()
    };
  }
}

// Ballon Bulle personnalisé preview
class BallonPreview {
  constructor() {
    this.prenomEl = document.getElementById('ballon-prenom');
    this.colorEl = document.getElementById('ballon-color');
    this.previewEl = document.getElementById('ballon-preview-text');
    this.init();
  }

  init() {
    if (!this.prenomEl) return;
    this.prenomEl.addEventListener('input', () => this.render());
    if (this.colorEl) this.colorEl.addEventListener('change', () => this.render());
    this.render();
  }

  render() {
    if (!this.previewEl) return;
    const prenom = this.prenomEl.value || 'Léon';
    const color = this.colorEl?.value || 'or';
    this.previewEl.textContent = prenom;
    this.previewEl.style.color = color === 'or' ? '#C9A86A' : color === 'rose' ? '#FF6B8A' : '#4FC3F7';
  }
}

// Auto-init on DOM load
document.addEventListener('DOMContentLoaded', () => {
  // Affiche
  new PersonalizationPreview('affiche-canvas', {
    prenom: 'input-prenom',
    date: 'input-date',
    poids: 'input-poids',
    message: 'input-message'
  });

  // Ballon
  new BallonPreview();

  // Bind add to cart with personalization data
  const forms = document.querySelectorAll('form[action="/cart/add"]');
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      const canvas = document.getElementById('affiche-canvas');
      if (canvas) {
        const dataInput = document.createElement('input');
        dataInput.type = 'hidden';
        dataInput.name = 'personalization_json';
        dataInput.value = JSON.stringify({
          prenom: document.getElementById('input-prenom')?.value || '',
          date: document.getElementById('input-date')?.value || '',
          message: document.getElementById('input-message')?.value || '',
          preview: canvas.toDataURL().slice(0, 100) + '...[truncated]'
        });
        form.appendChild(dataInput);
      }
    });
  });
});

// Confetti effect (existing)
function createConfetti(color, count) {
  count = count || 20;
  for (let i = 0; i < count; i++) {
    const el = document.createElement('div');
    el.style.position = 'fixed';
    el.style.left = Math.random() * 100 + 'vw';
    el.style.top = '-10px';
    el.style.width = '8px';
    el.style.height = '8px';
    el.style.background = color || '#C9A86A';
    el.style.borderRadius = '50%';
    el.style.pointerEvents = 'none';
    el.style.zIndex = '9999';
    el.style.animation = `fall ${2 + Math.random() * 2}s linear`;
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 4000);
  }
}

const style = document.createElement('style');
style.textContent = '@keyframes fall { to { transform: translateY(100vh) rotate(360deg); opacity:0 } }';
document.head.appendChild(style);
