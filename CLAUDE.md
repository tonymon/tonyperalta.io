# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a static portfolio website for Tony Peralta, an IT leader and AI engineer, hosted on GitHub Pages at tonyperalta.io. The site showcases professional experience, certifications, case studies, projects, and media appearances.

## Architecture & File Structure

### Core Files
- **`index.html`** - Production portfolio (742 lines, deployed live)
- **`staging.html`** - Development environment with staging banner (833 lines)
- **`styles.css`** - Shared CSS styles for both HTML files (1,782 lines)
- **`script.js`** - Shared JavaScript functionality (139 lines)
- **`STAGING-README.md`** - Comprehensive staging system documentation
- **`CNAME`** - Domain configuration for GitHub Pages (tonyperalta.io)
- **`pictures/`** - Image assets directory
  - `OpenPagePicture.png` - Hero section background (desert landscape)
  - `travel/` - Photo gallery images for "Beyond the Code" section

### Modular Architecture
The codebase uses a **decoupled architecture** for maintainability:
- **Shared Stylesheets**: `styles.css` contains all styling for both production and staging
- **Shared Scripts**: `script.js` contains interactive functionality (lightbox, filtering, smooth scrolling)
- **Staging-Specific CSS**: Only staging banner styles are inline in `staging.html`

### Dual-File System
**Production (`index.html`)**: Clean, optimized content ready for public deployment
**Staging (`staging.html`)**: Development environment with:
- Red staging banner at top
- All production content plus work-in-progress sections
- Testimonials section (ready but contains placeholder content)

## Key Features & Implementation

### 1. Hero Section Design
- **Background**: Full-width desert landscape (`pictures/OpenPagePicture.png`)
- **Layout**: Floating transparent overlay on right side of landscape
- **Mobile**: Background positioned at `22% center` to keep Tony visible
- **Text Effects**: White text with subtle shadow for desert/sky contrast
- **Components**: Introduction text, floating metrics cards, "Let's Connect" button

### 2. Floating Metrics Cards
- **Design**: Glass-morphism cards with icons, numbers, and descriptive subtitles
- **Content**: Professional metrics (15+ years experience, certifications, etc.)
- **Interactive**: Hover effects with tooltips for additional context
- **Mobile**: Responsive grid layout

### 3. Photo Gallery ("Beyond the Code")
- **Structure**: Responsive grid layout with lazy loading
- **Functionality**: Lightbox modal with keyboard navigation (arrow keys, ESC)
- **Images**: Travel photos showcasing personal interests
- **Performance**: Optimized loading and mobile touch interactions

### 4. Responsive Design
- **Breakpoints**: Mobile-first approach with desktop enhancements
- **Navigation**: Fixed header with blur effect and smooth scrolling
- **Sections**: Modular design with consistent spacing and typography
- **Mobile Hero**: Specific positioning to maintain visual impact

## Development Patterns

### CSS Architecture
- **Variables**: Consistent color scheme and spacing
- **Animations**: Subtle hover effects and floating animations
- **Glass-morphism**: `backdrop-filter: blur()` effects for modern UI
- **Grid Systems**: CSS Grid and Flexbox for responsive layouts

### JavaScript Features
- **Smooth Scrolling**: Navigation with scroll behavior
- **Modal System**: Lightbox with keyboard and click controls
- **Filtering**: Project portfolio with category filtering
- **Lazy Loading**: Performance optimization for images

### Mobile Optimization
- **Hero Background**: Position `22% center` for mobile visibility
- **Touch Interactions**: Swipe gestures and touch-friendly controls
- **Responsive Typography**: Scalable text and spacing
- **Performance**: Optimized images and efficient CSS

## Content Management

### Production-Ready Sections
- ✅ Expertise showcase
- ✅ AWS certifications (6 credentials)
- ✅ Case studies (3 detailed projects)
- ✅ Project portfolio with filtering
- ✅ Media & Speaking (5 major appearances)
- ✅ Beyond the Code photo gallery

### Staging-Only Content
- 🚧 Testimonials (waiting for real client feedback)
- 🚧 Additional sections in development

## Deployment Workflow

### GitHub Pages Setup
- **Domain**: tonyperalta.io (configured via CNAME)
- **Branch**: main (auto-deploys from commits to index.html)
- **Assets**: All images must be committed to repository

### Development Process
1. **Stage First**: Develop new features in `staging.html`
2. **Test Thoroughly**: Verify responsive design and functionality
3. **Move to Production**: Copy ready sections to `index.html`
4. **Deploy**: Commit changes to trigger GitHub Pages deployment

## Development Commands

### Local Development
```bash
# Serve locally (use any static server)
python -m http.server 8000
# or
npx serve .
# or
live-server
```

### File Management
```bash
# Make changes to shared styles
vim styles.css  # Changes affect both index.html and staging.html

# Add new images to gallery
cp new_image.jpg pictures/travel/
git add pictures/travel/new_image.jpg
```

