# WhatsApp Message Automation

A simple Python + Selenium tool to send a predefined WhatsApp message to multiple recipients through WhatsApp Web.

The goal is simple:

**Clone → Configure → Execute**

---

## ⚠️ Important

This project uses Selenium to automate WhatsApp Web.

Use it responsibly and only send messages to people you are authorized to contact. Avoid spam, bulk unsolicited messaging, or behavior that may violate WhatsApp's terms.

**Never commit sensitive personal information to a public repository.**

---

## Requirements

* Python 3.10+
* Google Chrome
* A WhatsApp account
* Internet connection

---

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/whatsapp-message-automation.git
cd whatsapp-message-automation
```

---

## 2. Create a Virtual Environment

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 4. Configure Your Message and Recipients

The required configuration files are already included in the repository:

```text
config/
├── message.txt
└── recipients.json
```

### `config/message.txt`

Open this file and replace the example message with the message you want to send.

Example:

```text
Hello,

This is my message.

Thank you.
```

### `config/recipients.json`

Add the WhatsApp phone numbers you want to contact.

Example:

```json
{
  "recipients": [
    {
      "phone": "+911234567890"
    },
    {
      "phone": "+91XXXXXXXXXX"
    }
  ]
}
```

Use the international phone number format.

For example:

```text
+911234567890
```

Do not include spaces, brackets, or dashes.

---

## 5. Configure Timing

Create a `.env` file in the project root.

```text
WHATSAPP_LOAD_WAIT_SECONDS=30
MESSAGE_BOX_WAIT_SECONDS=30
MESSAGE_DELAY_SECONDS=7
```

### What do these mean?

| Setting                      | Purpose                                  | Default |
| ---------------------------- | ---------------------------------------- | ------: |
| `WHATSAPP_LOAD_WAIT_SECONDS` | Time to wait for WhatsApp Web / QR login |  30 sec |
| `MESSAGE_BOX_WAIT_SECONDS`   | Maximum time to wait for the message box |  30 sec |
| `MESSAGE_DELAY_SECONDS`      | Delay between messages                   |   7 sec |

You normally don't need to change these values.

---

## 6. Run the Automation

Make sure your virtual environment is activated, then run:

```bash
python3 src/whatsapp_sender.py
```

The program will:

1. Open Google Chrome.
2. Open WhatsApp Web.
3. Ask you to scan the QR code if required.
4. Load the configured recipients.
5. Load your message.
6. Send the message to each recipient.
7. Close Chrome when finished.

---

## Project Structure

```text
whatsapp-message-automation/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── config/
│   ├── message.txt
│   └── recipients.json
│
└── src/
    └── whatsapp_sender.py
```

---

## Troubleshooting

### `ModuleNotFoundError: No module named 'dotenv'`

Make sure your virtual environment is activated and run:

```bash
pip install -r requirements.txt
```

Or:

```bash
python -m pip install python-dotenv
```

---

### WhatsApp Web does not load

Make sure:

* Google Chrome is installed.
* You have an active internet connection.
* You can access WhatsApp Web normally.
* You have scanned the QR code when requested.

---

### Message box timeout

If WhatsApp Web is slow to load, increase:

```text
MESSAGE_BOX_WAIT_SECONDS=60
```

---

### QR code takes longer to scan

Increase:

```text
WHATSAPP_LOAD_WAIT_SECONDS=60
```

---

## Security

Do **not** commit sensitive information such as:

* Private phone numbers
* Personal or confidential messages
* `.env`
* Passwords
* API keys
* Credentials
* Browser session data

The real `.env` file should remain local.

---

## Responsible Use

This project is intended for personal automation and legitimate communication.

You are responsible for:

* Having permission to contact recipients.
* Using appropriate messages.
* Following WhatsApp's rules and policies.
* Avoiding spam or unwanted bulk messaging.

---

## License

Choose an appropriate license for your project before publishing it publicly.

