# Warp Bubble Metric Ansatz - Documentation Site

This directory contains the GitHub Pages site for the Warp Bubble Metric Ansatz project.

## Setup

### Local Development

To run the site locally:

1. Install Jekyll and dependencies:
   ```bash
   gem install jekyll bundler
   bundle install
   ```

2. Serve the site:
   ```bash
   bundle exec jekyll serve
   ```

3. Open `http://localhost:4000` in your browser

### GitHub Pages Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the main branch. The site will be available at:
`https://your-username.github.io/warp-bubble-metric-ansatz/`

## Structure

- `index.html` - Main landing page
- `styles.css` - Custom CSS styles
- `script.js` - JavaScript functionality
- `_config.yml` - Jekyll configuration
- `assets/` - Images and other static assets

## Features

- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Mathematical Rendering**: Uses MathJax for LaTeX math expressions
- **Modern UI**: Clean, professional design with smooth animations
- **SEO Optimized**: Proper meta tags and structured data
- **Accessibility**: WCAG compliant design patterns

## Customization

### Colors and Theming

The main color scheme is defined in `styles.css`. Key colors:
- Primary: `#2563eb` (blue)
- Background: `#ffffff` (white)
- Text: `#1e293b` (dark gray)
- Light background: `#f8fafc`

### Content Updates

- Update the GitHub repository URLs in `index.html`
- Modify contact information and social links
- Add your organization name and branding

### Adding New Sections

To add new sections to the main page:

1. Add a new section in `index.html`
2. Update the navigation in the header
3. Add corresponding styles in `styles.css`
4. Update the smooth scrolling in `script.js`

## Dependencies

- **MathJax**: For mathematical equation rendering
- **Google Fonts**: Inter font family
- **Jekyll**: Static site generator (for GitHub Pages)

## Browser Support

- Chrome/Chromium 60+
- Firefox 60+
- Safari 12+
- Edge 79+

## Performance

The site is optimized for performance with:
- Minified CSS and JavaScript
- Optimized images
- Efficient font loading
- Minimal external dependencies