### Testing Workflow
```bash
# Test staging environment
open staging.html  # or http://localhost:8000/staging.html

# Test production environment  
open index.html    # or http://localhost:8000/index.html

# Test mobile responsiveness (key breakpoint at 768px)
# Use browser dev tools or resize window
```

### Deployment
```bash
# Deploy to production (GitHub Pages auto-deploys)
git add index.html styles.css script.js
git commit -m "Update production site"
git push origin main
```

## Content Management Guidelines

### Development Process
1. **Always start in staging**: Make changes to `staging.html` first
2. **Test thoroughly**: Verify responsive design and functionality
3. **Update shared files**: Modify `styles.css` or `script.js` as needed
4. **Move to production**: Copy ready sections from staging to `index.html`
5. **Deploy**: Commit and push changes

### Photo Gallery Management
**Hard-coded image references**: Photo gallery uses manually defined image paths in HTML
- **To add photos**: Add images to `pictures/travel/` AND manually add HTML elements in both `index.html` and `staging.html`
- **Pattern**: `<div class="photo-item" data-image="path">` with matching `<img src="path">`
- **To remove photos**: Delete image file AND remove corresponding HTML elements from both files
- **Important**: Gallery count must stay synchronized between production and staging files

### Contact Information
- **Email**: Always use `tony@tonyperalta.io` for contact references
- **Professional Content**: Only include verifiable achievements and metrics

### Staging vs Production Differences
**Critical**: `staging.html` contains additional sections not in production:
- **Testimonials section**: Fully styled but contains placeholder content
- **Red staging banner**: Visual indicator for development environment
- **Navigation**: Includes "Testimonials" link in staging only

## Technical Architecture

### CSS Organization (`styles.css`)
- **Mobile-first responsive design** with `@media (max-width: 768px)` breakpoint
- **CSS Grid and Flexbox** for layout systems
- **Glass-morphism effects** using `backdrop-filter: blur()`
- **Component-based styling**: Each section has dedicated CSS classes
- **Animation keyframes**: Floating animations, hover effects, and transitions

### JavaScript Functionality (`script.js`)
- **Project and Media Filtering**: Dynamic content filtering with `.filter-btn` and `.media-filter-btn`
- **Photo Gallery Lightbox**: Full-screen modal with keyboard navigation (Arrow keys, ESC)
- **Smooth Scrolling**: Automatic scroll behavior for navigation links
- **Event Delegation**: Efficient event handling for interactive elements

### Mobile Optimization Critical Details
- **Hero Background Position**: Must be `22% center` on mobile to keep Tony visible in photo
- **Touch Interactions**: Photo gallery optimized for mobile touch/swipe
- **Responsive Grids**: Metrics change from 4-column to 2-column on mobile

## Technical Considerations

### Performance
- **Images**: Optimize file sizes for web delivery
- **CSS**: Efficient selectors and minimal reflow
- **JavaScript**: Lightweight interactions without heavy frameworks

### Browser Support
- **Modern Features**: backdrop-filter, CSS Grid, Flexbox
- **Fallbacks**: Graceful degradation for older browsers
- **Mobile**: iOS Safari and Android Chrome optimization

### SEO & Accessibility
- **Semantic HTML**: Proper heading hierarchy and landmarks
- **Alt Text**: Descriptive image alternatives
- **Meta Tags**: Professional title and description
- **Navigation**: Keyboard accessible with focus indicators

## Contact & Communication

- **Email**: tony@tonyperalta.io
- **Professional Focus**: IT leadership, AI engineering, federal consulting
- **Content Approach**: Factual, metrics-driven, professional tone

## Deployment & GitHub Pages

### Live Site
- **Production URL**: https://tonyperalta.io (auto-deploys from `main` branch)
- **GitHub Pages Source**: `main` branch, root directory
- **Custom Domain**: Configured via `CNAME` file

### File Dependencies
**Critical**: All assets must be committed to repository (no external CDNs)
- Images in `pictures/` directory are directly referenced in HTML
- `styles.css` and `script.js` are linked relatively from HTML files
- Changes to any file require git commit + push to deploy

## Content Status

### Production-Ready Sections (in `index.html`)
- ✅ Hero section with desert landscape background
- ✅ Professional metrics with tooltips
- ✅ Technical expertise showcase
- ✅ AWS certifications (6 credentials)
- ✅ Case studies (3 detailed projects with metrics)
- ✅ Project portfolio with filtering
- ✅ Media & Speaking (5 major appearances)
- ✅ Beyond the Code photo gallery (17 travel photos)

### Staging-Only Content (in `staging.html`)
- 🚧 **Testimonials section**: Fully built and styled, contains placeholder testimonials waiting for real client feedback

### Key Integration Points
- **Email Contact**: `tony@tonyperalta.io` used throughout site
- **Professional Tone**: Factual, metrics-driven content approach
- **Federal Focus**: Emphasizes government IT and AWS expertise
EOF < /dev/null