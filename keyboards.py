from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

# Asosiy menyu tugmalari
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚀 Xizmatlar va narxlar"),
            KeyboardButton(text="💼 Portfolio"),
        ],
        [
            KeyboardButton(text="📝 Buyurtma berish"),
            KeyboardButton(text="📞 Bog'lanish"),
        ],
    ],
    resize_keyboard=True,
)

# Telefon raqamni yuborish tugmasi
phone_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)],
        [KeyboardButton(text="❌ Bekor qilish")],
    ],
    resize_keyboard=True,
)

# Jarayonni bekor qilish tugmasi
cancel_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="❌ Bekor qilish")],
    ],
    resize_keyboard=True,
)

# Portfolio uchun havola tugmalari
portfolio_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🌐 Neon Vizitka Saytim",
                url="https://izzatbek369.github.io/business-card/",
            )
        ],
        [
            InlineKeyboardButton(
                text="💻 GitHub Profilim",
                url="https://github.com/IZZATBEK369",
            )
        ],
    ]
)