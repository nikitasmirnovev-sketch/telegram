from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8218670396:AAG5YGxm8Ml9zGy_RGzYWR9FCrIxgmKXnuE"

# ---------- КНОПКИ ----------
menu_keyboard = ReplyKeyboardMarkup(
    [
        ["▶ Start"],
        ["ℹ Help"]
    ],
    resize_keyboard=True
)

# ---------- КОМАНДЫ ----------
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ Помощь:\n\n"
        "/start — запуск бота\n"
        "/help — описание команд\n"
        "/info — информация о боте\n"
        "Кнопки делают то же самое 👇",
        reply_markup=menu_keyboard
    )

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Команда /info\n"
        "Информация о боте - Создатель --> Никита Смирнов, в боте можно работать и  тд(еще не придумал что) , для чего создан бот? - (не придумал), удачного использывания!"
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Доступные команды:\n\n"
        "/start — показать команды\n"
        "/help — описание команд\n"
        "Или используй кнопки 👇",
        reply_markup=menu_keyboard
    )

# ---------- ОБРАБОТКА КНОПОК ----------
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "▶ Start":
        await start(update, context)
    elif text == "ℹ Help":
        await help_command(update, context)

# ---------- ЗАПУСК ----------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("info", info_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

print("✅ Бот запущен")
app.run_polling()