# Selenium Python Hybrid Page Object Model Framework

A lightweight automation framework using **Selenium WebDriver with Python**.  
It follows the **Hybrid Page Object Model (POM)** design pattern, combining data-driven testing, reusable utilities, and rich reporting.

## 🚀 Features
- Page Object Model for clean, reusable code
- Cross-browser support (Chrome, Edge, Firefox, headless)
- Config-driven setup via `config.ini`
- Pytest integration with HTML & Allure reports
- Screenshots on failure for debugging

## ▶️ Run Tests
```bash
pytest -s -v ./testCases/ --browser=edge --headless
