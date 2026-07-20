# 📱 HackPath Phone Analyzer v2

> **6-in-1 Phone number analysis toolkit**
> Created by **Sachin Ser** | HackPath

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://python.org)
[![Version](https://img.shields.io/badge/Version-2.0-purple?style=flat-square)](https://github.com/sachin-null/hackpath-phone-analyzer)
[![Platform](https://img.shields.io/badge/Platform-Termux%20|%20Linux%20|%20Kali-orange?style=flat-square)](https://github.com/sachin-null)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![HackPath](https://img.shields.io/badge/HackPath-CEH%20v12-red?style=flat-square)](https://github.com/sachin-null/hackpath)

---

## ⚡ All 6 Tools

| # | Tool | Features |
|---|------|---------|
| 1 | 🔍 **Analyze Number** | Country · Carrier · State · Formats · Online links |
| 2 | 📁 **Bulk Analyze** | File input · Stats · Country/Carrier summary |
| 3 | 🌍 **Country Lookup** | 100+ countries · Search by name or code |
| 4 | 📡 **India Carrier** | Airtel/Jio/Vi/BSNL · State/Region |
| 5 | 📋 **Number Formatter** | E.164 · International · National · All formats |
| 6 | 🔎 **Spam Check Links** | Truecaller · ShouldIAnswer · CallerInfo · Google |

---

## 📌 What's New in v2?

- Number Formatter tool (NEW)
- Spam Check Links (NEW)
- India Carrier Lookup standalone (NEW)
- Bulk analyze stats (Country + Carrier summary)
- More India carrier prefixes (Airtel/Jio/Vi/BSNL)
- More India states coverage
- More country codes (150+)
- Carrier color coding in output
- Better number format detection

---

## 📲 Install & Run

### Termux (Android)
```bash
pkg install python git -y
git clone https://github.com/sachin-null/hackpath-phone-analyzer
cd hackpath-phone-analyzer
python3 phone_analyzer.py
```

### Kali Linux / Linux
```bash
git clone https://github.com/sachin-null/hackpath-phone-analyzer
cd hackpath-phone-analyzer
python3 phone_analyzer.py
```

### One Line (Termux)
```bash
pkg install python git -y && git clone https://github.com/sachin-null/hackpath-phone-analyzer && cd hackpath-phone-analyzer && python3 phone_analyzer.py
```

---

## 🖥️ Menu

```
  MENU
  [1] Analyze Phone Number
  [2] Bulk Analyze (from file)
  [3] Country Code Lookup
  [4] India Carrier Lookup
  [5] Number Formatter
  [6] Spam Check Links
  [0] Exit

  HackPath Phone >
```

---

## 🔍 Sample Output

```
  FORMAT ANALYSIS
  Input                   : +919447123456
  Country Code            : +91
  Country                 : India
  Local Number            : 9447123456

  INDIA ANALYSIS
  Number (10d)            : 9447123456
  Carrier                 : BSNL
  State/Region            : Kerala
  Type                    : Mobile
  Format                  : Valid

  NUMBER FORMATS
  E.164                   : +919447123456
  International           : +91 9447123456
  National (00)           : 00919447123456
  Local only              : 9447123456
```

---

## 📁 Bulk Analyze Format

Input file (one number per line):
```
+919447123456
+14155552671
+447911123456
9820123456
```

Output CSV:
```
Input|Code|Country|Local|Carrier|State
+919447123456|+91|India|9447123456|BSNL|Kerala
+14155552671|+1|USA/Canada|4155552671|N/A|N/A
```

---

## 🌍 Supported Countries

100+ countries including:
- 🇮🇳 India (+91) — with carrier & state detection
- 🇺🇸 USA/Canada (+1)
- 🇬🇧 UK (+44)
- 🇦🇺 Australia (+61)
- 🇯🇵 Japan (+81)
- 🇨🇳 China (+86)
- 🇩🇪 Germany (+49)
- And 100+ more!

---

## 📡 India Carriers Detected

| Carrier | Color |
|---------|-------|
| Airtel | 🔴 Red |
| Jio | 🔵 Blue |
| Vi (Vodafone-Idea) | 🟣 Purple |
| BSNL | 🟢 Green |

---

## 📦 Requirements

```
Python 3.x only
Zero extra packages
Works offline (carrier/country detection)
Internet needed for spam check links only
```

---

## 🔄 Changelog

### v2.0
- 6 tools (was 3)
- Number Formatter (new)
- Spam Check Links (new)
- India Carrier standalone (new)
- Bulk stats summary
- More carriers (150+ prefixes)
- More states coverage
- Carrier color coding

### v1.0
- Initial release with 3 tools

---

## ⚠️ Disclaimer

> For **educational use only**.
> Do not use to stalk or harass individuals.
> Use ethically and responsibly.

---

## 👤 Created by

**Sachin Ser** | [HackPath](https://github.com/sachin-null)

- GitHub: [@sachin-null](https://github.com/sachin-null)
- Instagram: [@sachin_ser](https://instagram.com/sachin_ser)

---

## 🔗 More HackPath Tools

| Tool | Repo |
|------|------|
| 🔓 CTF Helper v2 | [hackpath-ctf-helper](https://github.com/sachin-null/hackpath-ctf-helper) |
| 🔐 PassGen v2 | [hackpath-passgen](https://github.com/sachin-null/hackpath-passgen) |
| 📋 Wordlist Maker v2 | [hackpath-wordlist-maker](https://github.com/sachin-null/hackpath-wordlist-maker) |
| 🌐 OSINT Tool | [hackpath-osint](https://github.com/sachin-null/hackpath-osint) |

---

<div align="center">

**Star this repo if it helped you!**

`Made with love by Sachin Ser | HackPath`

</div>
