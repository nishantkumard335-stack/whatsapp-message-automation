# WhatsApp Message Automation

Simple Python automation to send a predefined WhatsApp message to a list of authorized recipients using WhatsApp Web.

## 🚀 Quick Start

You only need to do **3 things**:

1. Install the application
2. Configure recipients and message
3. Run the application

No Python coding is required.

---

# 1. Requirements

You need:

* Python 3.10 or newer
* Google Chrome
* A WhatsApp account
* Access to WhatsApp Web

---

# 2. Download the Project

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/whatsapp-message-automation.git
```

Go into the project:

```bash
cd whatsapp-message-automation
```

---

# 3. Create Python Environment

Run:

```bash
python3 -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

# 4. Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

---

# 5. Configure the Application

Go to the `config` folder.

You will find:

```text
config/
├── recipients.example.csv
└── message.example.txt
```

Create your personal configuration files.

### Create recipients file

Copy:

```bash
cp config/recipients.example.csv config/recipients.csv
```

### Create message file

Copy:

```bash
cp config/message.example.txt config/message.txt
```

Your folder will now look like:

```text
config/
├── recipients.csv
├── recipients.example.csv
├── message.txt
└── message.example.txt
```

---

# 6. Add Recipients

Open:

```text
config/recipients.csv
```

Use this format:

```csv
name,phone
John,+919999999999
Ramesh,+918888888888
Suresh,+917777777777
```

### Important

* Include the country code.
* Do not include spaces in phone numbers.
* Do not add `+` more than once.
* Use only recipients you are authorized to contact.

For India:

```text
+91XXXXXXXXXX
```

Example:

```csv
name,phone
John,+919999999999
```

---

# 7. Add Your Message

Open:

```text
config/message.txt
```

Paste the message you want to send.

For example:

```text
Hi,

This is a test message.

Thank you.
```

You can use multiple lines.

---

# 8. Configure Timing

The `.env.example` file contains the default timing settings.

Create your local `.env`:

```bash
cp .env.example .env
```

The default settings are:

```env
WHATSAPP_LOAD_WAIT_SECONDS=30
MESSAGE_BOX_WAIT_SECONDS=30
MESSAGE_DELAY_SECONDS=7
```

### What do these mean?

| Setting                      | Meaning                         | Default |
| ---------------------------- | ------------------------------- | ------: |
| `WHATSAPP_LOAD_WAIT_SECONDS` | Wait after opening WhatsApp Web |  30 sec |
| `MESSAGE_BOX_WAIT_SECONDS`   | Maximum wait for message box    |  30 sec |
| `MESSAGE_DELAY_SECONDS`      | Wait before next recipient      |   7 sec |

For example:

```env
MESSAGE_DELAY_SECONDS=10
```

means the application waits 10 seconds between recipients.

---

# 9. Run the Application

Run:

```bash
python3 src/whatsapp_sender.py
```

Chrome will open WhatsApp Web.

If WhatsApp asks for authentication, scan the QR code using your phone.

The application will then process the configured recipients.

---

# 📁 Project Structure

```text
whatsapp-message-automation/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── config/
│   ├── recipients.csv          # Your recipients - LOCAL ONLY
│   ├── recipients.example.csv  # Example
│   ├── message.txt             # Your message - LOCAL ONLY
│   └── message.example.txt     # Example
│
└── src/
    └── whatsapp_sender.py
```

---

# 🔐 Security

Never upload the following to GitHub:

```text
.env
config/recipients.csv
config/message.txt
```

These files may contain private information.

The repository is configured to ignore them automatically.

Before pushing changes, check:

```bash
git status
```

---

# ⚠️ Responsible Use

Use this automation only for recipients you are authorized to contact.

Do not use it for spam, unsolicited bulk messaging, or activity that violates WhatsApp's applicable terms or policies.

---

# 🛠 Troubleshooting

## `ModuleNotFoundError: No module named 'dotenv'`

Run:

```bash
pip install -r requirements.txt
```

## Chrome does not open

Make sure Google Chrome is installed and updated.

## WhatsApp asks for QR authentication

Scan the QR code displayed by WhatsApp Web.

## Message box is not found

Increase:

```env
MESSAGE_BOX_WAIT_SECONDS=45
```

Then run the application again.

## WhatsApp Web loads slowly

Increase:

```env
WHATSAPP_LOAD_WAIT_SECONDS=45
```

---

# License

For personal/internal automation use.

