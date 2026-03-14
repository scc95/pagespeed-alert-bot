# PageSpeed Alert Bot

[![PageSpeed Monitor](https://github.com/scc95/pagespeed-alert-bot/actions/workflows/monitor.yml/badge.svg)](https://github.com/scc95/pagespeed-alert-bot/actions/workflows/monitor.yml)

Automated website performance monitoring tool built with Python and GitHub Actions. This bot tracks Google PageSpeed Insights and sends real-time alerts to Discord whenever performance scores dip below a set threshold.

## Features
- **Automated Scanning:** Runs on a schedule (every hour) with GitHub Actions.
- **Instant Alerts:** Sends detailed notifications to Discord via Webhooks.
- **CSV Logging:** Generates a sitewarnings.csv to track performance dips over time.
- **Secure:** Uses GitHub Secrets to manage API keys and Webhook URLs safely.

## Built With
- **Python 3.10**
- **Google PageSpeed Insights API v5**
- **GitHub Actions** (CI/CD & Scheduling)
- **Discord Webhooks**

## Setup and Installation

### 1. Prerequisites
You will need:
- A Google PageSpeed API Key.
- A Discord Channel Webhook URL.

### 2. Configuration
To run this in your own GitHub environment:
1. Fork or clone this repository.
2. Go to Settings > Secrets and variables > Actions.
3. Create two new repository secrets:
   - apikey: Your Google PageSpeed API Key.
   - webhook_url: Your Discord Webhook URL.

### 3. Usage
The bot is set to run automatically every hour. You can also trigger it manually:
- Go to the Actions tab.
- Select PageSpeed Monitor.
- Click Run workflow.

## Project Structure
- monitor.py: The core for API requests and Discord alerts.
- requirements.txt: Python dependencies.
- .github/workflows/monitor.yml: The GitHub Actions configuration.
