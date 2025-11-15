# Getting Started with htmlxify

Welcome to htmlxify! This guide will get you up and running in 5 minutes.

## 1. Installation (1 minute)

### Option A: Install from TestPyPI (Recommended)

```bash
pip install -i https://test.pypi.org/simple/ htmlxify
```

Done! You can now use the `htmlxify` command.

### Option B: Install from Source (For Development)

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Install in development mode
pip install -e .

# Step 3: Verify it works
htmlxify --version
```

### Option C: Run Python CLI Directly

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the CLI
python cli.py --version
```

## 2. Create Your First File (1 minute)

Create a file called `hello.htmlxify` with this content:

```markup
div#app.container {
  h1.title { Hello World }
  p { Welcome to htmlxify }
  button.primary { Get Started }
}
```

Save it in any directory.

## 3. Compile It (30 seconds)

```bash
# Using installed package (recommended)
htmlxify hello.htmlxify output/

# Or using Python directly
python cli.py hello.htmlxify output/
```

You should see:
```
Compiling hello.htmlxify...
✓ Parsing complete
✓ Validation complete
✓ Generated HTML, CSS, JavaScript
Compilation successful!
```

## 4. View the Result (1 minute)

Open `output/hello.html` in your web browser.

You'll see a styled page with:
- A title "Hello World"
- A subtitle "Welcome to htmlxify"
- A styled button with responsive design

**That's it! You've created your first htmlxify page!** 🎉

---

## Next: Make It Yours

### Add More Content

```markup
div#app.container {
  h1.title { My Website }
  p { Welcome to my site }
  
  div.feature-grid {
    div.feature-card { Feature 1 }
    div.feature-card { Feature 2 }
    div.feature-card { Feature 3 }
  }
  
  button.primary(⚡-call: "trackCTAClick") { Learn More }
}
```

### Add a Navigation Bar

```markup
nav.navbar {
  div.brand { My Company }
  div.nav-links {
    a(href: "/") { Home }
    a(href: "/about") { About }
    a(href: "/contact") { Contact }
  }
}

div.container {
  h1 { Welcome }
  p { Main content }
}
```

### Add a Form

```markup
form {
  div.form-group {
    label(for: "name") { Your Name }
    input(id: "name", type: "text", required: true)
  }
  
  div.form-group {
    label(for: "email") { Email }
    input(id: "email", type: "email", required: true)
  }
  
  button.primary(⚡-call: "submitForm") { Submit }
}
```

### Add Styling

The generated `output/hello.css` contains 650+ lines of responsive styling. To customize:

1. Open `output/hello.css`
2. Find the class you want to change
3. Modify the CSS
4. Refresh browser

For example, to change button color:
```css
button.primary {
  background-color: #0066cc;  /* Change this color */
}
```

---

## Common First Attempts

### A Landing Page

```markup
nav.navbar {
  div.brand { MyStartup }
  div.menu {
    a(href: "#features") { Features }
    a(href: "#pricing") { Pricing }
  }
}

div.hero {
  h1 { Build Faster With htmlxify }
  p { Write less code, ship faster }
  button.primary(⚡-call: "trackCTAClick") { Get Started }
}

div.container {
  h2 { Features }
  
  div.feature-grid {
    div.feature-card {
      h3 { Fast }
      p { Compiles instantly }
    }
    div.feature-card {
      h3 { Simple }
      p { Easy syntax }
    }
    div.feature-card {
      h3 { Powerful }
      p { Full control }
    }
  }
}

footer.footer {
  p { Copyright 2025 }
}
```

### A Portfolio Page

```markup
header.navbar {
  div.brand { John Doe }
}

div.hero {
  h1 { Welcome }
  p { Designer & Developer }
}

div.container {
  h2 { My Work }
  
  div.feature-grid {
    div.feature-card {
      h3 { Project 1 }
      p { Description }
    }
    div.feature-card {
      h3 { Project 2 }
      p { Description }
    }
  }
}

footer {
  p { Contact: john@example.com }
}
```

### A Product Page

```markup
div.container {
  h1 { Our Product }
  
  div.product-card {
    img(src: "product.jpg", alt: "Product")
    
    h2 { Product Name }
    p.price { $99.99 }
    p { Detailed product description }
    
    button.primary(⚡-call: "selectPlan") { Buy Now }
  }
}
```

---

## Syntax Quick Tips

### Elements
```markup
div { content }           // Container
p { text }               // Paragraph
h1 { heading }           // Heading
button { click me }      // Button
```

### Classes & IDs
```markup
div.container { ... }    // Add class
div#main { ... }         // Add ID
div.class1.class2 { ... }// Multiple classes
```

### Attributes
```markup
a(href: "url") { ... }                    // With URL
input(type: "email", placeholder: "Email") // Multiple
button(disabled: true) { ... }            // Boolean
```

