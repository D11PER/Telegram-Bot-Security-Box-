# Telegram Password Generator Bot 🔐

A simple yet effective Telegram bot built with `pyTelegramBotAPI` that generates secure, random passwords for various platforms.

## 🚀 Evolution: What's New?

I have recently updated the bot to improve User Experience (UX) and provide more customization.

### New Version (v2.0) - *Latest Update*
* **User-Controlled Length:** Instead of random length, users can now specifically choose between 7, 8, 9, or 10 characters.
* **Advanced Navigation:** Improved `ReplyKeyboardMarkup` menus for a smoother flow.
* **New Commands:** Added `/length` command for quick access to password settings.
* **Optimized Logic:** Refined message handlers to support a step-by-step selection process.

### Old Version (v1.0)
* Generated passwords based on a fixed random range (e.g., 7-12 characters).
* Basic interaction: Only two buttons (Telegram/Gmail) with immediate results.

---

## 🛠 Features
* **Instant Generation:** Get a password in two clicks.
* **Diverse Character Set:** Includes lowercase letters, numbers, and special symbols (`@`, `#`, `%`, `$`, `!`).
* **Platform Specific:** Logic separates requests for Telegram and Gmail passwords.

## 💻 Tech Stack
* **Language:** Python 3.x
* **Library:** [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
* **Randomization:** Python `random` module

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bashFeature,v1.0 (Basic),v2.0 (Interactive),v3.0 (Professional)
User Control,Fixed Randomness,Choice via Buttons,Dynamic Selection
Length Logic,"random.randint(7,12)",Hardcoded if/elif,Loops & Lists (Scalable)
UX / Design,Plain Text,Basic Buttons,Markdown (Click-to-Copy)
Code Quality,Repetitive,Structured,DRY (Clean & Modular)
Commands,/start,"/start, /length",Universal Handler
