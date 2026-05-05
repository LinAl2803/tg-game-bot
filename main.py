import asyncio
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

# ⚠️ Твой токен
TOKEN = "7970297730:AAGELamWJDkxSxZ80GtbyWUndWin541g4Fg"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⚔️ Атаковать дракона", callback_data="attack")],
        [InlineKeyboardButton(text="🏃 Убежать", callback_data="run")]
    ])
    await message.answer(
        "👋 Привет, герой! Ты стоишь перед пещерой дракона.\nЧто будешь делать?",
        reply_markup=keyboard
    )

@dp.callback_query(F.data == "attack")
async def process_attack(callback: CallbackQuery):
    await callback.answer()
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Начать заново", callback_data="restart")]
    ])
    await callback.message.edit_text(
        "🐉 Ты храбро атаковал! Но дракон оказался сильнее...\nТы проиграл.",
        reply_markup=keyboard
    )

@dp.callback_query(F.data == "run")
async def process_run(callback: CallbackQuery):
    await callback.answer()
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Начать заново", callback_data="restart")]
    ])
    await callback.message.edit_text(
        "💨 Ты быстро убежал и спас свою жизнь!\nПобеда (трусливая, но победа).",
        reply_markup=keyboard
    )

@dp.callback_query(F.data == "restart")
async def process_restart(callback: CallbackQuery):
    await callback.answer()
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⚔️ Атаковать дракона", callback_data="attack")],
        [InlineKeyboardButton(text="🏃 Убежать", callback_data="run")]
    ])
    await callback.message.edit_text(
        "👋 Привет, герой! Ты стоишь перед пещерой дракона.\nЧто будешь делать?",
        reply_markup=keyboard
    )

async def main():
    print("✅ Бот запущен на сервере!", flush=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    # 🔧 Исправление: настройка только для Windows
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    asyncio.run(main())