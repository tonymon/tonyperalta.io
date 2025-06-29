# CLAUDE.md - Portfolio Development Guide

This document provides context and guidance for Claude Code instances working on Tony Peralta's portfolio website.

## Repository Overview

This is a static portfolio website for Tony Peralta, an IT leader and AI engineer, hosted on GitHub Pages at tonyperalta.io. The site showcases professional experience, certifications, case studies, projects, and media appearances.

## Architecture & File Structure

### Core Files
- **`index.html`** - Production portfolio (deployed live)
- **`staging.html`** - Development environment with staging banner
- **`STAGING-README.md`** - Comprehensive staging system documentation
- **`CNAME`** - Domain configuration for GitHub Pages
- **`pictures/`** - Image assets directory
  - `OpenPagePicture.png` - Hero section background (desert landscape)
  - `travel/` - Photo gallery images for "Beyond the Code" section

### Dual-File System
The repository uses a staging/production workflow:
- **Production (`index.html`)**: Only production-ready content
- **Staging (`staging.html`)**: Development environment with red banner, includes all sections plus work-in-progress content like testimonials

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

## Common Tasks & Commands

### Image Management
```bash
# Add new images to repository
git add pictures/
git commit -m "Add new images"
git push
```

### Mobile Testing
- Test hero section background positioning
- Verify touch interactions in photo gallery
- Check navigation and button accessibility

### Content Updates
- **Contact Info**: Use `tony@tonyperalta.io` for all contact references
- **Staging Banner**: Maintain red banner in staging.html for visual distinction
- **Professional Content**: Only include verifiable achievements and metrics

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

## Future Development Notes

- **Testimonials**: Ready to activate when real client feedback is available
- **Case Studies**: Template established for additional project showcases
- **Media Section**: Expandable for new speaking engagements and coverage
- **Photo Gallery**: Easily updatable with new travel/personal content

This documentation ensures consistent development approaches and maintains the professional quality and performance standards established for the portfolio.
EOF < /dev/null