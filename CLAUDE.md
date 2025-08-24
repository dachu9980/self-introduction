# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal resume website project designed to showcase 沧海's professional background as a private domain operations specialist. The project creates a static HTML website based on resume content and targeted job requirements.

## Key Files

- `docs/resume.md` - Personal resume in Chinese containing career history, skills, and achievements
- `docs/jd.md` - Target job description for 私域运营操盘手 (Private Domain Operations Specialist) position
- `.claude/output-styles/personal-website-developer.md` - Output style configuration for website development workflow

## Development Commands

**Start local development server (preferred):**
```bash
python3 server.py
```
This custom server automatically opens the browser and includes UTF-8 encoding for Chinese content.

**Alternative methods:**
```bash
# Python 3 built-in server
python3 -m http.server 8000

# Python 2 (fallback)
python -m SimpleHTTPServer 8000
```

**Access the website:**
```
http://localhost:8000
```

## Project Architecture

**Static Website Structure:**
- `index.html` - Single-page application with SEO-optimized meta tags
- `styles.css` - Responsive design system with Chinese typography (Noto Sans SC)
- `script.js` - Interactive features: typing animation, counter animations, smooth scrolling
- `server.py` - Custom development server with UTF-8 encoding for Chinese content

**Design System:**
- Color scheme: Blue (#2563eb), Pink (#ec4899), Orange (#f97316)
- Typography: Noto Sans SC for Chinese, Inter/Roboto for English
- Animations: Intersection Observer API for scroll-triggered effects
- Responsive: Mobile-first design with desktop enhancements

## Content Strategy

The website is designed to align 沧海's background with the target position requirements:
- Emphasizes private domain operations experience from entrepreneurial background (2018-present)  
- Highlights team management experience from design director role (2015-2018)
- Showcases relevant skills: community operations, content marketing, data analysis
- Demonstrates cross-functional capabilities combining design and operations expertise

## Deployment Approach

The website is built as a static site that can be:
- Served locally with Python's HTTP server for development
- Deployed to any static hosting platform (GitHub Pages, Netlify, Vercel, etc.)
- Hosted on traditional web servers without server-side requirements