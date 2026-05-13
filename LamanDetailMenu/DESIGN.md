---
name: Vibrant Efficiency
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#5a4136'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#8e7164'
  outline-variant: '#e2bfb0'
  surface-tint: '#a04100'
  primary: '#a04100'
  on-primary: '#ffffff'
  primary-container: '#ff6b00'
  on-primary-container: '#572000'
  inverse-primary: '#ffb693'
  secondary: '#5d5e61'
  on-secondary: '#ffffff'
  secondary-container: '#e2e2e5'
  on-secondary-container: '#636467'
  tertiary: '#8b5000'
  on-tertiary: '#ffffff'
  tertiary-container: '#dd8300'
  on-tertiary-container: '#4a2900'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#e2e2e5'
  secondary-fixed-dim: '#c6c6c9'
  on-secondary-fixed: '#1a1c1e'
  on-secondary-fixed-variant: '#454749'
  tertiary-fixed: '#ffdcbe'
  tertiary-fixed-dim: '#ffb870'
  on-tertiary-fixed: '#2c1600'
  on-tertiary-fixed-variant: '#693c00'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  button:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  margin-mobile: 20px
  gutter-mobile: 12px
---

## Brand & Style

The design system is anchored in the concept of "Vibrant Efficiency." It targets a modern, fast-moving audience that values both aesthetic warmth and functional clarity. The brand personality is energetic, approachable, and highly organized. 

The visual style is **Modern Corporate with a Friendly Edge**, leaning heavily into minimalism to ensure the "vibrant orange" remains a powerful focal point without overwhelming the user. By utilizing expansive white space and high-contrast typography, the UI minimizes cognitive load, making the app feel effortless and professional. Soft shadows and generous curves prevent the interface from feeling clinical, adding a human touch to a high-performance tool.

## Colors

This design system utilizes a high-energy primary palette balanced by a sophisticated neutral foundation.

- **Primary (Vibrant Orange):** Used exclusively for primary actions, active states, and brand-critical elements. It is the "pulse" of the application.
- **Secondary (Deep Charcoal):** Used for primary headings and high-priority text to ensure maximum readability against white backgrounds.
- **Neutrals:** A range of cool, subtle grays are used for borders and secondary text to maintain a clean, uncluttered appearance.
- **Semantic Colors:** Success, Warning, and Error states should be clearly defined but used sparingly to allow the primary orange to lead the visual hierarchy.

## Typography

The typography strategy employs **Plus Jakarta Sans** for its modern, friendly, and geometric characteristics. It strikes the perfect balance between professional and approachable.

- **Headlines:** Set with tighter letter spacing and heavier weights to create a strong visual anchor.
- **Body Text:** Optimized for legibility with generous line heights. The "Deep Charcoal" (#1A1C1E) is used for body text to maintain high contrast.
- **Hierarchy:** Use weight (Bold vs Regular) rather than size shifts alone to differentiate information levels, maintaining a compact mobile layout.

## Layout & Spacing

This design system uses a **4px baseline grid** to ensure mathematical harmony across all components.

- **Mobile Layout:** A fluid 4-column grid with 20px outer margins. This provides a "breathing room" feel that aligns with the brand's emphasis on white space.
- **Stacking:** Use the `lg` (24px) unit to separate distinct sections or cards, and `sm` (8px) for related elements within a group.
- **Efficiency:** Vertical density is prioritized in lists, but touch targets must never drop below 44x44px to maintain usability.

## Elevation & Depth

Hierarchy is established through **Ambient Shadows** and **Tonal Layering**. 

1. **Flat Surface:** The main background is pure white (#FFFFFF).
2. **Raised Level (Cards):** Components use a soft, highly diffused shadow (Shadow Blur: 20px, Y-Offset: 4px, Opacity: 4% Black) to appear subtly lifted.
3. **Interactive Level (Buttons):** Active buttons may use a slightly more pronounced shadow with a hint of the primary orange color in the shadow mix to indicate "pressability."
4. **Dividers:** Use 1px solid borders in #E9ECEF only when white space alone is insufficient to separate content.

## Shapes

The shape language is consistently **Rounded**. This softens the high-contrast color palette and makes the app feel more inviting.

- **Primary Components:** Buttons and Input fields use a 0.5rem (8px) radius.
- **Containers:** Large cards and modals use the `rounded-xl` (24px) setting to create a friendly, "app-like" container feel.
- **Icons:** Should be selected from a rounded-cap library (e.g., Lucide or Phosphor) to match the UI's corner radii.

## Components

- **Buttons:** Primary buttons are solid Vibrant Orange with white text. Secondary buttons use a subtle gray outline or a ghost style to remain secondary in the visual hierarchy.
- **Inputs:** Fields use a light gray background (#F8F9FA) with a 1px border that turns Vibrant Orange on focus. Labels sit clearly above the field in `label-md`.
- **Cards:** White background with `rounded-xl` corners and the standard ambient shadow. Content inside cards should follow the 16px (md) internal padding rule.
- **Chips/Tags:** Used for categorization, these should have a 100px (pill) radius and use a light tint of the primary color (e.g., 10% opacity orange) with dark text.
- **Lists:** Clean rows with 1px bottom borders in #E9ECEF. Use "Chevron Right" icons in the primary orange color to indicate drill-down actions.
- **Navigation:** A clean bottom tab bar with high-contrast icons. The active state is indicated by a color shift to Vibrant Orange and a small dot indicator below the icon.