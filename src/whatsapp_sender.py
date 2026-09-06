import json
import time
import urllib.parse
import os
from dotenv import load_dotenv
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_DIR = Path(__file__).resolve().parent.parent

RECIPIENTS_FILE = BASE_DIR / "config" / "recipients.json"
MESSAGE_FILE = BASE_DIR / "config" / "message.txt"

load_dotenv(BASE_DIR / ".env")

WHATSAPP_LOAD_WAIT_SECONDS = int(
    os.getenv("WHATSAPP_LOAD_WAIT_SECONDS", "30")
)

MESSAGE_BOX_WAIT_SECONDS = int(
    os.getenv("MESSAGE_BOX_WAIT_SECONDS", "30")
)

MESSAGE_DELAY_SECONDS = int(
    os.getenv("MESSAGE_DELAY_SECONDS", "7")
)


def load_recipients():
    with open(RECIPIENTS_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data["recipients"]


def load_message():
    with open(MESSAGE_FILE, "r", encoding="utf-8") as file:
        return file.read()


def send_message(driver, phone, message):
    clean_phone = phone.replace("+", "").replace(" ", "")

    encoded_message = urllib.parse.quote(message)

    url = (
        f"https://web.whatsapp.com/send"
        f"?phone={clean_phone}"
        f"&text={encoded_message}"
    )

    driver.get(url)

    print(f"Loading {phone}...")

    wait = WebDriverWait(driver, MESSAGE_BOX_WAIT_SECONDS)

    message_box = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//div[@contenteditable="true"]'
            )
        )
    )

    time.sleep(2)

    message_box.click()
    message_box.send_keys(Keys.ENTER)

    print(f"Message sent to {phone}")

    time.sleep(MESSAGE_DELAY_SECONDS)


def main():
    recipients = load_recipients()
    message = load_message()

    driver = webdriver.Chrome()

    try:
        driver.get("https://web.whatsapp.com")

        print(">>> Scan WhatsApp QR code if required.")
        print(">>> Waiting for WhatsApp Web to load...")

        time.sleep(WHATSAPP_LOAD_WAIT_SECONDS)

        for recipient in recipients:
            phone = recipient["phone"]

            try:
                send_message(driver, phone, message)

            except Exception as error:
                print(f"Failed for {phone}: {error}")

    finally:
        driver.quit()

    print("All done!")


if __name__ == "__main__":
    main()
