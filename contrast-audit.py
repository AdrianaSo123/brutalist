#!/usr/bin/env python3
"""WCAG 2.1 AA Contrast Ratio Calculator"""

def hex_to_rgb(hex_color):
    """Convert hex color to RGB"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def relative_luminance(rgb):
    """Calculate relative luminance per WCAG formula"""
    r, g, b = [x / 255.0 for x in rgb]
    
    def adjust(color):
        return color / 12.92 if color <= 0.03928 else ((color + 0.055) / 1.055) ** 2.4
    
    r, g, b = adjust(r), adjust(g), adjust(b)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast_ratio(color1, color2):
    """Calculate contrast ratio between two colors"""
    lum1 = relative_luminance(hex_to_rgb(color1))
    lum2 = relative_luminance(hex_to_rgb(color2))
    
    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    
    return (lighter + 0.05) / (darker + 0.05)

def check_wcag(ratio, text_size="normal"):
    """Check WCAG compliance"""
    if text_size == "large":  # 18pt+ or 14pt+ bold
        if ratio >= 4.5:
            return "✅ AAA"
        elif ratio >= 3.0:
            return "✅ AA"
        else:
            return "❌ FAIL"
    else:  # normal text
        if ratio >= 7.0:
            return "✅ AAA"
        elif ratio >= 4.5:
            return "✅ AA"
        else:
            return "❌ FAIL"

# Current palette
colors = {
    "Black": "#000000",
    "White": "#FFFFFF",
    "Cyan": "#00FFB3",
    "Yellow": "#F7E74F",
    "Pink": "#FFB3D9"
}

print("=" * 80)
print("NEO-BRUTALISM COLOR PALETTE - WCAG 2.1 AA CONTRAST AUDIT")
print("=" * 80)
print()

# Test all combinations with black text
print("BLACK TEXT (#000000) ON COLORED BACKGROUNDS:")
print("-" * 80)
for name, color in colors.items():
    if name != "Black":
        ratio = contrast_ratio("#000000", color)
        status_normal = check_wcag(ratio, "normal")
        status_large = check_wcag(ratio, "large")
        print(f"{name:12} ({color}): {ratio:5.2f}:1  |  Normal: {status_normal}  |  Large: {status_large}")

print()
print("WHITE TEXT (#FFFFFF) ON COLORED BACKGROUNDS:")
print("-" * 80)
for name, color in colors.items():
    if name != "White":
        ratio = contrast_ratio("#FFFFFF", color)
        status_normal = check_wcag(ratio, "normal")
        status_large = check_wcag(ratio, "large")
        print(f"{name:12} ({color}): {ratio:5.2f}:1  |  Normal: {status_normal}  |  Large: {status_large}")

print()
print("=" * 80)
print("RECOMMENDATIONS:")
print("=" * 80)
print("✅ = Passes WCAG standard")
print("❌ = Fails WCAG standard (do not use this combination)")
print()
print("Normal text: Body copy, regular paragraphs (4.5:1 minimum for AA)")
print("Large text: Headings 18pt+ or 14pt+ bold (3.0:1 minimum for AA)")
print("=" * 80)
