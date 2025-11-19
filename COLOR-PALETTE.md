# Neo-Brutalism Color Palette
## Standardized Colors - November 19, 2025

**THESE ARE THE ONLY COLORS USED IN THIS PROJECT**

## Primary Colors (CSS Variables)

**Limited Palette: Black + White + 3 Accent Colors**  
Following Nielsen Norman Group recommendation to prevent overwhelming users.

```css
:root {
    --color-black: #000000;
    --color-white: #FFFFFF;
    --color-green: #00FF7F;  /* Primary accent - most used */
    --color-yellow: #FFFF00; /* Secondary accent */
    --color-pink: #FF69B4;   /* Tertiary accent */
}
```

## Color Usage

| Color | Hex Code | CSS Variable | Usage |
|-------|----------|--------------|-------|
| **Black** | `#000000` | `var(--color-black)` | Text, borders, backgrounds |
| **White** | `#FFFFFF` | `var(--color-white)` | Backgrounds, text on dark |
| **Green** | `#00FF7F` | `var(--color-green)` | Primary accent - shadows, backgrounds |
| **Yellow** | `#FFFF00` | `var(--color-yellow)` | Secondary accent - highlights |
| **Pink** | `#FF69B4` | `var(--color-pink)` | Tertiary accent - shadows, accents |

## ❌ OLD COLORS (DO NOT USE)

These colors were removed in the palette simplification:
- ~~`#00CED1`~~ (blue) - Never used, removed
- ~~`#FF1744`~~ (red) - Replaced with pink #FF69B4
- ~~`#FFD93D`~~ → Use `#FFFF00` (yellow)
- ~~`#FF6B9D`~~ → Use `#FF69B4` (pink)
- ~~`#6BCF7F`~~ → Use `#00FF7F` (green)

**Rationale:** Limited to 3 accent colors (green, yellow, pink) to prevent overwhelming users while maintaining Neo-Brutalist boldness.

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

November 19, 2025 - Simplified to 3 accent colors (green, yellow, pink) following NN/g UX recommendation to limit palette and prevent overwhelming users.
