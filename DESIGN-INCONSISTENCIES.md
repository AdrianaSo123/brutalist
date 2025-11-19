# DESIGN INCONSISTENCY AUDIT
**Expert Neo-Brutalist Review**

## Critical Issues:

### 1. Text Shadows (INCONSISTENT)
**Problem:** Mixed usage creates visual confusion
- history.html: 2px, 3px
- designers.html: 2px, 3px  
- about.html: 3px AND none
- collaboration.html: 2px, 3px

**Neo-Brutalist Standard:**
Text shadows are NOT neo-brutalist. They soften edges and reduce clarity.
- ✅ REMOVE ALL text-shadows
- High contrast already provides depth
- Shadows add unnecessary decoration

### 2. Box Shadow Sizes (INCONSISTENT)
**Main CSS:**
- Navigation: 4px, 6px, 8px
- Content boxes: 10px, 12px
- Large sections: 16px, 20px

**Embedded HTML:**
- Everything: 16px (no variation)

**Neo-Brutalist Standard:**
Shadow size should indicate hierarchy:
- Small elements: 4-8px
- Medium boxes: 10-12px
- Large sections: 16-20px
- ✅ Need consistent scale

### 3. Border Thickness (MOSTLY CONSISTENT ✅)
- 4px: Small elements
- 6-8px: Medium boxes
- 10-12px: Large sections
- **This is good - maintain this**

### 4. Color Usage (NEEDS REVIEW)
Pink #FFB3D9 usage:
- ✅ Structural borders (12px left borders) - GOOD
- ✅ Box shadows - GOOD
- ❌ Header backgrounds on some cards - INCONSISTENT

Should pink be:
- A) Accent only (borders, shadows)
- B) Also backgrounds occasionally

Currently mixing both = inconsistent

## Recommendations:

1. **REMOVE all text-shadows** across all pages
2. **Standardize box-shadow scale:**
   - 8px for cards
   - 12px for sections
   - 16px for major containers
3. **Define pink role:** Border/shadow accent only (no backgrounds except where structurally necessary)

