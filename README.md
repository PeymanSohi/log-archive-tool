## 🗃️ Log Archiver

**Log Archiver** is a simple and extensible CLI tool to compress and archive logs on a Unix-based system. It helps clean up your system by archiving logs in `.tar.gz` format while keeping track of when each archive was created. You can optionally send email notifications or upload the archive to a remote server.

---

### ✨ Features

- 📁 Compress log directories into `.tar.gz` archives
- 📌 Store archives in a dedicated directory (`/var/log_archives`)
- 🕒 Log each archive creation with a timestamp
- 📧 Optional email notification after archiving
- ☁️ Optional upload of archive to a remote server (via `scp`)

---

### 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/peymansohi/log-archive-tool.git
   cd log-archive-tool
   ```

2. Make the script executable:
   ```bash
   chmod +x log-archive.py
   ```

3. (Optional) Install dependencies:
   - For email notifications: none (built-in `smtplib`)
   - For remote upload: make sure `scp` is installed

---

### ⚙️ Usage

```bash
./log-archive.py <log-directory> [--email <email>] [--remote <user@host:/path>]
```

#### 🔹 Arguments

| Argument         | Description                                                  |
|------------------|--------------------------------------------------------------|
| `<log-directory>`| The directory containing logs you want to archive            |
| `--email`        | (Optional) Send archive notification to this email address   |
| `--remote`       | (Optional) Upload the archive to this SCP destination        |

---

### 📌 Examples

#### ✅ Basic Archive
```bash
./log-archive.py /var/log
```

#### 📧 With Email Notification
```bash
./log-archive.py /var/log --email admin@example.com
```

#### ☁️ With Remote Backup
```bash
./log-archive.py /var/log --remote user@192.168.1.10:/backups
```

#### 🧩 All Features Combined
```bash
./log-archive.py /var/log --email admin@example.com --remote user@host:/path
```

---

### 📄 Archive Output

- Files are stored in: `/var/log_archives`
- Example archive name: `logs_archive_20240816_100648.tar.gz`
- Log of all archives: `/var/log_archives/archive_log.txt`

---

### 🔐 Security Tips

- Avoid hardcoding email credentials in the script.
- Use environment variables or `.env` files for sensitive data.
- For Gmail, consider using [App Passwords](https://support.google.com/accounts/answer/185833).

---

### 📦 To-Do (Improvements)

- [ ] Use `.env` file for config
- [ ] Support multiple log directories
- [ ] Compress logs older than X days
- [ ] Integrate with cloud storage (S3, Google Drive)
- [ ] Add systemd/cron integration

---

https://roadmap.sh/projects/log-archive-tool
