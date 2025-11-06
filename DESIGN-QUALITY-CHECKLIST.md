# Design Quality Checklist
## Section-by-Section Review Tool

# Design Quality Checklist
## Review Framework for Every Section

**Project:** Swiss Design Lineage Vibe Coding  
**Purpose:** Systematic quality review before moving forward

---

## 🎯 How to Use This Checklist

**During Phase 4 (Build & Iterate):**
- Take screenshot of section
- Review using this checklist
- Share findings with AI
- Iterate until criteria met
- Check off completed items

**Minimum 2-3 review cycles per section.**

---

## 📸 Screenshot Workflow

**Before Every Review:**

1. **Full Desktop Screenshot** (1920px width)
   - Chrome DevTools: Toggle device toolbar OFF
   - Capture entire section in context

2. **Tablet Screenshot** (768px width)
   - Chrome DevTools: Responsive mode
   - Set width to 768px exactly
   - Capture same section

3. **Mobile Screenshot** (375px width)
   - Chrome DevTools: iPhone SE preset
   - Portrait orientation
   - Capture same section

**Share all three with AI before review.**

---

## 🏠 Hero Section Review

### Visual Hierarchy
- [ ] Main heading immediately draws attention
- [ ] Hierarchy clear: heading → subheading → CTA
- [ ] Eye path flows naturally top to bottom
- [ ] Nothing competes with main message

### Typography
- [ ] Heading size appropriate for style (check design system)
- [ ] Body text readable at all sizes (minimum 16px)
- [ ] Line height prevents cramping (check style guide)
- [ ] Font choices authentic to style
- [ ] Text has adequate contrast (4.5:1 minimum)

### Layout & Spacing
- [ ] Content centered or aligned per style rules
- [ ] Whitespace (or lack thereof) matches style
- [ ] Padding consistent with design system
- [ ] Asymmetry intentional (if applicable)
- [ ] Grid structure visible/hidden per style

### Color Usage
- [ ] Color choices match style palette
- [ ] Accent colors used strategically (not randomly)
- [ ] Background/foreground contrast passes WCAG
- [ ] Color meaning consistent throughout site

### Responsive Behavior
- [ ] **Desktop (1920px):** Spacious, makes good use of width
- [ ] **Tablet (768px):** Adapts gracefully, nothing squished
- [ ] **Mobile (375px):** Stacks properly, text remains readable
- [ ] Touch targets minimum 44×44px (mobile)
- [ ] Headings don't overflow or break awkwardly

### Style Authenticity
- [ ] Feels like authentic [STYLE], not generic
- [ ] Avoids common style mistakes (see style guide)
- [ ] Key characteristics clearly visible
- [ ] Not trying to please everyone (bold choices)

### Prompt to AI (if issues found):
```
Hero section review—I found these issues:
- [List specific problems]
- Screenshot: [paste image]

Please refine the hero section to address these. Reference our design system and [STYLE] principles.
```

---

## 🧭 Navigation Review

### Structure & Clarity
- [ ] Menu items clearly labeled
- [ ] Item order logical (expected pattern)
- [ ] Current page indicated (active state)
- [ ] Logo/site title present and clickable

### Visual Design
- [ ] Navigation style matches overall design
- [ ] Links clearly distinguishable
- [ ] Hover/focus states visible
- [ ] Spacing between items appropriate
- [ ] Alignment consistent

### Functionality
- [ ] All links work (no 404s)
- [ ] Dropdown menus (if any) accessible
- [ ] Keyboard navigation works (Tab, Enter)
- [ ] Focus indicators visible
- [ ] Mobile menu icon clear (hamburger, etc.)

### Mobile Behavior
- [ ] **Desktop:** Horizontal/full menu visible
- [ ] **Tablet:** May collapse to hamburger or stay visible
- [ ] **Mobile:** Hamburger menu required
- [ ] Mobile menu opens/closes smoothly
- [ ] Mobile menu items large enough to tap (44px)
- [ ] Close button obvious in mobile menu

