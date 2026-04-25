## Password-Gen-Showcase in Telegram 🤖
Telegram Bot: @passwriter_bot

## Telegram Password Generator Bot 🔐
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

## 📊 Project Evolution: Version Comparison

| Feature | v1.0 (Basic/Old) | v2.0 (Interactive/New) |
| :--- | :--- | :--- |
| User Control | Fixed Randomness | Choice via Buttons |
| Length Logic | random.randint(7,12) | Hardcoded if/elif |
| UX / Design | Plain Text | Basic Buttons |
| Code Quality | Repetitive | Structured |
| Commands | /start | /start, /length |

## 🎯 Roadmap & Future Improvements

I'm constantly working to make this bot better. Here is what's coming next:

### 🚀 Roadmap / Future Updates

| Status | Feature | Description | Progress |
| :--- | :--- | :--- | :---: |
| ⏳ Planned | Strength Meter | Analyze how secure the generated password is. | [20%] |
| ⏳ Planned | Multi-Language Support | Support for 🇺🇦 Ukrainian, 🇩🇪 German and other languages. | [50%] |
