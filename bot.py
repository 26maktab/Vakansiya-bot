from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import asyncio

TOKEN = "8558760712:AAEhXc3bv1tIr4rsxuHjq2VepRR3Ozg5z64"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Jizzax tumanlari ---
districts = [
    "Jizzax shahri", "Arnasoy", "Baxmal", "Do‘stlik", "Forish",
    "G‘allaorol", "Sharof Rashidov", "Paxtakor", "Mirzacho‘l",
    "Zafarobod", "Zarbdor", "Yangiobod"
]

# --- Vakansiyalar (misol) ---
vakansiyalar = {
    "Jizzax shahri": ["🔹 Tarbiyachi – 12-DMTT", "🔹 Psixolog – 25-DMTT"],
    "Arnasoy": ["🔹 Tarbiyachi – 7-DMTT"],
    "Baxmal": ["🔹 Tarbiyachi – 14-DMTT", "🔹 Hamshira – 3-DMTT"],
    "Do‘stlik": ["🔹 Bo‘sh ish o‘rni yo‘q"],
    "Forish": ["🔹 Tarbiyachi – 5-DMTT"],
    "G‘allaorol": ["🔹 Tarbiyachi – 2-DMTT"],
    "Sharof Rashidov": ["🔹 Tarbiyachi – 18-DMTT"],
    "Paxtakor": ["🔹 Bo‘sh ish o‘rni yo‘q"],
    "Mirzacho‘l": ["🔹 Tarbiyachi – 6-DMTT"],
    "Zafarobod": ["🔹 Tarbiyachi – 4-DMTT"],
    "Zarbdor": ["🔹 Bo‘sh ish o‘rni yo‘q"],
    "Yangiobod": ["🔹 Tarbiyachi – 1-DMTT"]
}

# --- START komandasi ---
@dp.message(Command(commands=["start"]))
async def start(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=d)] for d in districts],
        resize_keyboard=True
    )
    await message.answer(
        "🟩 *Jizzax DMTT Vakansiya Botiga xush kelibsiz!*\n"
        "Viloyat tumani/shaharni tanlang:",
        reply_markup=kb,
        parse_mode="Markdown"
    )

# --- Tuman tanlanganda ---
@dp.message()
async def show_vacancies(message: types.Message):
    district = message.text
    if district in vakansiyalar:
        text = f"📌 *{district} bo‘yicha vakansiyalar:*\n\n"
        for v in vakansiyalar[district]:
            text += f"{v}\n"
        await message.answer(text, parse_mode="Markdown")
    else:
        await message.answer("❗ Tuman tanlanmadi. Iltimos menyudan tanlang.")

# --- Botni ishga tushirish ---
async def main():
    print("Bot ishga tushmoqda...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
