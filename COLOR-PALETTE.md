# Neo-Brutalism Color Palette
## Standardized Colors - November 19, 2025

**THESE ARE THE ONLY COLORS USED IN THIS PROJECT**

## Primary Colors (CSS Variables)

**Limited Palette: Black + White + 3 Accent Colors**  
Following Nielsen Norman Group recommendation to prevent overwhelming users.  
**Inspired by:** Modern Neo-Brutalist reference designs - softer, less harsh palette

```css
:root {
    --color-black: #000000;
    --color-white: #FFFFFF;
    --color-green: #00FFB3;  /* Cyan/turquoise - primary accent */
    --color-yellow: #F7E74F; /* Softer yellow - less harsh */
    --color-pink: #FFB3D9;   /* Softer pink/lavender - pastel */
}
```

## Color Usage

| Color | Hex Code | CSS Variable | Usage |
|-------|----------|--------------|-------|
| **Black** | `#000000` | `var(--color-black)` | Text, borders, backgrounds |
| **White** | `#FFFFFF` | `var(--color-white)` | Backgrounds, text on dark |
| **Cyan** | `#00FFB3` | `var(--color-green)` | Primary accent - shadows, backgrounds |
| **Yellow** | `#F7E74F` | `var(--color-yellow)` | Secondary accent - softer, less harsh |
| **Pink** | `#FFB3D9` | `var(--color-pink)` | Tertiary accent - pastel pink/lavender |

## ❌ OLD COLORS (DO NOT USE)

These colors were removed or replaced:
- ~~`#FFFF00`~~ (harsh yellow) → Use `#F7E74F` (softer yellow)
- ~~`#FF69B4`~~ (hot pink) → Use `#FFB3D9` (softer pastel pink)
- ~~`#00CED1`~~ (old blue) - Removed
- ~~`#FF1744`~~ (red) - Removed
- ~~`#00FF7F`~~ (spring green) → Use `#00FFB3` (cyan)
- ~~`#FFD93D`~~, ~~`#FF6B9D`~~, ~~`#6BCF7F`~~ - Old versions

**Current palette:** Softer, less harsh colors inspired by modern Neo-Brutalist designs. Maintains boldness without being overwhelming.

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
