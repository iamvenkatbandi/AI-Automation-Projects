from gmail import (
    get_gmail_service,
    get_unread_messages,
    read_message,
    send_reply,
    mark_as_read
)
from ai import classify_email, generate_reply
from logger import setup_logger

import re
import time
import os
import logging


PROCESSED_FILE = "processed_emails.txt"


def extract_email(sender):
    """
    Extract clean email from sender string
    Example:
    'John Doe <john@gmail.com>' → 'john@gmail.com'
    """
    match = re.search(r'<(.+?)>', sender)
    return match.group(1) if match else sender


def load_processed_ids():
    """Load already processed email IDs"""
    if not os.path.exists(PROCESSED_FILE):
        return set()

    with open(PROCESSED_FILE, "r") as f:
        return set(line.strip() for line in f.readlines())


def save_processed_id(msg_id):
    """Save processed email ID to avoid duplicates"""
    with open(PROCESSED_FILE, "a") as f:
        f.write(msg_id + "\n")


def is_valid_email(sender, body):
    """
    Basic filtering before AI processing
    """
    if not sender or not body:
        return False

    sender_lower = sender.lower()

    # ❌ Ignore no-reply emails
    if "no-reply" in sender_lower or "noreply" in sender_lower:
        return False

    # ❌ Ignore very short emails
    if len(body.strip()) < 10:
        return False

    return True


def main():
    # ✅ Setup logging
    setup_logger()
    logging.info("🚀 Starting AI Email Auto-Responder")

    try:
        service = get_gmail_service()
    except Exception as e:
        logging.error(f"❌ Gmail connection failed: {str(e)}")
        return

    try:
        messages = get_unread_messages(service)
    except Exception as e:
        logging.error(f"❌ Failed to fetch emails: {str(e)}")
        return

    if not messages:
        logging.info("📭 No new unread emails.")
        return

    processed_ids = load_processed_ids()

    for msg in messages:
        try:
            msg_id = msg.get('id')

            if not msg_id:
                continue

            # 🚫 Skip already processed
            if msg_id in processed_ids:
                logging.info(f"⏩ Skipping processed email: {msg_id}")
                continue

            # 📥 Read email
            subject, sender, body = read_message(service, msg_id)

            logging.info(f"📩 Processing | Subject: {subject} | Sender: {sender}")

            # 🚫 Basic validation
            if not is_valid_email(sender, body):
                logging.info("⚠️ Skipped invalid email")
                mark_as_read(service, msg_id)
                save_processed_id(msg_id)
                continue

            # 📧 Extract clean receiver email
            receiver = extract_email(sender)

            # 🧠 AI Classification
            try:
                category = classify_email(body)
                category = category.strip().lower()
                logging.info(f"🧠 Category: {category}")
            except Exception as e:
                logging.error(f"❌ Classification failed: {str(e)}")
                continue

            # 🚫 Smart AI Filtering (IMPORTANT)
            if category == "ignore":
                logging.info("🚫 Ignored by AI (not important)")
                mark_as_read(service, msg_id)
                save_processed_id(msg_id)
                continue

            # ✍️ Generate AI reply
            try:
                reply = generate_reply(body, category)
            except Exception as e:
                logging.error(f"❌ Reply generation failed: {str(e)}")
                continue

            # 📤 Send reply
            try:
                send_reply(service, receiver, subject, reply)
            except Exception as e:
                logging.error(f"❌ Failed to send reply: {str(e)}")
                continue

            # ✅ Mark as read
            mark_as_read(service, msg_id)

            # 💾 Save processed ID
            save_processed_id(msg_id)

            logging.info(f"✅ Replied successfully to {receiver}")

            # ⏳ Prevent rate limit
            time.sleep(5)

        except Exception as e:
            logging.error(f"❌ Unexpected error: {str(e)}")

    logging.info("✅ Cycle completed\n")


if __name__ == "__main__":
    main()
