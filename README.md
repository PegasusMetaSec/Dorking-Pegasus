<img width="1024" height="1024" alt="WhatsApp Image 2026-04-15 at 22 45 12" src="https://github.com/user-attachments/assets/7a0659b3-4232-4747-8410-53f081f5a9d3" />


# DORKING PEGASUS
[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/yourusername/dorking-pegasus)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

> **Advanced Google Dorking Automation Tool** – Discover hidden vulnerabilities, exposed data, and misconfigurations with the power of Pegasus.

<img width="1919" height="723" alt="Screenshot 2026-04-15 224851" src="https://github.com/user-attachments/assets/2e9e87bd-704b-4088-8cbe-3b1b02e0764f" />

---

## 📖 Overview

**DORKING PEGASUS** adalah alat canggih untuk melakukan pencarian menggunakan *Google dorks* secara otomatis, sistematis, dan efisien.  
Dirancang untuk para profesional keamanan siber, bug hunter, dan tim red team dalam mengidentifikasi:

- 🔓 File sensitif terekspos (`config`, `env`, `sql`, `log`)
- 📁 Direktori terbuka (open directory listing)
- 🛠 Panel admin tanpa autentikasi
- 📊 Database error & SQL injection points
- 🧠 Informasi melalui OSINT (email, user, dokumen)

> ⚠️ *Hanya untuk penggunaan etis dan legal. Gunakan di sistem yang Anda miliki atau memiliki izin tertulis.*

---

## ✨ Fitur Utama

| Fitur | Deskripsi |
|-------|------------|
| 🗂 **100+ Dork Templates** | Kategori: `database`, `admin panel`, `file sensitif`, `cctv`, `email`, `ftp` |
| 🧠 **Custom Dork Builder** | Buat dork sendiri dengan parameter dinamis |
| 🎯 **Domain Filtering** | Target spesifik domain atau subdomain |
| 🧹 **Auto-filter Duplicate** | Hindari hasil duplikat dengan hash URL |
| 📄 **Multi-Format Export** | JSON, CSV, HTML, TXT |
| 🕵️‍♂️ **User-Agent Rotator** | Hindari blokir Google |
| ⏱ **Delay & Randomized Timing** | Bypass rate limiting |
| 🌐 **Proxy Support** | HTTP/HTTPS/SOCKS5 |
| 🖥 **CLI + Web Dashboard (optional)** | Monitor hasil secara realtime |

---

## 🖼 Preview

```bash
$ python pegasus.py --domain example.com --dork admin_login

[✓] Target: example.com
[✓] Dork used: intitle:"admin login" site:example.com
[➜] Scraping Google results...
[✓] Found 14 unique URLs
[!] Sensitive findings: 2
   - https://example.com/admin/config.php (exposed credentials)
   - https://example.com/backup/db.sql
[✓] Report saved: reports/example_com_20250218.json
