# Research Sources & Design Influences
## Neo-Brutalist Design Gallery Project

**Created**: November 10, 2025  
**Project**: Swiss Design Lineage - Brutalist Style  
**Course**: IS 218 - Building Web Applications, NJIT

---

## Primary Research Sources

### 1. Nielsen Norman Group (NN/g)
**URL**: https://www.nngroup.com/articles/neobrutalism/  
**Author**: Hayat Sheikh  
**Date**: April 11, 2025  
**Type**: UX research and best practices

#### Key Insights Used:
- **Brutalism vs. Neobrutalism distinction**
  - Brutalism = raw, utilitarian (Drudge Report, Craigslist)
  - Neobrutalism = brutalism + 90s graphic design nostalgia
  - Applied: Clarified our site as NEO-BRUTALISM specifically

- **6 UX Best Practices**:
  1. ✓ Design with usability at forefront
  2. ✓ Contrast ratios matter (WCAG standards)
  3. ✓ Limit color palette (2-3 bold colors)
  4. ✓ Prioritize readability
  5. ✓ Use whitespace strategically
  6. ✓ Test interactions clearly

- **Color Contrast Standards**:
  - Black on White: 21:1 ratio ✓
  - Black on Yellow: 10.4:1 ratio ✓
  - Applied: Used contrast checker to verify all combinations

- **Real-World Examples**:
  - Figma: Bold contrasts, unconventional typography
  - Gumroad: Raw aesthetic, functionality over flourish
  - Applied: Referenced these as successful neo-brutalist implementations

#### How This Influenced Our Design:
- Added `about.html` section on UX best practices
- Verified all color contrast ratios meet WCAG standards
- Balanced boldness with readability (16-18px body text)
- Used strategic whitespace (32-48px padding) despite tight philosophy
- Created clear button states with thick underlines
- Emphasized distinction between brutalism and neo-brutalism throughout site

---

### 2. Medium Article by Sepideh Yazdi
**URL**: https://medium.com/@sepidy/how-can-i-design-in-the-neo-brutalism-style-d85c458042de  
**Author**: Sepideh Yazdi (@sepidy)  
**Date**: February 11, 2023  
**Type**: Practical design tutorial with cheat sheet

#### Key Insights Used:

