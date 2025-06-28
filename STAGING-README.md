# Portfolio Staging System

This repository uses a dual-file system to manage content development and production deployment.

## File Structure

### `index.html` - Production Site
- **Purpose**: Live portfolio deployed at tonyperalta.io
- **Content**: Only production-ready sections
- **Updates**: Only commit changes that are ready for public viewing
- **Current Sections**:
  - ✅ Expertise
  - ✅ Certifications  
  - ✅ Case Studies
  - ✅ Projects
  - ✅ Media & Speaking

### `staging.html` - Development Environment
- **Purpose**: Testing ground for new sections and content
- **Content**: All sections including work-in-progress
- **Access**: Local development only (not deployed publicly)
- **Visual Indicator**: Red staging banner at top
- **Current Sections**:
  - ✅ All production sections
  - 🚧 Testimonials (ready for when you have real testimonials)
  - 🚧 Future sections in development

## Development Workflow

### Adding New Content
1. **Develop in staging.html**: Add new sections, test functionality
2. **Review and refine**: Polish content and styling in staging
3. **Test thoroughly**: Ensure responsive design and functionality
4. **Move to production**: Copy ready sections to index.html
5. **Deploy**: Commit index.html changes to go live

### Working with Testimonials
The testimonials section is fully built and styled, ready for when you have:
- Real client testimonials and quotes
- Permission to use client names and titles
- Actual project references

To activate testimonials:
1. Copy testimonials section from staging.html to index.html
2. Update navigation menu to include testimonials link
3. Replace placeholder content with real testimonials
4. Commit and deploy

## Best Practices

### Staging Development
- Always test new features in staging.html first
- Use the staging banner to remind yourself it's not production
- Feel free to experiment with layout and content
- Keep staging.html up to date with production changes

### Production Deployment
- Only move content to index.html when completely ready
- Test all links and functionality before committing
- Ensure mobile responsiveness is working
- Verify all content is accurate and professional

### Content Guidelines
- **Production**: Only include content you can substantiate
- **Staging**: Feel free to create placeholder content for testing
- **Testimonials**: Wait for real client feedback before going live
- **Case Studies**: Ensure all metrics and details are accurate

## File Maintenance

### Keeping Staging Current
When updating production (index.html), also update staging.html to keep them in sync:
```bash
# After updating index.html
cp index.html staging.html
# Then re-add staging banner and any staging-only sections
```

### Emergency Rollback
If needed, you can quickly revert to a previous version:
```bash
git checkout HEAD~1 index.html  # Rollback to previous version
git commit -m "Emergency rollback"
git push
```

## Current Status

### Ready for Production ✅
- Hero section with professional metrics
- Expertise showcase with technical skills
- AWS certifications and credentials
- Detailed case studies with real metrics  
- Project portfolio with filtering
- Media & Speaking appearances with real coverage

### In Staging 🚧
- Testimonials section (waiting for real testimonials)
- Additional sections as they're developed

This system allows you to maintain a professional, accurate public portfolio while having the flexibility to develop and test new content privately.