### Special Features
```markup
button(⚡-call: "trackClick") { ... }     // Track clicks
div(⚡-data: "myData") { ... }            // Data binding
```

---

## Common Questions

**Q: Do I need to install anything to use htmlxify?**
A: Yes, install from TestPyPI: `pip install -i https://test.pypi.org/simple/ htmlxify`

**Q: Do I need Python?**
A: Yes, Python 3.8+ is required to run htmlxify.

**Q: Can I customize the CSS?**
A: Yes! Modify the generated `.css` file directly.

**Q: Can I add my own JavaScript?**
A: Yes! The generated `.js` file can be edited.

**Q: How do I deploy my site?**
A: Upload the `.html`, `.css`, and `.js` files to any web hosting.

**Q: Do I need a backend server?**
A: No! htmlxify uses mock data. For real API calls, set up a backend.

**Q: Can I use different colors/fonts?**
A: Yes! Edit the CSS file to customize the look.

---

## Troubleshooting

### Error: File not found
```bash
# Make sure file has .htmlxify extension
htmlxify myfile.htmlxify output/
# or
python cli.py myfile.htmlxify output/
```

### Styles don't appear
```bash
# Check browser cache with F12 (Developer Tools)
# Clear cache and refresh
# Make sure CSS file is in same folder as HTML
```

### Syntax error in markup
```bash
# Use verbose mode to see details
htmlxify myfile.htmlxify output/ --verbose
# or
python cli.py myfile.htmlxify output/ --verbose

# Common mistakes:
# ❌ div .container (space before dot)
# ✓  div.container (no space)
```

---

## Resources

- **[README.md](README.md)** - Full documentation
- **[HOW_TO_USE.md](HOW_TO_USE.md)** - Complete guide
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Syntax cheat sheet
- **[example.htmlxify](example.htmlxify)** - Full example

---

## Your Learning Path

### Day 1: Basics
- ✓ Download/Install compiler
- ✓ Create first `.htmlxify` file
- ✓ Learn element syntax
- ✓ Try different HTML tags

### Day 2: Styling
- ✓ Learn classes and IDs
- ✓ Understand auto-generated CSS
- ✓ Customize colors and fonts
- ✓ Create styled layouts

### Day 3: Advanced
- ✓ Add forms and inputs
- ✓ Use interactive features (⚡-call)
- ✓ Create multi-section pages
- ✓ Build a full landing page

### Week 2+: Mastery
- ✓ Build portfolio/blog pages
- ✓ Create complex layouts
- ✓ Optimize CSS for performance
- ✓ Deploy to web hosting

---

## 5-Minute Project Ideas

1. **Hello Page** (5 min)
   - Single div with heading and button
   
2. **Feature Cards** (10 min)
   - Hero section + 3 feature cards
   
3. **Contact Form** (15 min)
   - Form with name, email, message fields
   
4. **Mini Portfolio** (20 min)
   - Nav + Hero + 3 projects + Footer
   
5. **Pricing Page** (25 min)
   - 3 pricing tiers with compare table

---

## Now You're Ready!

Pick one of the ideas above and start building. The best way to learn is by doing!

**Happy htmlxify coding!** 🚀

For help, check [HOW_TO_USE.md](HOW_TO_USE.md) or the [QUICK_REFERENCE.md](QUICK_REFERENCE.md).

---

## Next: Make It Yours

### Add More Content

```markup
div#app.container {
  h1.title { My Website }
  p { Welcome to my site }
  
  div.feature-grid {
    div.feature-card { Feature 1 }
    div.feature-card { Feature 2 }
    div.feature-card { Feature 3 }
  }
  
  button.primary(⚡-call: "trackCTAClick") { Learn More }
}
```

### Add a Navigation Bar

```markup
nav.navbar {
  div.brand { My Company }
  div.nav-links {
    a(href: "/") { Home }
    a(href: "/about") { About }
    a(href: "/contact") { Contact }
  }
}

div.container {
  h1 { Welcome }
  p { Main content }
}
```

### Add a Form

```markup
form {
  div.form-group {
    label(for: "name") { Your Name }
    input(id: "name", type: "text", required: true)
  }
  
  div.form-group {
    label(for: "email") { Email }
    input(id: "email", type: "email", required: true)
  }
  
  button.primary(⚡-call: "submitForm") { Submit }
}
```

### Add Styling

The generated `output/hello.css` contains 650+ lines of styling. To customize:

1. Open `output/hello.css`
2. Find the class you want to change
3. Modify the CSS
4. Refresh browser

For example, to change button color:
```css
button {
  background-color: #0066cc;  /* Change this color */
}
```

---

## Common First Attempts

### A Landing Page