##### Color Guidelines:
- **Black**: Pitch black (#000000) with no fear - for strokes and dark shadows
- **Vibrant colors**: High saturation colors allowed
- **Vintage and muted colors**: Old magazine/poster aesthetic
- **No gradients**: Colors are distinct, no different tones
- **Background colors**: Can use vibrant colors (not just white/gray)

Applied:
```css
:root {
    --color-black: #000000;
    --color-white: #FFFFFF;
    --color-yellow: #FFFF00;  /* Vibrant, unrefined */
}
```

##### Components:
- **Raw, unrefined shapes**: Circles, rectangles, stars, polygons with strokes
- **Thick borders**: Define spaces with cards that have strokes
- **Hard shadows**: Both X and Y offset, no blur, black at 100% opacity
- **Drop shadow formula**: `box-shadow: 8px 8px 0 #000000` (X offset, Y offset, 0 blur)

Applied:
```css
.brutal-button {
    border: 4px solid #000000;
    box-shadow: 8px 8px 0 #000000;
}
```

##### Typography:
- **Sans-serif**: More popular in this style
- **Large font sizes**: For headings
- **Experiment with line height and letter spacing**
- **Typography as decorative element**: Especially on websites
- **Example fonts**: Lexend Mega, Public Sans, Mabry Pro, Archivo Black, Bebas Kai

Applied:
- Used system sans-serif fonts (Arial/Helvetica)
- Heading sizes: 72-96px (hero), 48px (h2), 32px (h3)
- Tight line-height: 1.2-1.4
- ALL CAPS for decorative impact

##### 3 Categories Framework:
1. **Color** ✓
2. **Components** ✓
3. **Typography** ✓

This structured our entire design system.

##### Design Considerations:
- **When NOT to use**:
  - High amounts of data/complicated IA
  - Diverse general audience
  - Apps for kids, elderly, disabilities
  - Established products with existing brand

- **When TO use**:
  - Creative portfolios
  - Design-related startup landing pages
  - Experimental software wanting attention
  - Small touch to make websites stand out

Applied: Perfect for our educational design gallery

##### Real Examples Studied:
- **FigChallenge**: Design challenge app (designed by Sepideh)
- **Bitesized**: Design subscription company
- **MongoDB**: Added neo-brutalist elements to website (not product)
- **Figma**: Website/blog in neo-brutalism (product stays minimal)
- **Gumroad**: Completely neo-brutalist e-commerce platform
- **Abhishek Choudhury**: Personal developer website

Applied: Referenced Gumroad and Figma throughout our site

#### How This Influenced Our Design:

1. **Color System**:
   - Confirmed our black/white/yellow palette
   - Gave us confidence to use BRIGHT yellow (#FFFF00)
   - No gradients rule reinforced

2. **Shadow Technique**:
   - Learned exact formula: `8px 8px 0 #000000`
   - Understood no blur is intentional (not mistake)
   - Applied consistently across all buttons and cards

3. **Typography Approach**:
   - Large heading sizes justified (72-96px is normal)
   - ALL CAPS isn't excessive - it's characteristic
   - System fonts are deliberate choice

4. **Component Structure**:
   - Raw shapes with thick strokes
   - Cards with visible borders
   - Geometric simplicity

5. **Use Case Validation**:
   - Design portfolio/gallery is PERFECT use case
   - Educational purpose aligns with style
   - Not too complex for neo-brutalism

6. **Cheat Sheet Reference**:
   - Used as quick-check throughout development
   - Verified each design decision against criteria
   - Ensured authenticity

---

### 3. Gumroad Website (Live Example)
**URL**: https://gumroad.com/  
**Type**: Real-world neo-brutalist e-commerce platform

#### Observations:
- **Complete neo-brutalist implementation**
- Bold pink/purple colors with black borders
- Thick strokes on all elements
- Hard shadows on cards and buttons
- System fonts with clear hierarchy
- High contrast throughout
- No smooth transitions
- Sharp 90° corners everywhere

#### Design Elements Borrowed:
- Button styling approach (thick border + hard shadow)
- Card layout with visible structure
- Color blocking technique
- Typography contrast (large/small extremes)
- Raw, unpolished aesthetic balanced with usability

#### What We Learned:
- Neo-brutalism CAN work for complex systems (e-commerce)
- Users can navigate bold designs if structure is clear
- Bright colors don't compromise usability if contrast is good
- Thick borders create natural visual hierarchy

---

### 4. NEO-BRUTALISM-GUIDE.md (Professor's Style Guide)
**Location**: `/style-guides/intermediate/NEO-BRUTALISM-GUIDE.md`  
**Source**: Swiss Design Lineage Project repository  
**Type**: Comprehensive educational style documentation

#### Historical Context:
- **1950s origins**: Le Corbusier's béton brut (raw concrete)
- **1960s-70s peak**: Government buildings, universities
- **1980s-2000s decline**: Hundreds of buildings demolished
- **2010s digital revival**: Reaction against over-polished interfaces
- **2020s mainstream**: Balenciaga, Bloomberg, Washington Post

Applied: Created entire `history.html` page based on this timeline

#### Key Practitioners:
1. Le Corbusier - Architectural pioneer
2. Alison & Peter Smithson - Coined "Brutalism"
3. Pascal Deville - Founded BrutalistWebsites.com
4. Balenciaga Digital Team - High fashion brutalism
5. Bloomberg Design - Data journalism brutalism
6. Craig Newmark - Accidental brutalism (Craigslist)
7. Washington Post - Election coverage brutalism

Applied: Created `designers.html` with profiles of all 7

#### Design Specifications:
- **Color**: Black (#000000), White (#FFFFFF), bright accents
- **Typography**: System fonts, ALL CAPS, 1.2-1.4 line-height
- **Borders**: 4-5px thickness, #000000
- **Corners**: 0px border-radius (90° angles)
- **Shadows**: Hard offset (8px 8px 0), no blur
- **Spacing**: Tight and packed (16-32px)
- **Transitions**: none
- **Grid**: Visible and exposed

Applied: Built entire CSS system from these specs

#### Common Mistakes to Avoid:
1. ❌ Making it too pretty (rounded corners, soft shadows)
2. ❌ Using too many colors (rainbow palette)
3. ❌ Generous white space (airy layouts)
4. ❌ Smooth animations (fade transitions)
5. ❌ Hiding structure (seamless sections)

Applied: Actively avoided all of these in implementation

#### Authenticity Checklist:
- ✓ Stark black and white dominate
- ✓ Bright accent colors sparingly
- ✓ System fonts only
- ✓ ALL CAPS headings
- ✓ Thick borders (3-5px)
- ✓ No rounded corners
- ✓ Hard shadows
- ✓ Tight spacing
- ✓ Anti-corporate feel
- ✓ Deliberately rough (not accidentally amateur)

Applied: Used as verification throughout development

---

### 5. BrutalistWebsites.com
**URL**: https://brutalistwebsites.com  
**Curator**: Pascal Deville  
**Founded**: 2016  
**Type**: Definitive collection of brutalist web design (1000+ sites)

#### How This Informed Our Work:
- Reference point for authentic brutalism
- Inspiration for raw aesthetic
- Validation that our approach aligns with established examples
- Understanding of what makes design "brutalist" vs just ugly

Referenced in:
- History page (2016 digital revival)
- Designers page (Pascal Deville profile)
- Research notes as primary authority

---

## Synthesis: How Sources Shaped Final Design

### Color Palette Decision
**Sources**: NN/g (limit to 2-3 colors) + Sepideh (pitch black, vibrant colors) + Style Guide (black/white/accent)

**Result**:
```css
--color-black: #000000;   /* Sepideh: "pitch black with no fear" */
--color-white: #FFFFFF;   /* NN/g: high contrast base */
--color-yellow: #FFFF00;  /* Sepideh: vibrant, unrefined */
```

**Rationale**: 
- Exactly 3 colors (NN/g best practice)
- Maximum contrast (21:1 black/white)
- Bright yellow creates nostalgic 90s feel
- No gradients (Sepideh + Style Guide)

---

### Typography System
**Sources**: Sepideh (large headings, ALL CAPS, tight line-height) + NN/g (readable body text) + Style Guide (system fonts)

**Result**:
```css
h1 { font-size: 72px; }      /* Sepideh: "large font sizes for headings" */
body { font-size: 18px; }    /* NN/g: "prioritize readability" */
h1 { line-height: 1.2; }     /* Style Guide: 1.2-1.4 tight */
font-family: Arial, Helvetica, sans-serif; /* All sources: system fonts */
```

**Rationale**:
- Extreme size contrast (4x difference) creates hierarchy
- System fonts maintain raw aesthetic
- ALL CAPS for impact (characteristic of style)
- Readable body size despite tight philosophy

---

### Shadow Technique
**Sources**: Sepideh (exact formula) + Style Guide (hard shadows) + Gumroad (visual confirmation)

**Result**:
```css
box-shadow: 8px 8px 0 #000000;  /* Sepideh: "X, Y, 0 blur, black 100%" */
```

**Rationale**:
- No blur is INTENTIONAL (not technical limitation)
- Large offset creates depth without softness
- Consistent application maintains cohesion

---

### Border System
**Sources**: Style Guide (4-5px) + Sepideh (thick strokes define spaces) + Gumroad (visual reference)

**Result**:
```css
border: 4px solid #000000;   /* Style Guide: 4-5px thickness */
border-radius: 0;            /* All sources: NO rounded corners */
```

**Rationale**:
- Thick enough to be structural element
- Sharp corners resist softening
- Creates grid-like compartmentalization

---

### Spacing Philosophy
**Sources**: Style Guide (tight 16-32px) + NN/g (strategic whitespace 24-32px) + Sepideh (intentional cramping)

**Result**:
```css
padding: 32px;              /* Balance: tight but not cramped */
section { padding: 48px; }  /* NN/g: breathing room for bold elements */
```

**Rationale**:
- Tighter than Swiss design (32px vs 64px+)
- Looser than pure brutalism (32px vs 16px)
- Strategic compromise for readability

---

### Interaction Design
**Sources**: NN/g (clear interactions) + Style Guide (no transitions) + Sepideh (instant state changes)

**Result**:
```css
transition: none;                      /* Style Guide: no smoothness */
.brutal-button:hover {
    background: #FFFF00;               /* NN/g: clear state change */
    box-shadow: 6px 6px 0 #000000;     /* Instant shadow shift */
}
```

**Rationale**:
- Instant changes feel more "brutal"
- Clear enough for usability (NN/g requirement)
- Maintains raw aesthetic

---

### Responsive Strategy
**Sources**: NN/g (test on mobile) + Sepideh (considerations for different audiences) + Style Guide (maintain aesthetic)

**Result**:
```css
@media (max-width: 768px) {
    h1 { font-size: 48px; }        /* Scale down but keep impact */
    padding: 24px;                 /* Reduce but stay tight */
    box-shadow: 6px 6px 0 #000000; /* Smaller shadow, still hard */
}
```

**Rationale**:
- Mobile users need readability
- But style must remain intact
- No compromising on sharp corners or hard shadows

---

## Design Decisions: Source Mapping

| Design Element | Primary Source | Supporting Sources | Result |
|----------------|----------------|-------------------|---------|
| Color Palette | NN/g (limit 2-3) | Sepideh (vibrant), Style Guide | Black/White/Yellow only |
| Shadow Style | Sepideh (formula) | Style Guide, Gumroad | 8px 8px 0 #000000 |
| Border Thickness | Style Guide (4-5px) | Sepideh (thick strokes) | 4px solid #000000 |
| Typography Size | Sepideh (large headings) | NN/g (readable body) | 72px / 18px extreme contrast |
| Line Height | Style Guide (1.2-1.4) | Sepideh (tight spacing) | 1.2-1.4 throughout |
| Font Family | All sources | Style Guide emphasis | System fonts only |
| Border Radius | All sources | Gumroad visual | 0px (sharp 90° angles) |
| Transitions | Style Guide (none) | Sepideh (instant) | transition: none |
| Spacing | Style Guide (16-32) | NN/g (24-32 strategic) | 32-48px compromise |
| ALL CAPS | Sepideh (decorative) | Style Guide (headings) | All headings uppercase |
| Contrast Ratio | NN/g (WCAG standards) | — | 21:1 black/white tested |
| Grid Visibility | Style Guide (exposed) | Sepideh (bordered cards) | Boxed sections with borders |

---

## Content Sources

### Historical Information:
- **Style Guide**: Timeline from 1950s to 2020s
- **Sepideh**: Digital evolution (Figma, Gumroad, MongoDB)
- **NN/g**: Brutalism vs. neobrutalism distinction

### UX Best Practices:
- **NN/g**: 6 best practices framework
- **Sepideh**: When to use/not use considerations
- **Gumroad**: Real-world validation

### Design Examples:
- **Gumroad**: E-commerce platform
- **Figma**: Design tool website
- **Style Guide**: Washington Post, Balenciaga, Bloomberg

---

## What We Learned from Each Source

### From NN/g:
✓ Usability must come first (even in bold designs)  
✓ Contrast ratios are non-negotiable (accessibility)  
✓ Color palette must be LIMITED (cognitive load)  
✓ Whitespace is STRATEGIC (not absent)  
✓ Test interactions thoroughly  
✓ Real-world examples prove style works commercially

### From Sepideh:
✓ Exact shadow formula: X Y 0-blur color  
✓ No gradients rule (colors are distinct)  
✓ Typography as decorative element  
✓ Raw shapes with strokes are core  
✓ Use case matters (portfolio/creative is ideal)  
✓ Balance bold with intentional (not accidental amateur)

### From Style Guide:
✓ Historical context grounds design decisions  
✓ Authenticity comes from understanding origins  
✓ Common mistakes to actively avoid  
✓ System fonts are philosophical choice  
✓ Anti-corporate feeling is intentional  
✓ Tight spacing creates productive tension

### From Gumroad:
✓ Neo-brutalism works for complex systems  
✓ Users adapt to bold interfaces  
✓ Color blocking creates natural hierarchy  
✓ Thick borders don't hinder usability  
✓ Raw aesthetic = brand differentiation

---

## Validation: Design Aligned with Research

### Checklist from All Sources Combined:

#### Visual Style ✓
- [x] Stark black and white dominate (Style Guide, NN/g, Sepideh)
- [x] Bright accent colors sparingly (All sources: limited palette)
- [x] No gradients (Sepideh, Style Guide)
- [x] High contrast everywhere (NN/g: 21:1 verified)

#### Typography ✓
- [x] System fonts only (All sources)
- [x] ALL CAPS headings (Sepideh, Style Guide)
- [x] Tight line-height 1.2-1.4 (Style Guide, Sepideh)
- [x] Large size contrast (Sepideh: large headings, NN/g: readable body)

#### Layout ✓
- [x] Thick borders 4-5px (Style Guide, Sepideh)
- [x] No rounded corners (All sources)
- [x] Grid visible/obvious (Style Guide: exposed structure)
- [x] Boxed sections (Sepideh: cards with strokes)

#### Spacing ✓
- [x] Tight and packed (Style Guide: 16-32px)
- [x] Strategic whitespace (NN/g: 24-32px for breathing room)
- [x] Balance readability with philosophy (Compromise: 32-48px)

#### Components ✓
- [x] Thick borders on buttons (All sources)
- [x] Hard shadows 8px 8px 0 (Sepideh formula, Style Guide)
- [x] No smooth transitions (Style Guide, Sepideh)
- [x] Raw, unrefined appearance (Deliberate, not amateur)

#### UX & Accessibility ✓
- [x] Usability at forefront (NN/g primary principle)
- [x] Contrast ratios meet WCAG (NN/g: tested with tools)
- [x] Clear interactions (NN/g: recognizable elements)
- [x] Readable body text (NN/g: 16-18px)
- [x] Strategic whitespace offsets density (NN/g: 32-48px padding)

#### Overall Feel ✓
- [x] Deliberately rough (Not accidentally amateur)
- [x] Anti-corporate (Style Guide philosophy)
- [x] Honest about structure (Style Guide: exposed grid)
- [x] Functional and minimal (All sources)
- [x] NEO-brutalist (not pure brutalist) (NN/g distinction)

---

## Research Impact Summary

### Before Research:
- Vague understanding of "brutalist style"
- Could have created something accidentally amateur
- Would have missed UX best practices
- Might have used wrong terminology (brutalism vs neo-brutalism)

### After Research:
- ✓ Clear framework: Color + Components + Typography (Sepideh)
- ✓ Exact specifications: 8px 8px 0, 4-5px borders, 1.2-1.4 line-height
- ✓ UX validation: Contrast ratios, readability, accessibility (NN/g)
- ✓ Historical grounding: 1950s origins to 2020s mainstream (Style Guide)
- ✓ Real-world examples: Gumroad, Figma working implementations
- ✓ Proper terminology: NEO-BRUTALISM (not just brutalism)

### Result:
A **deliberately designed** neo-brutalist website that:
- Looks intentionally raw (not accidentally broken)
- Meets accessibility standards (not sacrificing usability)
- Follows established conventions (not making up rules)
- Honors historical context (understanding architectural roots)
- Balances boldness with function (usability-first approach)

---

## Additional References

### Tools Used:
- **WebAIM Contrast Checker**: Verified 21:1 black/white ratio
- **Coolors**: Generated yellow (#FFFF00) validation
- **MDN Web Docs**: CSS box-shadow specifications

### Visual Inspiration:
- Gumroad.com (live site review)
- BrutalistWebsites.com (portfolio examples)
- Figma marketing site (neo-brutalist elements)
- Washington Post 2016 election coverage (reference in Style Guide)

### Fonts Considered (but not used):
From Sepideh's recommendations:
- Lexend Mega - too specialized
- Public Sans - considered but system fonts won
- Mabry Pro - commercial font
- Archivo Black - too heavy
- Bebas Kai - too stylized

**Chose**: Arial/Helvetica/Sans-serif (system stack)  
**Rationale**: Most brutalist, universally available, fastest loading

---

## Credit & Attribution

### Primary Research:
1. **Nielsen Norman Group** - UX framework and validation
2. **Sepideh Yazdi** - Practical design tutorial and formulas
3. **NEO-BRUTALISM-GUIDE.md** - Historical context and specifications
4. **Gumroad.com** - Living example and validation

### Supporting Research:
- BrutalistWebsites.com (Pascal Deville)
- Swiss Design Lineage Project (Professor Keith Williams)
- Figma marketing site
- NN/g case studies (Tony's Chocolonely, 99percentoffsale, etc.)

### Educational Context:
- **Course**: IS 218 - Building Web Applications
- **Institution**: New Jersey Institute of Technology (NJIT)
- **Professor**: Keith Williams
- **Assignment**: Swiss Design Lineage with AI collaboration
- **Difficulty Level**: Intermediate (Neo-Brutalism)

---

## Conclusion

This neo-brutalist design gallery is built on **solid research foundation** combining:

1. **Academic UX Research** (Nielsen Norman Group)
2. **Practical Design Tutorial** (Sepideh Yazdi)
3. **Educational Style Guide** (Professor's Neo-Brutalism Guide)
4. **Real-World Examples** (Gumroad, Figma)

Every design decision can be **traced back to sources**:
- Color palette → NN/g + Sepideh + Style Guide
- Shadow technique → Sepideh formula + Gumroad visual
- Typography → All sources (system fonts, large headings, ALL CAPS)
- Spacing → Style Guide + NN/g compromise
- UX practices → NN/g 6 best practices framework

The result is **intentionally brutalist** (not accidentally amateur) and **functional** (not just bold).

---

**Research compiled**: November 10, 2025  
**Project**: Neo-Brutalist Design Gallery  
**Student**: Adriana So  
**Course**: IS 218, NJIT, Fall 2025
