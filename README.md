
![CI Status](https://github.com/bvsuhas/automation-framework-suhas-/actions/workflows/test.yml/badge.svg)

# Automation Framework – Suhas

![CI](https://github.com/your-username/automation-framework-suhas/actions/workflows/behave.yml/badge.svg)

This framework uses Behave + Selenium + Allure for login validation...

:wq!
# automation-framework-suhas-
Selenium + API + Cucumber BDD framework for web and backend testing 


# Automation Framework - Selenium + API + Cucumber

This repository contains a modular automation framework built using **Selenium WebDriver**, **RestAssured**, and **Cucumber BDD**. It supports both UI and API testing, designed for scalability, readability, and CI/CD integration.


- Cucumber (BDD)
# Python Automation Framework - Selenium + API + Behave (BDD)

This repository contains a modular Python automation framework using **Selenium WebDriver**, **Requests**, and **Behave** for BDD-style testing. It supports both UI and API testing and is designed for scalability, readability, and CI/CD integration.

## 🧰 Tech Stack
- Python 3.x
- Selenium WebDriver
- Behave (BDD)
- Requests (API Testing)
- PyTest (optional for API)
- pytest-html (Reporting)
- GitHub Actions / Jenkins (CI/CD)



## 📁 Project Structure
automation_framework/
├── features/
│   ├── login.feature
│   └── steps/
│       └── login_steps.py
├── pages/
│   └── login_page.py
├── tests/
│   └── test_api_login.py
├── utils/
│   └── config.py
├── conftest.py
├── requirements.txt
└── README.md


## 🚀 Getting Started
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/automation-framework-suhas.git
   
   cd automation-framework-suhas

#Bash

pip install -r requirements.txt

#Bash

behave

#Run Api test
pytest tests/test_api_login.py --html=report.html
