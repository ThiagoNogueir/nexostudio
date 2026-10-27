# Nexo Studio — Sites que Conectam e Convertem ✦

Site oficial da **Nexo Studio**, agência especializada em criação de sites institucionais, landing pages e redesigns de alta conversão para pequenas e médias empresas.

🌐 **Identidade visual**:
- **Azul Principal**: `#2563EB` (Confiança · Tecnologia · Crescimento)
- **Preto**: `#0B0F14` (Sofisticação · Elegância · Profissionalismo)
- **Cinza**: `#6B7280` (Equilíbrio · Modernidade · Apoio)
- **Branco**: `#F8FAFC` (Limpeza · Clareza · Simplicidade)
- **Tipografia**: Montserrat

---

## 🚀 Funcionalidades

- **100% Responsivo**: Layout fluido otimizado para celulares, tablets e desktops (Mobile-First).
- **Hero Interativo**: Mockups visuais em CSS puro simulando site e aplicativo mobile.
- **Seção de Cases**: Estrutura modular preparada para receber prints/cases de sucesso reais.
- **Tabela de Pacotes & Manutenção**: Apresentação clara de preços e planos recorrentes com link direto para o WhatsApp.
- **Formulário com Conversão Direta**: Integração automática com WhatsApp Business com dados preenchidos.
- **Consentimento de Cookies (LGPD)**: Banner moderno e discreto com opções de aceitar e gerenciar preferências via `localStorage`.
- **Animações de Entrada**: Revelações suaves via `IntersectionObserver` com respeito a `prefers-reduced-motion`.

---

## 📁 Estrutura de Arquivos

```
nexo/
├── index.html        # Estrutura semântica completa
├── css/
│   └── style.css     # Design system, tokens e componentes
├── js/
│   └── main.js       # Interações, WhatsApp, animações e cookies
├── assets/
│   └── favicon.svg   # Favicon com o símbolo oficial da marca
├── .gitignore
└── README.md
```

---

## ⚡ Como Rodar Localmente

Basta abrir o arquivo `index.html` em qualquer navegador ou rodar um servidor estático local:

```bash
# Com Python 3
python -m http.server 3000

# Ou com Node.js
npx serve .
```

---

## 🌐 Deploy na Vercel

Este projeto é um site estático puro (HTML, CSS e JS modernos). Para colocar no ar na **Vercel**:
1. Conecte sua conta do GitHub na Vercel.
2. Importe o repositório `nexostudio`.
3. Mantenha as configurações padrão (Framework Preset: *Other*) e clique em **Deploy**.