```markup
nav.navbar {
  div.brand { MyStartup }
  div.menu {
    a(href: "#features") { Features }
    a(href: "#pricing") { Pricing }
  }
}

div.hero {
  h1 { Build Faster With htmlxify }
  p { Write less code, ship faster }
  button.primary(⚡-call: "trackCTAClick") { Get Started }
}

div.container {
  h2 { Features }
  
  div.feature-grid {
    div.feature-card {
      h3 { Fast }
      p { Compiles instantly }
    }
    div.feature-card {
      h3 { Simple }
      p { Easy syntax }
    }
    div.feature-card {
      h3 { Powerful }
      p { Full control }
    }
  }
}

footer.footer {
  p { Copyright 2025 }
}
```

### A Portfolio Page

```markup
header.navbar {
  div.brand { John Doe }
}

div.hero {
  h1 { Welcome }
  p { Designer & Developer }
}

div.container {
  h2 { My Work }
  
  div.feature-grid {
    div.feature-card {
      h3 { Project 1 }
      p { Description }
    }
    div.feature-card {
      h3 { Project 2 }
      p { Description }
    }
  }
}

footer {
  p { Contact: john@example.com }
}
```

### A Product Page

```markup
div.container {
  h1 { Our Product }
  
  div.product-card {
    img(src: "product.jpg", alt: "Product")
    
    h2 { Product Name }
    p.price { $99.99 }
    p { Detailed product description }
    
    button.primary(⚡-call: "selectPlan") { Buy Now }
  }
}
```

---

## Syntax Quick Tips

### Elements
```markup
div { content }           // Container
p { text }               // Paragraph
h1 { heading }           // Heading
button { click me }      // Button
```

### Classes & IDs
```markup
div.container { ... }    // Add class
div#main { ... }         // Add ID
div.class1.class2 { ... }// Multiple classes
```

### Attributes
```markup
a(href: "url") { ... }                    // With URL
input(type: "email", placeholder: "Email") // Multiple
button(disabled: true) { ... }            // Boolean
```

### Special Features
```markup
button(⚡-call: "trackClick") { ... }     // Track clicks
div(⚡-data: "myData") { ... }            // Data binding
```

---

## Common Questions

**Q: Do I need to install Node.js?**
A: No! htmlxify uses Python. Make sure Python 3.x is installed.

**Q: Can I customize the CSS?**
A: Yes! Modify the generated `.css` file directly.

**Q: Can I add my own JavaScript?**
A: Yes! The generated `.js` file can be edited.

**Q: How do I deploy my site?**
A: Upload the `.html`, `.css`, and `.js` files to any web hosting.

**Q: Do I need a backend server?**
A: No! htmlxify uses mock data. For real API calls, you'll need a backend.

**Q: Can I use different colors/fonts?**
A: Yes! Edit the CSS file to customize the look.

---

## Troubleshooting

### Error: File not found
```bash
# Make sure file has .htmlxify extension and is in current directory
python cli.py myfile.htmlxify output/
```

### Styles don't appear
```bash
# Check browser cache with F12 (Developer Tools)
# Clear cache and refresh
# Make sure CSS file is in same folder as HTML
```

### Syntax error in markup
```bash
# Use verbose mode to see details
python cli.py myfile.htmlxify output/ --verbose

# Common mistakes:
# ❌ div .container (space before dot)
# ✓  div.container (no space)
```

---

## Resources

- **[README.md](README.md)** - Full documentation
- **[HOW_TO_USE.md](HOW_TO_USE.md)** - Complete guide
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Syntax cheat sheet
- **[comprehensive_test.htmlxify](comprehensive_test.htmlxify)** - Full example

---

## Your Learning Path

### Day 1: Basics
- ✓ Install compiler
- ✓ Create first `.htmlxify` file
- ✓ Learn element syntax
- ✓ Try different HTML tags

### Day 2: Styling
- ✓ Learn classes and IDs
- ✓ Understand auto-generated CSS
- ✓ Customize colors and fonts
- ✓ Create styled layouts

### Day 3: Advanced
- ✓ Add forms and inputs
- ✓ Use interactive features (⚡-call)
- ✓ Create multi-section pages
- ✓ Build a full landing page

### Week 2+: Mastery
- ✓ Build portfolio/blog pages
- ✓ Create complex layouts
- ✓ Optimize CSS for performance
- ✓ Deploy to web hosting

---

## 5-Minute Project Ideas

1. **Hello Page** (5 min)
   - Single div with heading and button
   
2. **Feature Cards** (10 min)
   - Hero section + 3 feature cards
   
3. **Contact Form** (15 min)
   - Form with name, email, message fields
   
4. **Mini Portfolio** (20 min)
   - Nav + Hero + 3 projects + Footer
   
5. **Pricing Page** (25 min)
   - 3 pricing tiers with compare table

---

## Now You're Ready!

Pick one of the ideas above and start building. The best way to learn is by doing!

**Happy htmlxify coding!** 🚀

For help, check [HOW_TO_USE.md](HOW_TO_USE.md) or the [QUICK_REFERENCE.md](QUICK_REFERENCE.md).
