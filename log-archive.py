#!/usr/bin/env python3

import os
import sys
import tarfile
import datetime
import smtplib
import subprocess
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import argparse

ARCHIVE_DIR = "/var/log_archives"
LOG_FILE = os.path.join(ARCHIVE_DIR, "archive_log.txt")


def create_archive_dir():
    os.makedirs(ARCHIVE_DIR, exist_ok=True)


def get_timestamp():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def archive_logs(log_dir):
    timestamp = get_timestamp()
    archive_name = f"logs_archive_{timestamp}.tar.gz"
    archive_path = os.path.join(ARCHIVE_DIR, archive_name)

    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(log_dir, arcname=os.path.basename(log_dir))

    log_archive_action(archive_name)
    return archive_path


def log_archive_action(archive_name):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - Created archive: {archive_name}\n")


def send_email_notification(to_email, archive_path):
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Log Archive Completed"
    msg["From"] = sender_email
    msg["To"] = to_email

    text = f"The log archive has been created:\n{archive_path}"
    msg.attach(MIMEText(text, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        print("[✓] Email sent to", to_email)
    except Exception as e:
        print("[!] Failed to send email:", e)


def upload_to_remote(archive_path, remote):
    try:
        subprocess.run(["scp", archive_path, remote], check=True)
        print("[✓] Uploaded to remote server:", remote)
    except subprocess.CalledProcessError as e:
        print("[!] Remote upload failed:", e)


def main():
    parser = argparse.ArgumentParser(description="Log Archiver Tool")
    parser.add_argument("log_directory", help="Directory containing logs to archive")
    parser.add_argument("--email", help="Email address to notify after archiving")
    parser.add_argument("--remote", help="Remote scp destination (e.g. user@host:/path)")
    args = parser.parse_args()

    log_dir = args.log_directory

    if not os.path.exists(log_dir):
        print(f"[!] Log directory '{log_dir}' does not exist.")
        sys.exit(1)

    create_archive_dir()
    archive_path = archive_logs(log_dir)

    if args.email:
        send_email_notification(args.email, archive_path)

    if args.remote:
        upload_to_remote(archive_path, args.remote)


if __name__ == "__main__":
    main()
