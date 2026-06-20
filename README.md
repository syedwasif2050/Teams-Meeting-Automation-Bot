# 🤖 MS-Teams Automation Engine

A lightweight Python automation tool powered by **Selenium WebDriver**. It automates entering virtual meetings, handling hardware state configuration, and scraping real-time DOM elements to trigger custom chat responses based on specific strings.

## 🔥 Key Capabilities
* **Hardware State Configuration:** Automatically detects and clicks structural elements to mute the microphone and disable the camera before entering the session.
* **Dynamic DOM Scraper:** Implements a continuous conditional polling loop to scrape and parse live chat entries.
* **Targeted String Response:** Actively monitors string streams for predefined user identifiers (e.g., Names, Identification Numbers) to execute instant automated feedback.
* **Session Persistence:** Configured with an isolated user data profile directory to preserve login sessions and prevent repetitive multi-factor authentications.

## 🛠️ Logic & Architecture Pipeline
1. **Implicit/Explicit Structural Waits:** Utilizes `WebDriverWait` paired with `expected_conditions` to handle slow network rendering up to 25 seconds before failing.
2. **De-duplication Tracking:** Employs a local unique string `set()` tracker to prevent execution loops and redundant automated messaging on historically logged data.

## 🚀 Installation & Setup

### 1. Requirements
Install the required browser automation library:
```bash
pip install selenium
