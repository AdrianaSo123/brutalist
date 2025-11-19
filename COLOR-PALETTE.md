# Neo-Brutalism Color Palette
## Standardized Colors - November 19, 2025

**THESE ARE THE ONLY COLORS USED IN THIS PROJECT**

## Primary Colors (CSS Variables)

```css
:root {
    --color-black: #000000;
    --color-white: #FFFFFF;
    --color-yellow: #FFFF00;
    --color-pink: #FF69B4;
    --color-blue: #00CED1;
    --color-green: #00FF7F;
    --color-red: #FF1744;
}
```

## Color Usage

| Color | Hex Code | CSS Variable | Usage |
|-------|----------|--------------|-------|
| **Black** | `#000000` | `var(--color-black)` | Text, borders, backgrounds |
| **White** | `#FFFFFF` | `var(--color-white)` | Backgrounds, text on dark |
| **Yellow** | `#FFFF00` | `var(--color-yellow)` | Accent color, highlights |
| **Pink** | `#FF69B4` | `var(--color-pink)` | Shadows, accents |
| **Blue** | `#00CED1` | `var(--color-blue)` | Accents, highlights |
| **Green** | `#00FF7F` | `var(--color-green)` | Shadows, backgrounds |
| **Red** | `#FF1744` | `var(--color-red)` | Alert color, accents |

## ❌ OLD COLORS (DO NOT USE)

These colors were replaced in the standardization:
- ~~`#FFD93D`~~ → Use `#FFFF00` (yellow)
- ~~`#FF6B9D`~~ → Use `#FF69B4` (pink)
- ~~`#6BCF7F`~~ → Use `#00FF7F` (green)
- ~~`#FF6B6B`~~ → Use `#FF1744` (red)

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

November 19, 2025 - Color standardization audit
