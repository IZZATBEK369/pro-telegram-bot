import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import BOT_TOKEN, ADMIN_ID
from keyboards import main_menu, phone_menu, cancel_menu, portfolio_inline
from states import OrderState

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        f"Assalomu alaykum, <b>{message.from_user.full_name}</b>! 👋\n\n"
        "Men <b>Izzatbek Shokirjonovning</b> rasmiy IT-asistent botiman.\n"
        "Quyidagi menyu orqali xizmatlarim bilan tanishishingiz yoki loyiha buyurtma qilishingiz mumkin:",
        reply_markup=main_menu,
    )


@dp.message(F.text == "❌ Bekor qilish")
async def cancel_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Amal bekor qilindi. Asosiy menyudasiz:",
        reply_markup=main_menu,
    )


@dp.message(F.text == "🚀 Xizmatlar va narxlar")
async def services_handler(message: Message):
    text = (
        "<b>🛠 Mening IT xizmatlarim:</b>\n\n"
        "1️⃣ <b>Landing Page (Vizitka sayt)</b>\n"
        "• Zamonaviy dizayn, mobil moslashuvchanlik (HTML/CSS)\n"
        "• Muddati: 1–3 kun\n\n"
        "2️⃣ <b>Telegram Bot yaratish</b>\n"
        "• Buyurtma qabul qiluvchi, ma'lumot beruvchi yoki avtomatlashtirilgan botlar (Python / Aiogram 3)\n"
        "• Muddati: 2–5 kun\n\n"
        "3️⃣ <b>Python skriptlar va avtomatlashtirish</b>\n"
        "• Turli vazifalarni avtomatlashtiruvchi maxsus dasturlar\n\n"
        "💡 <i>Aniq narx va muddatni kelishish uchun <b>«📝 Buyurtma berish»</b> tugmasini bosing.</i>"
    )
    await message.answer(text)


@dp.message(F.text == "💼 Portfolio")
async def portfolio_handler(message: Message):
    await message.answer(
        "<b>💼 Mening ishlarim va profillarim:</b>\n\n"
        "Quyidagi tugmalar orqali shaxsiy veb-saytim hamda GitHub sahifamdagi loyihalarimni ko'rishingiz mumkin:",
        reply_markup=portfolio_inline,
    )


@dp.message(F.text == "📞 Bog'lanish")
async def contact_handler(message: Message):
    await message.answer(
        "<b>📞 Bog'lanish uchun ma'lumotlar:</b>\n\n"
        "👨‍💻 <b>Dasturchi:</b> Izzatbek Shokirjonov\n"
        "📧 <b>Email:</b> izzatbeks458@gmail.com\n"
        "📍 <b>Manzil:</b> Toshkent, O'zbekiston\n\n"
        "Tezkor aloqa uchun <b>«📝 Buyurtma berish»</b> bo'limidan so'rov qoldiring, o'zim aloqaga chiqaman!"
    )


@dp.message(F.text == "📝 Buyurtma berish")
async def order_start(message: Message, state: FSMContext):
    await state.set_state(OrderState.name)
    await message.answer(
        "📝 <b>Yangi buyurtma rasmiylashtirish</b>\n\n"
        "1-qadam: Ismingizni kiriting:",
        reply_markup=cancel_menu,
    )


@dp.message(OrderState.name)
async def order_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(OrderState.phone)
    await message.answer(
        "2-qadam: Bog'lanish uchun telefon raqamingizni yozing yoki pastdagi tugmani bosing:",
        reply_markup=phone_menu,
    )


@dp.message(OrderState.phone)
async def order_phone(message: Message, state: FSMContext):
    phone = message.contact.phone_number if message.contact else message.text
    await state.update_data(phone=phone)
    await state.set_state(OrderState.description)
    await message.answer(
        "3-qadam: Qanday veb-sayt yoki Telegram bot kerakligini qisqacha yozib bering:",
        reply_markup=cancel_menu,
    )


@dp.message(OrderState.description)
async def order_description(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    name = data.get("name")
    phone = data.get("phone")
    description = message.text
    username = f"@{message.from_user.username}" if message.from_user.username else "Mavjud emas"

    admin_text = (
        "🔔 <b>YANGI BUYURTMA KELDI!</b>\n\n"
        f"👤 <b>Mijoz:</b> {name}\n"
        f"📱 <b>Telefon:</b> {phone}\n"
        f"🔗 <b>Telegram:</b> {username} (ID: <code>{message.from_user.id}</code>)\n"
        f"📋 <b>Loyiha haqida:</b>\n{description}"
    )

    await bot.send_message(chat_id=ADMIN_ID, text=admin_text)
    await state.clear()
    await message.answer(
        "✅ <b>Buyurtmangiz muvaffaqiyatli qabul qilindi!</b>\n\n"
        "Ma'lumotlar adminga yuborildi. Tez orada siz bilan bog'lanamiz!",
        reply_markup=main_menu,
    )


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())