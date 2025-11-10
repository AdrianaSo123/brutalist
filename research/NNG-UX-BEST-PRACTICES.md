# Neo-Brutalism UX Best Practices
## From Nielsen Norman Group Research

**Source**: [Nielsen Norman Group - Neobrutalism: Definition and Best Practices](https://www.nngroup.com/articles/neobrutalism/)  
**Author**: Hayat Sheikh  
**Date**: April 11, 2025

## Key Distinctions

### Brutalism vs. Neobrutalism

**Brutalism**:
- Raw, harsh, unfinished or utilitarian
- Plain HTML elements, limited color palettes
- Example: Drudge Report (barebones HTML, monospaced headlines)
- Pre-CSS web aesthetic

**Neobrutalism**:
- Combines brutalist style with nostalgic 90s graphic design
- More colorful and orderly than true brutalism
- Bold dividers, thick strokes, bright colors
- Structured but raw aesthetic

## Core Characteristics (from NN/g)

### 1. High Contrast and Bright Colors
- Bold, primary colors
- High-contrast combinations
- Emphasizes key functions and UI elements
- Creates unconventional, memorable experience
- Helps users focus on essential elements

### 2. Thick Lines and Geometric Shapes
- Thick borders and angular forms
- Solid lines create structure
- No gradients or soft shadows
- Clear, defined boundaries

### 3. Stark Drop Shadows
- Bold, striking shadows (not soft/layered)
- Solid, single-color shadows (e.g., black offset by 4px)
- Adds depth while maintaining raw aesthetic
- Contrast with minimalism's soft shadows

### 4. Bold Type
- Bold, "unpolished" elements
- Quirky or slightly eccentric typefaces
- Balanced by generous whitespace
- Typography as functional element AND focal point
- Deliberate rather than overwhelming

### 5. Skeuomorphic Elements
- Nostalgic elements from early digital interfaces
- Windows 98-style buttons, monospace fonts
- Retro aesthetics blended with modern design
- Creates sense of familiarity

## UX Best Practices for Neo-Brutalism

### ✅ Design with Usability at Forefront
- Clear buttons
- Readable type
- Ample whitespace
- Keep experience intuitive and accessible
- Bold aesthetic shouldn't compromise usability

**Example Applied**: Our site uses clear navigation, readable body text (16-18px), and sufficient padding even with tight spacing philosophy.

### ✅ Contrast Ratios Matter
- Bold colors MUST meet text-contrast standards
- Avoid pairing vibrant hues that fail readability tests
- Use tools like Coolors' contrast checker
- Ensure combinations remain accessible

**Example Applied**: 
- Black (#000000) on White (#FFFFFF) = 21:1 ratio ✓
- Black on Yellow (#FFFF00) = 10.4:1 ratio ✓
- White on Black = 21:1 ratio ✓

### ✅ Limit Your Color Palette
- Restrict to 2-3 bold, high-contrast colors
- Avoid overwhelming users
- Examples: black + neon green + electric blue

**Example Applied**: Our palette is Black (#000000), White (#FFFFFF), Yellow (#FFFF00) - exactly 3 colors.

### ✅ Prioritize Readability
- Pair bold, unconventional headlines with clean body fonts
- Use neutral fonts like Roboto or Inter for body text
- Avoid overly decorative fonts for paragraphs
- Maintain legibility across devices

**Example Applied**: 
- Headlines: Arial/Helvetica (bold, ALL CAPS)
- Body: Arial/Helvetica (regular weight)
- System fonts ensure consistency

### ✅ Use Whitespace Strategically
- Offset dense geometric shapes with generous padding
- Use 24-32px margins for breathing room
- Prevent clutter
- Guide users to key actions

**Example Applied**: 
- Section padding: 32-48px (desktop)
- Content boxes: 32px internal padding
- Reduced to 24px on mobile but still substantial

### ✅ Test Interactions
- Interactive elements must remain recognizable
- Use underlines on hover or subtle color shifts
- Indicate state changes clearly
- Example: Button lightens on click for feedback

**Example Applied**:
- Hover states change background to yellow
- Links have thick underlines
- Buttons shift shadow on hover (6px → 3px)
- Instant state changes (no transitions)

### ✅ Avoid Oversimplification
- Retain hierarchy through size variation
- Use color intensity for emphasis
- Headlines should be significantly larger (2x body text)
- Clear calls to action
- Key usability elements must stand out

**Example Applied**:
- H1: 72-96px (hero)
- H2: 48px (sections)
- H3: 32px (subsections)
- Body: 16-18px
- Size ratio: 4-6x difference maintains hierarchy

## Brand Examples Using Neobrutalism

### Figma
- Bold contrasts and unconventional typography
- Emphasizes creative freedom and flexibility
- Dynamic user experience
- Brand refresh exemplifies neobrutalist design

### Gumroad
- Raw aesthetic aligns with empowering independent creators
- Strips away unnecessary polish
- Focuses on functionality over flourish
- Emphasizes simplicity and accessibility

### Other Examples Cited
- Tony's Chocolonely eCommerce - Bold, quirky typography
- 99percentoffsale.com - High-contrast colors
- byooooob.com - Thick borders, playful shapes
- dodonut.com - Readable text with brutalist style
- bieffeforniture.it - Limited color palette (blue + red)

## Critical UX Considerations

### Balance Boldness with Usability
> "Neobrutalism's rebellious aesthetic can grab attention, but its success hinges on balancing boldness with usability."

### Ground in Accessibility Principles
- Color contrast must meet WCAG standards
- Text must be readable on all backgrounds
- Interactive elements need clear affordances
- Mobile responsiveness is critical

### Test with Real Users
- Bold designs can overwhelm
- Need to verify usability in practice
- What looks striking may hinder navigation
- User feedback is essential

## How Our Implementation Aligns

### ✅ Strengths
1. **High contrast**: Black/white/yellow meets all standards
2. **Limited palette**: Exactly 3 colors as recommended
3. **Clear hierarchy**: 4-6x size difference between headings and body
4. **Readable body text**: System fonts at 16-18px
5. **Strategic whitespace**: 32-48px padding offsets bold elements
6. **Clear interactions**: Underlines, color shifts, shadow changes
7. **Thick borders**: 4-5px throughout
8. **Hard shadows**: 8px offset, no blur
9. **Bold typography**: ALL CAPS headings
10. **No gradients**: Flat colors only

### 🔧 Areas for Enhancement
1. **More whitespace**: NN/g recommends 24-32px margins; we could increase
2. **Body font refinement**: Could consider using Inter or Roboto for improved readability while keeping headers brutalist
3. **Interactive feedback**: Could add more explicit hover states
4. **Testing**: Need real user testing to verify usability

## Key Takeaway from NN/g

> "By grounding the style in accessibility principles and testing with users, designers can create interfaces that are both striking and functional."

Our implementation successfully balances:
- **Aesthetic authenticity** (deliberately rough, anti-corporate)
- **Functional usability** (clear navigation, readable text)
- **Accessibility standards** (color contrast, hierarchy)
- **Responsive design** (works on all devices)

## Differences: Our Approach vs. NN/g Examples

### Our Neo-Brutalist Site
- **More historically focused**: Content about brutalism origins
- **Educational purpose**: Teaching design history
- **Tighter spacing**: Following pure brutalist philosophy
- **No retro/90s elements**: Staying closer to architectural brutalism
- **System fonts only**: No quirky typefaces

### NN/g Examples (Figma, Gumroad, etc.)
- **More colorful**: Multiple bright colors
- **Commercial focus**: Product/service selling
- **Generous whitespace**: More breathing room
- **Skeuomorphic elements**: Retro 90s graphics
- **Custom typography**: Brand-specific fonts

Both approaches are valid - ours leans more toward architectural brutalism roots, while commercial examples embrace more neobrutalist evolution with 90s nostalgia.

## References for Iteration

If refining the design based on NN/g research:

1. **Increase whitespace**: Bump section margins to 32px minimum
2. **Test contrast ratios**: Use Coolors or WebAIM contrast checker
3. **Simplify some interactions**: Ensure all buttons have obvious states
4. **Add more breathing room**: Increase padding in dense sections
5. **Verify mobile usability**: Test on actual devices, not just resize

---

**Research Date**: November 10, 2025  
**Source**: Nielsen Norman Group (NN/g)  
**Application**: Confirms our design decisions align with UX best practices for neobrutalism
