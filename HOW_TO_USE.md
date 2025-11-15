# How to Use HTMLx - Complete Guide

This guide walks you through everything you need to know to use the HTMLx compiler effectively.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Basic Syntax](#basic-syntax)
3. [Working with Elements](#working-with-elements)
4. [Styling with Classes & IDs](#styling-with-classes--ids)
5. [Attributes & Properties](#attributes--properties)
6. [Advanced Features](#advanced-features)
7. [Compiling Your Files](#compiling-your-files)
8. [Real-World Examples](#real-world-examples)
9. [Common Patterns](#common-patterns)
10. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Step 1: Install the Compiler

**Option 1: Install from TestPyPI (Recommended)**

```bash
pip install -i https://test.pypi.org/simple/ htmlx
```

**Option 2: Install from Source**

```bash
# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .

# Verify it's installed
htmlx --help
```

### Step 2: Create Your First File

Create a new file with `.htmlx` extension, for example `mypage.htmlx`:

```markup
div { Hello World }
```

### Step 3: Compile It

```bash
# Using installed package
htmlx mypage.htmlx output/

# Or using Python CLI
python cli.py mypage.htmlx output/
```

This creates three files in the `output/` directory:
- `mypage.html` - Your HTML structure
- `mypage.css` - Automatic styling
- `mypage.js` - JavaScript helpers

### Step 4: View the Result

Open `output/mypage.html` in your browser!

---

## Basic Syntax

### Elements

HTMLx uses a simplified syntax for HTML elements:

```markup
// Creating elements
div { Content }
p { Paragraph }
h1 { Heading }
button { Click Me }
span { Text }

// Self-closing elements
img(src: "image.jpg", alt: "Image")
input(type: "text", placeholder: "Enter text")
br
hr
```

### Block vs Inline

Block elements automatically create new lines:
```markup
div { Block element }
p { Another block }
```

Inline elements stay on the same line (when inside text):
```markup
p {
  This is text with
  span { inline content }
  in the middle
}
```

### Content

Elements can contain:
- **Text**: `div { Hello }`
- **Other elements**: `div { p { Nested } }`
- **Mixed content**: `div { Text here p { Element } more text }`

---

## Working with Elements

### Single Elements

```markup
// Simple element
div { Content }

// With content on multiple lines
div {
  This is a longer
  block of text that
  spans multiple lines
}
```

### Nested Elements

```markup
// Basic nesting
div {
  h1 { Title }
  p { Paragraph }
}

// Multiple levels
div {
  section {
    h2 { Section Title }
    p { Content }
    button { Action }
  }
}
```

### Repeating Elements

```markup
// Multiple similar elements
div {
  p { First paragraph }
  p { Second paragraph }
  p { Third paragraph }
}

// For cards or lists
div.card-list {
  div.card { Card 1 }
  div.card { Card 2 }
  div.card { Card 3 }
}
```

### Empty Elements

```markup
// Element with no content (self-closing)
br
hr
img(src: "image.jpg", alt: "")

// Element as container
div { }
```

---

## Styling with Classes & IDs

### Classes

Classes are used for styling and grouping elements. You can have multiple classes per element.

```markup
// Single class
div.container { ... }

// Multiple classes
button.primary.large { Click Me }

// Class naming (use hyphens for multiple words)
div.feature-card { ... }
p.hero-subtitle { ... }
```

### IDs

IDs uniquely identify elements. Each element can have one ID.

```markup
// Single ID
div#main { ... }
button#submit-btn { ... }

// ID with classes
div#app.container { ... }
button#cta-button.primary.large { ... }
```

### Styling Classes

The compiler automatically provides default styles for common classes:

```markup
// These classes have automatic styling:
nav.navbar { ... }          // Navigation bar
div.hero { ... }            // Hero section
div.container { ... }       // Container
div.feature-card { ... }    // Feature card
div.pricing-card { ... }    // Pricing card
button.primary { ... }      // Primary button
table.comparison { ... }    // Comparison table
footer.footer { ... }       // Footer
```

### Custom Classes

You can create any custom classes:

```markup
// Custom classes get basic styling
div.my-custom-class { ... }

// Then modify in the generated CSS file
```

---

## Attributes & Properties

### Basic Attributes

```markup
// String attributes
a(href: "https://example.com") { Link }

// Boolean attributes
input(type: "checkbox", checked: true)
input(type: "text", required: true)

// Multiple attributes
input(
  type: "email",
  placeholder: "Enter email",
  required: true
)
```

### Common Attributes

```markup
// Links
a(href: "page.html", target: "_blank") { External Link }

// Images
img(src: "photo.jpg", alt: "Description", loading: "lazy")

// Forms
input(type: "text", placeholder: "Name", required: true)
input(type: "email", placeholder: "Email")
textarea(placeholder: "Message", rows: 5)
button(type: "submit") { Submit }

// Buttons
button(onclick: "doSomething()") { Click }
button(disabled: true) { Disabled Button }

// Data attributes
div(data-id: "123", data-name: "item") { ... }
```

### Attribute Values

```markup
// String values (with or without quotes)
a(href: "https://example.com") { Link }
div(data-name: myValue) { ... }

// Numbers
input(maxlength: 100)
div(data-count: 5) { ... }

// Boolean values
input(required: true)
button(disabled: false) { ... }
```

---

## Advanced Features

### Special Attributes for Interactivity

#### Backend Integration with `⚡-call`

```markup
// Track button clicks
button(⚡-call: "trackCTAClick") { Get Started }

// Plan selection
button(⚡-call: "selectPlan", data-plan: "starter") {
  Choose Plan
}

// Form submission
button(⚡-call: "submitForm") { Submit }

// Contact inquiry
button(⚡-call: "contactSales") { Contact Sales }
```

**What happens:**
1. Compiler converts `⚡-call` to `data-api-call` in HTML
2. JavaScript automatically triggers the handler on page load
3. Mock data is returned (no backend needed for demo)

**Available endpoints:**
- `trackCTAClick` - Click tracking
- `submitForm` - Form handler
- `selectPlan` - Plan selection
- `contactSales` - Sales inquiry
- `getData` - Generic data endpoint

#### Dynamic Data Binding with `⚡-data`

```markup
// Bind element to data
div(⚡-data: "userName") {
  Hello User!
}

// Update dynamically with JavaScript:
// updateBinding('userName', 'John Doe');
```

### Semantic HTML Elements

```markup
// Use semantic HTML elements
header.navbar { ... }
nav { ... }
main { ... }
article { ... }
section { ... }
aside { ... }
footer { ... }
```

### Forms

```markup
form {
  div.form-group {
    label(for: "email") { Email }
    input(id: "email", type: "email", required: true)
  }
  
  div.form-group {
    label(for: "message") { Message }
    textarea(id: "message", rows: 5)
  }
  
  button(type: "submit") { Send }
}
```

### Lists

```markup
// Unordered list
ul {
  li { Item 1 }
  li { Item 2 }
  li { Item 3 }
}

// Ordered list
ol {
  li { First }
  li { Second }
  li { Third }
}

// Description list
dl {
  dt { Term }
  dd { Definition }
}
```

### Tables

```markup
table.comparison {
  thead {
    tr {
      th { Feature }
      th { Basic }
      th { Pro }
    }
  }
  tbody {
    tr {
      td { Users }
      td { 5 }
      td { Unlimited }
    }
    tr {
      td { Storage }
      td { 10 GB }
      td { 1 TB }
    }
  }
}
```

### Media Elements

```markup
// Images
img(src: "photo.jpg", alt: "Photo", loading: "lazy")

// Audio
audio(src: "song.mp3", controls: true)

// Video
video(src: "video.mp4", controls: true, width: 640, height: 480)
```

### Details & Summary (Expandable)

```markup
details {
  summary { Click to expand }
  p { Hidden content that appears when clicked }
}
```

### Progress & Meter

```markup
// Progress bar
progress(value: 70, max: 100)

// Meter gauge
meter(value: 6, min: 0, max: 10)
```

---

## Compiling Your Files

### Command Line Usage

```bash
# Using installed package
htmlx input.htmlx output/
htmlx input.htmlx output/ --verbose

# Or using Python CLI
python cli.py input.htmlx output/
python cli.py input.htmlx output/ --verbose

# With verbose output (shows each step)
python cli.py input.htmlx output/ --verbose

# Show help
python cli.py --help

# Check version
python cli.py --version
```

### Output Directory

The compiler creates three files:

```
output/
├── input.html          # HTML structure
├── input.css           # CSS styling (7+ KB)
├── input.js            # JavaScript
└── input.html.map      # Source map
```

### Verbose Mode

Use `--verbose` to see detailed compilation steps:

```bash
python cli.py myfile.htmlx output/ --verbose
```

Output:
```
Compiling myfile.htmlx...

Step 1/6: Parsing...
✓ Parsing complete
Step 2/6: Processing indentation...
✓ Indentation processed
Step 3/6: Validating...
✓ Validation complete
Step 4/6: Generating HTML...
✓ Generated output\myfile.html
Step 5/6: Generating CSS...
✓ Generated output\myfile.css
Step 6/6: Generating JavaScript...
✓ Generated output\myfile.js

Compilation successful!
```

---

## Real-World Examples

### Example 1: Simple Blog Post

```markup
article.post {
  header {
    h1 { How to Use HTMLx }
    p.meta { Published on November 12, 2025 }
  }
  
  div.content {
    p { This is the introduction to the post. }
    
    h2 { Section 1 }
    p { Content for section 1 }
    
    h2 { Section 2 }
    p { Content for section 2 }
  }
  
  footer.post-footer {
    p { By Author Name }
  }
}
```

### Example 2: Contact Form

```markup
div.contact-form {
  h2 { Contact Us }
  
  form {
    div.form-group {
      label(for: "name") { Full Name }
      input(id: "name", type: "text", required: true)
    }
    
    div.form-group {
      label(for: "email") { Email Address }
      input(id: "email", type: "email", required: true)
    }
    
    div.form-group {
      label(for: "message") { Message }
      textarea(id: "message", rows: 6, required: true)
    }
    
    button.primary(⚡-call: "submitForm") { Send Message }
  }
}
```

### Example 3: Product Card

```markup
div.product-card {
  img(src: "product.jpg", alt: "Product", loading: "lazy")
  
  h3 { Product Name }
  
  p.price { $99.99 }
  
  p.description {
    This is a great product that solves problems.
  }
  
  div.rating {
    span { 4.8/5 }
    span.reviews { (124 reviews) }
  }
  
  button.primary(⚡-call: "trackCTAClick") {
    Add to Cart
  }
}
```

### Example 4: Testimonial Section

```markup
div.testimonials {
  h2 { What People Say }
  
  div.testimonial-grid {
    div.testimonial-card {
      p { Great product! Very happy with my purchase. }
      p.author { — John Doe }
    }
    
    div.testimonial-card {
      p { Best service I've ever used. Highly recommend! }
      p.author { — Jane Smith }
    }
    
    div.testimonial-card {
      p { Amazing quality and fast shipping. }
      p.author { — Mike Johnson }
    }
  }
}
```

---

## Common Patterns

### Navigation Bar

```markup
nav.navbar {
  div.navbar-brand { MyCompany }
  
  div.navbar-links {
    a(href: "/") { Home }
    a(href: "/about") { About }
    a(href: "/services") { Services }
    a(href: "/contact") { Contact }
  }
}
```

### Hero Section

```markup
div.hero {
  h1.hero-title { Welcome to Our Site }
  p.hero-subtitle { Build amazing things today }
  
  div.hero-buttons {
    button.primary(⚡-call: "trackCTAClick") { Get Started }
    button.secondary { Learn More }
  }
}
```

### Feature Grid (3 Columns)

```markup
div.feature-grid {
  div.feature-card {
    h3 { Feature 1 }
    p { Description of first feature }
  }
  
  div.feature-card {
    h3 { Feature 2 }
    p { Description of second feature }
  }
  
  div.feature-card {
    h3 { Feature 3 }
    p { Description of third feature }
  }
}
```

### Pricing Section

```markup
div.pricing-grid {
  div.pricing-card {
    h3 { Starter }
    p.price { $9/month }
    ul {
      li { Feature 1 }
      li { Feature 2 }
    }
    button(⚡-call: "selectPlan", data-plan: "starter") {
      Choose Plan
    }
  }
  
  div.pricing-card.featured {
    h3 { Professional }
    p.price { $29/month }
    ul {
      li { All Starter features }
      li { Feature 3 }
      li { Feature 4 }
    }
    button(⚡-call: "selectPlan", data-plan: "professional") {
      Choose Plan
    }
  }
  
  div.pricing-card {
    h3 { Enterprise }
    p.price { Custom }
    ul {
      li { Everything }
      li { Dedicated Support }
    }
    button(⚡-call: "contactSales") {
      Contact Sales
    }
  }
}
```

### Footer

```markup
footer.footer {
  div.footer-content {
    div.footer-column {
      h4 { Product }
      a(href: "#") { Features }
      a(href: "#") { Pricing }
      a(href: "#") { Blog }
    }
    
    div.footer-column {
      h4 { Company }
      a(href: "#") { About }
      a(href: "#") { Team }
      a(href: "#") { Careers }
    }
    
    div.footer-column {
      h4 { Legal }
      a(href: "#") { Privacy }
      a(href: "#") { Terms }
    }
  }
  
  div.copyright {
    p { Copyright 2025 MyCompany }
  }
}
```

---

## Troubleshooting

### Issue: "File not found" Error

**Problem:**
```
Error: File 'myfile.htmlx' not found
```

**Solution:**
- Make sure the file exists with `.htmlx` extension
- Check the file is in the current directory or use full path
- Example: `python cli.py C:\path\to\myfile.htmlx output/`

### Issue: CSS Not Applying

**Problem:** Styles don't appear in the browser

**Solutions:**
1. Make sure the CSS file is in the same directory as HTML
2. Clear browser cache (Ctrl+Shift+Delete)
3. Check browser console for errors (F12)
4. Verify classes/IDs match the ones in your .htmlx file

### Issue: Elements Not Displaying

**Problem:** Elements are missing from output

**Solutions:**
1. Check indentation - must use spaces or tabs consistently
2. Verify element names are valid HTML tags
3. Ensure closing braces `}` are proper
4. Check for syntax errors with `--verbose` flag

### Issue: Attributes Not Working

**Problem:** Attributes like `href`, `src` not showing up

**Solutions:**
1. Use correct syntax: `(key: value)`
2. Don't use spaces inside attributes: `(key:"value")` ✓
3. Quote string values: `(href: "link")`
4. Check attribute names are valid

### Issue: Special Characters Not Showing

**Problem:** Text with special characters shows incorrectly

**Solution:**
The compiler automatically handles HTML encoding. Special characters should work fine in text content.

### Issue: Compilation Fails Silently

**Problem:** No error message but nothing compiles

**Solution:**
Use verbose mode to see what's happening:
```bash
python cli.py input.htmlx output/ --verbose
```

### Issue: Classes Not Styling (Classes & IDs Syntax)

**Problem:** Custom classes have no styling

**Common mistake:**
```markup
// Wrong - space between element and class
div .my-class { ... }

// Correct - no space
div.my-class { ... }

// Wrong - space before ID
div #my-id { ... }

// Correct - no space
div#my-id { ... }
```

### Issue: Multiple Attributes Not Working

**Problem:** Only first attribute is parsed

**Solution:**
Ensure proper comma separation:
```markup
// Correct
button(onclick: "action", data-id: "123") { ... }

// Wrong (no comma)
button(onclick: "action" data-id: "123") { ... }
```

---

## Tips for Better HTMLx Code

### Use Semantic HTML

```markup
// Good - semantic
header { Logo }
main { Content }
footer { Copyright }

// Less good - generic
div { Logo }
div { Content }
div { Copyright }
```

### Organize with Comments

```markup
// Header section
header.navbar { ... }

// Main content
main {
  // Hero
  div.hero { ... }
  
  // Features
  div.features { ... }
}

// Footer
footer { ... }
```

### Use Descriptive Class Names

```markup
// Good - clear purpose
div.pricing-card-featured { ... }
button.cta-primary { ... }

// Less good - unclear
div.card1 { ... }
button.btn { ... }
```

### Keep Nesting Reasonable

```markup
// Good - 3 levels
div.container {
  div.card {
    h3 { Title }
  }
}

// Avoid - too deep
div {
  div {
    div {
      div {
        p { Content }
      }
    }
  }
}
```

---

## Next Steps

1. **Create your first page** - Start with a simple landing page
2. **Experiment with classes** - Try different class names
3. **Use the samples** - Check `comprehensive_test.htmlx` for reference
4. **Customize CSS** - Modify generated `styles.css` for your brand
5. **Deploy** - Upload your HTML, CSS, JS to web hosting

---

**Happy HTMLx coding! 🚀**

For more information, see [README.md](README.md) or review the test examples in `tests/unit/test_parser.py`.
