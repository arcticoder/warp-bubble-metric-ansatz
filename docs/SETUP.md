# GitHub Pages Setup Instructions

Your GitHub Pages site is now ready! Here's how to enable it:

## Enable GitHub Pages

1. Go to your repository on GitHub: https://github.com/arcticoder/warp-bubble-metric-ansatz
2. Click on **Settings** tab
3. Scroll down to **Pages** section in the left sidebar
4. Under **Source**, select "Deploy from a branch"
5. Choose **main** branch and **/docs** folder
6. Click **Save**

## Your Site URL

Once enabled, your site will be available at:
**https://arcticoder.github.io/warp-bubble-metric-ansatz/**

## Features

✅ **Responsive Design** - Works on all devices  
✅ **Mathematical Rendering** - MathJax for LaTeX equations  
✅ **Modern UI** - Clean, professional appearance  
✅ **SEO Optimized** - Proper meta tags and descriptions  
✅ **Demo Page** - Shows generated PDF and LaTeX source  
✅ **GitHub Actions** - Automatic deployment  

## File Structure

```
docs/
├── index.html          # Main homepage
├── demo.html           # Demo page with PDF viewer
├── styles.css          # All styling
├── script.js           # Interactive functionality  
├── _config.yml         # Jekyll configuration
├── Gemfile             # Ruby dependencies
├── assets/
│   ├── favicon.svg     # Site icon
│   └── images/         # Image assets
└── README.md           # This file
```

## Local Development

To run the site locally:

```bash
cd docs
bundle install
bundle exec jekyll serve
```

Visit `http://localhost:4000` to see your site.

## Customization

- Update repository URLs in `index.html` if needed
- Add images to `assets/images/` folder
- Modify colors in `styles.css`
- Update content in `index.html` and `demo.html`

## Automatic Updates

The site will automatically update whenever you:
1. Push changes to the main branch
2. Modify files in the `docs/` folder  
3. Update the generated `metric_ansatz.pdf` file

The GitHub Actions workflow handles the deployment automatically.
