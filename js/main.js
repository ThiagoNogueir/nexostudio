/* =========================================================
   NEXO STUDIO — main.js
   ========================================================= */

/* >>> Troque pelo número oficial do WhatsApp Business (DDI + DDD + número, só dígitos) */
const WHATSAPP_NUMBER = '5519996331656';

document.documentElement.classList.add('js');

const waLink = (msg) =>
  `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`;

/* ---------- Links de WhatsApp com mensagem pronta ---------- */
document.querySelectorAll('[data-wa]').forEach((el) => {
  el.href = waLink(el.dataset.wa);
  el.target = '_blank';
  el.rel = 'noopener';
});

/* ---------- Header ao rolar + botão flutuante ---------- */
const header = document.getElementById('header');
const waFloat = document.querySelector('.wa-float');
const onScroll = () => {
  const y = window.scrollY;
  header.classList.toggle('is-scrolled', y > 24);
  waFloat?.classList.toggle('is-visible', y > window.innerHeight * 0.6);
};
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

/* ---------- Menu mobile ---------- */
const burger = document.getElementById('burger');
const nav = document.getElementById('nav');
const setMenu = (open) => {
  burger.setAttribute('aria-expanded', String(open));
  burger.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
  nav.classList.toggle('is-open', open);
  document.body.classList.toggle('menu-open', open);
};
burger.addEventListener('click', () => setMenu(burger.getAttribute('aria-expanded') !== 'true'));
nav.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => setMenu(false)));
document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });
window.matchMedia('(min-width: 981px)').addEventListener('change', (e) => { if (e.matches) setMenu(false); });

/* ---------- Animações de entrada ---------- */
const reveals = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {
  // escalonamento leve entre irmãos
  const groups = new Map();
  reveals.forEach((el) => {
    const parent = el.parentElement;
    const i = groups.get(parent) || 0;
    el.style.setProperty('--d', `${Math.min(i, 6) * 0.08}s`);
    groups.set(parent, i + 1);
  });

  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  reveals.forEach((el) => io.observe(el));
} else {
  reveals.forEach((el) => el.classList.add('is-in'));
}

/* ---------- Link ativo no menu ---------- */
const links = [...document.querySelectorAll('.nav__link')];
const sections = links
  .map((l) => document.querySelector(l.getAttribute('href')))
  .filter(Boolean);
if ('IntersectionObserver' in window) {
  const spy = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      links.forEach((l) => l.classList.toggle('is-active', l.getAttribute('href') === `#${entry.target.id}`));
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  sections.forEach((s) => spy.observe(s));
}

/* ---------- Brilho que segue o mouse nos serviços ---------- */
document.querySelectorAll('.srv').forEach((row) => {
  row.addEventListener('pointermove', (e) => {
    const r = row.getBoundingClientRect();
    row.style.setProperty('--mx', `${e.clientX - r.left}px`);
  });
});

/* ---------- FAQ: abre um por vez ---------- */
const faqs = document.querySelectorAll('.qa');
faqs.forEach((d) => d.addEventListener('toggle', () => {
  if (d.open) faqs.forEach((o) => { if (o !== d) o.open = false; });
}));

/* ---------- Formulário → WhatsApp ---------- */
const form = document.getElementById('quote-form');
form?.addEventListener('submit', (e) => {
  e.preventDefault();
  const nome = form.nome.value.trim();
  const empresa = form.empresa.value.trim();
  const tipo = form.tipo.value;
  const msg = form.mensagem.value.trim();

  if (!nome) {
    form.nome.classList.add('is-invalid');
    form.nome.focus();
    return;
  }

  let text = `Olá, Nexo Studio! Meu nome é ${nome}`;
  if (empresa) text += `, da empresa ${empresa}`;
  text += `.\nTenho interesse em: ${tipo}.`;
  if (msg) text += `\n\n${msg}`;

  window.open(waLink(text), '_blank', 'noopener');
});
form?.nome.addEventListener('input', () => form.nome.classList.remove('is-invalid'));

/* ---------- Banner de Cookies (LGPD) ---------- */
const cookieBanner = document.getElementById('cookie-banner');
const cookieAccept = document.getElementById('cookie-accept');
const cookieEssential = document.getElementById('cookie-essential');
const openCookies = document.getElementById('open-cookies');
const COOKIE_KEY = 'nexo_cookie_consent';

const showCookieBanner = () => {
  if (!cookieBanner) return;
  cookieBanner.hidden = false;
  requestAnimationFrame(() => {
    cookieBanner.classList.add('is-active');
  });
};

const hideCookieBanner = (choice) => {
  if (!cookieBanner) return;
  if (choice) {
    try {
      localStorage.setItem(COOKIE_KEY, JSON.stringify({ choice, date: new Date().toISOString() }));
    } catch (err) {
      /* ignore storage quota / sandbox */
    }
  }
  cookieBanner.classList.remove('is-active');
  setTimeout(() => {
    cookieBanner.hidden = true;
  }, 400);
};

// Se o usuário ainda não escolheu, exibe após 900ms para uma entrada suave
const savedConsent = (() => {
  try {
    return localStorage.getItem(COOKIE_KEY);
  } catch (err) {
    return null;
  }
})();

if (!savedConsent) {
  setTimeout(showCookieBanner, 900);
}

cookieAccept?.addEventListener('click', () => hideCookieBanner('all'));
cookieEssential?.addEventListener('click', () => hideCookieBanner('essential'));
openCookies?.addEventListener('click', (e) => {
  e.preventDefault();
  showCookieBanner();
});

/* ---------- Ano no rodapé ---------- */
const year = document.getElementById('year');
if (year) year.textContent = new Date().getFullYear();
