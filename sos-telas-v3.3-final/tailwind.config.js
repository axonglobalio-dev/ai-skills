/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html"],
  theme: {
    extend: {
      colors: {
        white: '#FFFFFF',
        offwhite: '#F5F5F7',
        paper: '#FBF8F1',
        text: '#1D1D1F',
        muted: '#6E6E73',
        border: '#E8E8ED',
        accent: '#EFA12A',
        confirm: '#137A6A',
        'accent-soft': '#FFF3DC',
        'confirm-soft': '#E8F4F1',
        'surface-warm': '#FBF8F1',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
      },
      maxWidth: {
        'content': '1120px',
        'hero': '1440px',
        'offer': '1280px',
        'faq': '920px',
        'reading': '720px',
      },
      spacing: {
        'section-desktop': '96px',
        'section-mobile': '72px',
      },
    },
  },
  plugins: [],
}
