/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html"],
  theme: {
    extend: {
      colors: {
        'white': '#FFFFFF',
        'offwhite': '#F5F5F7',
        'paper': '#FBF8F1',
        'text': '#1D1D1F',
        'muted': '#6E6E73',
        'border': '#E8E8ED',
        'accent': '#EFA12A',
        'confirm': '#137A6A',
        'accent-soft': '#FFF3DC',
        'confirm-soft': '#E8F4F1',
        'surface-warm': '#FBF8F1',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
      },
      maxWidth: {
        'hero': '1440px',
        'content': '1120px',
        'offer': '1280px',
        'faq': '920px',
        'reading': '720px',
      },
      spacing: {
        'section-desktop': '96px',
        'section-mobile': '72px',
      },
      borderRadius: {
        'card': '1rem',
        'large': '2rem',
        'xl': '2.5rem',
      },
      boxShadow: {
        'soft': '0 4px 20px rgba(0, 0, 0, 0.05)',
        'medium': '0 8px 30px rgba(0, 0, 0, 0.08)',
        'large': '0 16px 50px rgba(0, 0, 0, 0.1)',
      },
    },
  },
  plugins: [],
};
