# E-Commerce Website

An Amazon clone built with HTML/CSS/JavaScript for the web and Kivy/KivyMD for the mobile app.

## Features

- **Web Version**: Responsive e-commerce website with product listings, search functionality, and interactive UI
- **Mobile App**: Kivy-based login system with SQLite database

## Project Structure

```
amazon/
├── index.html          # Main e-commerce website
├── style.css           # Styling for the website
├── login.html          # Alternative login page design
├── main.py             # Kivy login application
├── log.py              # Authentication system with database
├── log2.py             # Dashboard with file upload
├── log3.py             # KivyMD login app
├── login.kv            # Kivy login interface
├── dashboard.kv        # Dashboard interface
├── login2.py           # KivyMD dashboard with reports
├── dashboard.py        # Dashboard functionality
├── *.jpg/png           # Image assets
└── users.db            # SQLite database
```

## Requirements

### For Web Version
- Any modern web browser (Chrome, Firefox, Safari, Edge)

### For Kivy App
```
kivy>=2.2.0
kivymd>=1.1.0
```

## Installation

### Install Kivy dependencies:
```bash
pip install kivy kivymd
```

## Running the Application

### Web Version:
Open `amazon/index.html` in any web browser.

### Kivy App:
```bash
cd amazon
python main.py
```

## Deployment

This project can be easily deployed to GitHub Pages for the web version.

1. Create a repository on GitHub
2. Push the `amazon/` folder contents
3. Enable GitHub Pages in repository settings

## License

MIT License

