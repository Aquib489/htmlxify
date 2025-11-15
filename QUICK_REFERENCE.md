# htmlxify Quick Reference

## Element Syntax

```
element[.class][.class2][#id](attr: value) { content }
```

## Cheat Sheet

### Basic Elements
```markup
div { ... }
p { ... }
h1, h2, h3, h4, h5, h6 { ... }
button { ... }
a(href: "url") { ... }
img(src: "url", alt: "text")
input(type: "text")
```

### Classes & IDs
```markup
div.classname { ... }
div.class1.class2 { ... }
div#idname { ... }
div#id.classname { ... }
```

### Attributes
```markup
// Multiple attributes
a(
  href: "url",
  target: "_blank",
  class: "link"
) { ... }

// Common attributes
(type: "email")
(placeholder: "text")
(required: true)
(disabled: false)
(data-id: "123")
```

### Special Attributes
```markup
// Backend call
button(⚡-call: "endpoint") { ... }

// Dynamic data
div(⚡-data: "dataKey") { ... }
```

### Nesting
```markup
div {
  h1 { Title }
  p { Content }
  button { Action }
}
```

### Available Classes
```
.navbar          .hero           .container
.feature-card    .feature-grid   .pricing-card
.pricing-grid    .badge          .comparison
.footer          .button         .primary
```

### Available Endpoints
```
trackCTAClick    submitForm      selectPlan
contactSales     getData         getStats
```

## Common Patterns

### Navigation
```markup
nav.navbar {
  div.brand { Logo }
  div.menu {
    a(href: "/") { Home }
    a(href: "/about") { About }
  }
}
```

### Hero Section
```markup
div.hero {
  h1 { Title }
  p { Subtitle }
  button(⚡-call: "trackCTAClick") { CTA }
}
```

### Feature Cards
```markup
div.feature-grid {
  div.feature-card { Feature 1 }
  div.feature-card { Feature 2 }
  div.feature-card { Feature 3 }
}
```

### Pricing Cards
```markup
div.pricing-grid {
  div.pricing-card {
    h3 { Plan }
    button(⚡-call: "selectPlan") { Choose }
  }
  div.pricing-card.featured {
    h3 { Best }
    button(⚡-call: "selectPlan") { Choose }
  }
}
```

### Form
```markup
form {
  input(type: "text", placeholder: "Name")
  input(type: "email", placeholder: "Email")
  textarea(placeholder: "Message")
  button(type: "submit") { Send }
}
```

### Table
```markup
table.comparison {
  thead {
    tr {
      th { Column }
      th { Value }
    }
  }
  tbody {
    tr {
      td { Data }
      td { Value }
    }
  }
}
```

### Lists
```markup
ul {
  li { Item 1 }
  li { Item 2 }
  li { Item 3 }
}
```

### Footer
```markup
footer.footer {
  div.footer-column { Section 1 }
  div.footer-column { Section 2 }
  div.copyright { Copyright }
}
```

## CLI Commands

```bash
# Compile
htmlxify input.htmlxify output/

# Verbose
htmlxify input.htmlxify output/ --verbose

# Help
htmlxify --help

# Version
htmlxify --version
```

## Semantic HTML Elements

```
header    footer    main
nav       article   section
aside     figure    details
summary   dialog    form
```

## Tips

- ✓ Use `.class-name` format for classes
- ✓ Use `#unique-id` for IDs (one per element)
- ✓ Attributes: `(key: value, key2: value2)`
- ✓ No spaces before `.` or `#`
- ✓ Use descriptive class names
- ✓ Close all braces `{ }`

## Common Mistakes

```markup
// ❌ WRONG - space before dot
div .container { ... }

// ✓ CORRECT
div.container { ... }

// ❌ WRONG - space before hash
div #main { ... }

// ✓ CORRECT
div#main { ... }

// ❌ WRONG - no comma between attributes
button(onclick: "x" data-id: "1") { }

// ✓ CORRECT
button(onclick: "x", data-id: "1") { }

// ❌ WRONG - unquoted string
a(href: example.com) { }

// ✓ CORRECT
a(href: "example.com") { }
```

## File Structure

```
Input:   mypage.htmlxify
         └─→ Compiler
         ├─→ mypage.html (HTML)
         ├─→ mypage.css (Styles)
         ├─→ mypage.js (JavaScript)
         └─→ mypage.html.map (Source Map)
```

## Output File Sizes

- HTML: ~10-15 KB (semantic structure)
- CSS: ~7+ KB (650+ lines of defaults + custom)
- JS: ~5 KB (API handlers, data binding, animations)

## Getting Help

1. Read [README.md](README.md) for overview
2. Check [HOW_TO_USE.md](HOW_TO_USE.md) for detailed guide
3. Review `comprehensive_test.htmlxify` for examples
4. Check generated files for clues
5. Use `--verbose` flag for debugging

---

**Quick tip:** Copy and paste the patterns above to start building pages immediately!