### Accessibility
- [ ] Nav wrapped in `<nav>` landmark
- [ ] Links have descriptive text (not "click here")
- [ ] ARIA labels if needed (mobile menu button)
- [ ] Focus order logical (top to bottom)
- [ ] No keyboard traps

### Style Authenticity
- [ ] Navigation design reflects [STYLE] principles
- [ ] Not defaulting to generic Bootstrap nav
- [ ] Intentional about visibility/prominence
- [ ] Matches style guide recommendations

### Prompt to AI (if issues found):
```
Navigation review—I found these issues:
- [List specific problems]
- Screenshot: [paste desktop + mobile images]

Please refine the navigation to address these. Ensure mobile menu works properly and style matches our [STYLE] design system.
```

---

## 📝 Content Sections Review

**Use for:** About, Blog posts, Project pages, any content-heavy section

### Readability
- [ ] Line length not too wide (45-75 characters ideal)
- [ ] Paragraph spacing clear (not wall of text)
- [ ] Headings break up content (H2, H3 hierarchy)
- [ ] Lists used appropriately (bullets, numbered)
- [ ] Text-to-background contrast sufficient (4.5:1)

### Typography
- [ ] Body text minimum 16px
- [ ] Line height comfortable (1.5-1.75 for body)
- [ ] Heading sizes create clear hierarchy
- [ ] Font choices consistent with style
- [ ] Bold/italic used for emphasis (not color alone)

### Layout
- [ ] Content width contained (not full-bleed unless intentional)
- [ ] Margins/padding create breathing room
- [ ] Images integrated well (not awkwardly placed)
- [ ] Grid structure matches design system
- [ ] Alignment intentional (left/center/justified)

### Images & Media
- [ ] Images add value (not decorative filler)
- [ ] Alt text descriptive and meaningful
- [ ] Images responsive (scale on mobile)
- [ ] Aspect ratios maintained (no stretching)
- [ ] Lazy loading for performance (if many images)

### Links & CTAs
- [ ] Links clearly distinguishable from body text
- [ ] Hover states visible
- [ ] Buttons styled consistently
- [ ] CTA placement strategic (end of section)
- [ ] External links marked (icon or indication)

### Responsive Behavior
- [ ] **Desktop:** Multi-column if appropriate
- [ ] **Tablet:** May collapse to single column
- [ ] **Mobile:** Single column, images stack
- [ ] Text remains readable (no tiny fonts)
- [ ] Touch targets adequate (buttons, links)

### Style Authenticity
- [ ] Content styling matches [STYLE] principles
- [ ] Spacing decisions intentional (tight vs. generous)
- [ ] Visual treatment reinforces style
- [ ] Consistency across all content sections

### Prompt to AI (if issues found):
```
Content section review—I found these issues:
- Section: [name, e.g., "About page"]
- Issues: [list specific problems]
- Screenshot: [paste image]

Please refine this content section to improve readability and match our [STYLE] design system.
```

---

## 🦶 Footer Review

### Content & Structure
- [ ] Contact information present
- [ ] Social links (if applicable)
- [ ] Copyright notice with current year
- [ ] Secondary navigation (if needed)
- [ ] Attribution (Eleventy, template source)

### Visual Design
- [ ] Footer clearly separated from content
- [ ] Background color/style distinct
- [ ] Text readable (contrast check)
- [ ] Icon size appropriate
- [ ] Alignment consistent

