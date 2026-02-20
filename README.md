# Holehe Email Checker – Wrapper Project

This project uses **Holehe** – a powerful email‑checking tool – to find out if an email is registered on 120+ websites and if it appears in known data breaches. Results are saved in the `records/` folder (ignored by Git).

## Features
- Leverages Holehe's reliable and up‑to‑date checks.
- Colourful terminal output with categories (REGISTERED / NOT REGISTERED / UNKNOWN).
- Data breach information included.
- Results saved as JSON with timestamps.

## Requirements
- Python 3.6+
- `colorama` library (for coloured output)
- **Holehe** installed on your system

## Setup

### 1. Install Holehe
Choose one of the following methods:

**On Kali / Debian / Ubuntu:**
```bash
sudo apt update
sudo apt install holehe
