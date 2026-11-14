# 🤖 IT-Asistent & Order Telegram Bot

**Aiogram 3** kutubxonasida modulli arxitektura asosida yaratilgan professional Telegram bot. Mijozlarga xizmatlar va portfolioni taqdim etish hamda FSM (Finite State Machine) orqali bosqichma-bosqich buyurtma qabul qilish uchun mo'ljallangan.

## ✨ Asosiy imkoniyatlar
- **Modulli arxitektura:** Kod toza va tushunarli qismlarga ajratilgan (`main.py`, `config.py`, `keyboards.py`, `states.py`).
- **Buyurtma qabul qilish (FSM):** Mijozdan ketma-ket ism, telefon raqam va loyiha tavsifini yig'adi.
- **Admin xabarnomasi:** Tayyor buyurtmani bir zumda adminning shaxsiy Telegramiga yuboradi.
- **Xavfsizlik:** Maxfiy token va ID ma'lumotlari `.env` fayli orqali himoyalangan.

## 🛠 Texnologiyalar
- Python 3.12
- Aiogram 3
- python-dotenv

## 🚀 Ishga tushirish
1. Repozitoriyni klonlang:
   `git clone https://github.com/IZZATBEK369/pro-telegram-bot.git`
2. Kerakli kutubxonalarni o'rnating:
   `pip install aiogram python-dotenv`
3. `.env` faylini yarating va o'z ma'lumotlaringizni kiriting:
   `BOT_TOKEN=your_bot_token`
   `ADMIN_ID=your_telegram_id`
4. Botni ishga tushiring:
   `python main.py`