### Layout
- [ ] Multi-column layout (if desktop allows)
- [ ] Spacing consistent with design system
- [ ] Not too tall (doesn't dominate page)
- [ ] Padding adequate (not cramped)

### Links & Functionality
- [ ] All links work
- [ ] Social icons link to profiles
- [ ] Email link uses `mailto:`
- [ ] External links open appropriately
- [ ] Hover states visible

### Responsive Behavior
- [ ] **Desktop:** Multi-column layout
- [ ] **Tablet:** May collapse to fewer columns
- [ ] **Mobile:** Single column, stacked
- [ ] Social icons remain tappable (44px)
- [ ] Copyright text doesn't overflow

### Accessibility
- [ ] Footer wrapped in `<footer>` landmark
- [ ] Links have descriptive text
- [ ] Color not only indicator (underlines, icons)
- [ ] Focus indicators visible
- [ ] Keyboard accessible

### Style Authenticity
- [ ] Footer design matches overall style
- [ ] Not generic template footer
- [ ] Intentional about visibility/subtlety
- [ ] Consistent with style guide

### Prompt to AI (if issues found):
```
Footer review—I found these issues:
- [List specific problems]
- Screenshot: [paste image]

Please refine the footer to address these and match our [STYLE] design system.
```

---

## 🎨 Overall Design Consistency Review

**Run this AFTER building all sections (before final QA):**

### Visual Consistency
- [ ] Color palette consistent across all pages
- [ ] Typography scale consistent (headings, body)
- [ ] Spacing system consistent (margins, padding)
- [ ] Component styling consistent (buttons, cards, etc.)
- [ ] Grid structure consistent

### Interaction Consistency
- [ ] Hover states consistent (links, buttons)
- [ ] Focus indicators consistent
- [ ] Transitions/animations consistent (if any)
- [ ] Loading states consistent (if applicable)

### Content Consistency
- [ ] Heading hierarchy consistent (H1→H2→H3)
- [ ] Tone consistent (formal, casual, playful)
- [ ] Image treatment consistent (borders, shadows, etc.)
- [ ] Lists formatted consistently

### Style Authenticity
- [ ] Every section feels authentically [STYLE]
- [ ] No sections feel generic or template-like
- [ ] Bold choices maintained throughout
- [ ] Avoids common style mistakes consistently

### Prompt to AI (if issues found):
```
Overall consistency review—I found these inconsistencies:
- [List specific issues across sections]
- Screenshots: [paste images showing inconsistencies]

Please review our design system documentation and ensure all sections follow the same rules consistently.
```

---

## ♿ Accessibility Spot Check

**Run this for EACH section:**

### Color Contrast
- [ ] Text-to-background: 4.5:1 minimum (normal text)
- [ ] Text-to-background: 3:1 minimum (large text 24px+)
- [ ] Link color different from body text
- [ ] Focus indicators visible (3:1 contrast)

**Tool:** Use browser DevTools or WebAIM Contrast Checker

### Keyboard Navigation
- [ ] Can Tab through all interactive elements
- [ ] Tab order logical (top to bottom, left to right)
- [ ] Focus indicators visible at all times
- [ ] Can activate with Enter or Space
- [ ] No keyboard traps (can Tab out)

**Test:** Unplug mouse, navigate with keyboard only

### Screen Reader Compatibility
- [ ] Headings create logical outline (H1→H2→H3)
- [ ] Landmarks used (`<nav>`, `<main>`, `<footer>`)
- [ ] Images have meaningful alt text
- [ ] Links have descriptive text
- [ ] Form labels associated with inputs

**Tool:** Use NVDA (Windows) or VoiceOver (Mac)

### Semantic HTML
- [ ] Using proper elements (`<button>`, not `<div onclick>`)
- [ ] Lists use `<ul>` or `<ol>`, not `<div>` with bullets
- [ ] Headings in logical order (don't skip levels)
- [ ] `<main>` landmark wraps primary content

### Touch Targets (Mobile)
- [ ] All interactive elements minimum 44×44px
- [ ] Adequate spacing between touch targets
- [ ] Buttons large enough to tap accurately

### Prompt to AI (if issues found):
```
Accessibility issues in [section name]:
- [List specific WCAG failures]
- Contrast ratios that fail
- Keyboard navigation problems
- Missing ARIA labels or landmarks

Please fix these accessibility issues while maintaining our [STYLE] design.
```

---

## 🚀 Performance Quick Check

**Run during build iterations:**

### Image Optimization
- [ ] Images compressed (not 5MB JPGs)
- [ ] Appropriate formats (WebP for modern browsers)
- [ ] Lazy loading enabled (below fold)
- [ ] Responsive images (`srcset`, `sizes`)

### Code Efficiency
- [ ] No unused CSS (PurgeCSS with Tailwind)
- [ ] No console errors in browser
- [ ] Minimal JavaScript (if any)
- [ ] Build completes successfully

### Lighthouse Check
- [ ] Run Lighthouse in Chrome DevTools
- [ ] Performance: 90+ target
- [ ] Accessibility: 90+ target
- [ ] Best Practices: 90+ target
- [ ] SEO: 90+ target

**How:** Chrome DevTools → Lighthouse tab → Generate report

### Prompt to AI (if issues found):
```
Performance issues:
- Lighthouse scores: [paste scores]
- Specific issues: [list problems from report]

Please optimize performance while maintaining our design. Focus on [specific metric, e.g., "First Contentful Paint" or "Accessibility score"].
```

---

## 🔍 Using AI as Expert Reviewers

**Leverage AI's different perspectives:**

### UX Designer Review
```
Act as an expert UX designer reviewing this [section name] section. 
Screenshot: [paste image]

Review for:
- Visual hierarchy
- User flow
- Interaction clarity
- Mobile usability
- Accessibility

What works well? What needs improvement?
```

### Accessibility Specialist Review
```
Act as a WCAG 2.1 AA accessibility specialist reviewing this [section].
Screenshot: [paste image]

Audit for:
- Color contrast
- Keyboard navigation
- Screen reader compatibility
- Touch target sizes
- Semantic HTML

What accessibility issues do you see?
```

### Style Expert Review
```
Act as a [STYLE] design expert reviewing this section.
Screenshot: [paste image]

Does this authentically represent [STYLE] principles?
- What feels authentic?
- What feels generic?
- What common mistakes am I making?
- How can I push the style further?
```

### Literary Critic Review (for content)
```
Act as a literary critic reviewing the writing on this page.
Screenshot: [paste image]

Review:
- Clarity and readability
- Tone consistency
- Grammar and style
- Content structure

What works? What needs revision?
```

---

## 📋 Master Review Checklist

**Use this before marking Phase 4 complete:**

### All Sections Reviewed
- [ ] Hero section reviewed 2-3 times
- [ ] Navigation reviewed 2-3 times
- [ ] All content sections reviewed 2-3 times each
- [ ] Footer reviewed 2-3 times
- [ ] Overall consistency checked

### All Devices Tested
- [ ] Desktop (1920px) looks great
- [ ] Tablet (768px) adapts well
- [ ] Mobile (375px) fully functional
- [ ] Touch targets adequate on mobile

### Accessibility Verified
- [ ] All sections pass color contrast
- [ ] Keyboard navigation works everywhere
- [ ] Screen reader compatible
- [ ] Semantic HTML throughout
- [ ] ARIA labels where needed

### Performance Validated
- [ ] Lighthouse scores 90+ (all metrics)
- [ ] Images optimized
- [ ] Build succeeds with no errors
- [ ] No console errors

### Style Authenticity Confirmed
- [ ] Every section feels authentically [STYLE]
- [ ] Avoids common style mistakes
- [ ] Bold choices maintained
- [ ] Design system followed consistently

### Quality Gates Passing
- [ ] Prettier formatting succeeds
- [ ] ESLint passes (zero errors)
- [ ] Stylelint passes (zero errors)
- [ ] Pre-commit hooks working
- [ ] GitHub Actions CI/CD passing

### Ready for Phase 5
- [ ] All above criteria met
- [ ] No known issues remaining
- [ ] Screenshots documented
- [ ] Time tracking updated

---

## 💡 Pro Tips

**Don't Skip Mobile:**
Mobile reviews catch 80% of responsive issues. Always test mobile for every iteration.

**Use Three-Pass System:**
1. **Broad:** Overall impression, major issues
2. **Specific:** Section-by-section using this checklist
3. **Details:** Typography, spacing, consistency

**Trust Your Gut:**
If something feels wrong but you can't articulate why, screenshot it and ask AI: "This feels off to me. What might be causing that?"

**Iterate Boldly:**
First iteration usually too safe. Second iteration pushes style further. Third iteration refines the bold choices.

**Document Everything:**
Keep screenshots from each iteration. Your collaboration story will need them.

---

**Document Version:** 1.0  
**Last Updated:** November 5, 2025  
**Project:** Swiss Design Lineage Vibe Coding  
**Instructor:** Keith Williams, NJIT
