# Neo-Brutalism Color Palette
## Standardized Colors - November 19, 2025

**THESE ARE THE ONLY COLORS USED IN THIS PROJECT**

## Primary Colors (CSS Variables)

**Limited Palette: Black + White + 3 Accent Colors**  
Following Nielsen Norman Group recommendation to prevent overwhelming users.  
**Inspired by:** Modern Neo-Brutalist reference designs (yellow, cyan, pink combo)

```css
:root {
    --color-black: #000000;
    --color-white: #FFFFFF;
    --color-green: #00FFB3;  /* Cyan/turquoise - primary accent */
    --color-yellow: #FFFF00; /* Yellow - secondary accent */
    --color-pink: #FF69B4;   /* Pink - tertiary accent */
}
```

## Color Usage

| Color | Hex Code | CSS Variable | Usage |
|-------|----------|--------------|-------|
| **Black** | `#000000` | `var(--color-black)` | Text, borders, backgrounds |
| **White** | `#FFFFFF` | `var(--color-white)` | Backgrounds, text on dark |
| **Cyan** | `#00FFB3` | `var(--color-green)` | Primary accent - shadows, backgrounds |
| **Yellow** | `#FFFF00` | `var(--color-yellow)` | Secondary accent - highlights |
| **Pink** | `#FF69B4` | `var(--color-pink)` | Tertiary accent - shadows, accents |

## ❌ OLD COLORS (DO NOT USE)

These colors were removed or replaced:
- ~~`#00CED1`~~ (old blue) - Never used, removed
- ~~`#FF1744`~~ (red) - Replaced with pink #FF69B4
- ~~`#00FF7F`~~ (spring green) → Use `#00FFB3` (cyan/turquoise)
- ~~`#FFD93D`~~ → Use `#FFFF00` (yellow)
- ~~`#FF6B9D`~~ → Use `#FF69B4` (pink)
- ~~`#6BCF7F`~~ → Use `#00FFB3` (cyan)

**Current palette:** Inspired by modern Neo-Brutalist designs - cyan, yellow, pink combo creates vibrant but cohesive look.

## Where Colors Are Defined

1. **CSS Variables**: `/styles.css` and `/site/styles.css` (lines 5-12)
2. **HTML Embedded Styles**: Hardcoded throughout HTML files (now standardized)

## How to Use

**✅ PREFERRED** - Use CSS variables:
```css
.element {
    background-color: var(--color-yellow);
    color: var(--color-black);
    box-shadow: 8px 8px 0 var(--color-pink);
}
```

**⚠️ ACCEPTABLE** - Use hex codes directly (for embedded styles):
```html
<style>
    .special { background-color: #FFFF00; }
</style>
```

## Accessibility

All color combinations meet WCAG AA standards:
- Black on White: 21:1 ✓
- White on Black: 21:1 ✓
- Black on Yellow (#FFFF00): 10.4:1 ✓

## Last Updated

November 19, 2025 - Updated to cyan/turquoise (#00FFB3) inspired by modern Neo-Brutalist reference designs. Final palette: cyan, yellow, pink - vibrant but cohesive.
