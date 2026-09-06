# WhatsApp Message Automation

Python Selenium automation for sending predefined WhatsApp messages to authorized recipients through WhatsApp Web.

## Overview

This project uses Selenium WebDriver to automate message entry and sending through WhatsApp Web.

The project keeps application code separate from recipient data and message content.

## Features

* Selenium-based WhatsApp Web automation
* Multiple recipient support
* External recipient configuration
* External message template
* Local configuration kept outside Git
* Simple Python project structure

## Requirements

* Python 3.10+
* Google Chrome
* A WhatsApp account
* Selenium

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/whatsapp-message-automation.git
cd whatsapp-message-automation
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create the local recipient configuration:

```bash
cp config/recipients.example.json config/recipients.json
```

Edit the file and add only recipients you are authorized to contact.

Create the local message file:

```bash
touch config/message.txt
```

Add your message to `config/message.txt`.

The following local files are intentionally excluded from Git:

* `config/recipients.json`
* `config/message.txt`
* `.env`

## Running

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Run:

```bash
python src/whatsapp_sender.py
```

WhatsApp Web will open in Chrome. Scan the QR code when prompted.

## Project Structure

```text
whatsapp-message-automation/
├── src/
│   └── whatsapp_sender.py
├── config/
│   └── recipients.example.json
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Security

Do not commit:

* Phone numbers
* Personal contact information
* Message content containing private information
* Passwords
* API keys
* Authentication/session files
* Browser profiles containing sensitive data

Always review `git status` before committing changes.

## Responsible Use

Use this automation only for recipients you are authorized to contact and in accordance with WhatsApp's applicable terms and policies.

## License

This project is intended for personal/internal automation use.

