import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes, ConversationHandler
)
from sqlalchemy import create_engine, text

DB_URL = "postgresql://postgres:tu_contraseña@localhost:5432/campana_db"
engine = create_engine(DB_URL)

TOKEN = "TU_TELEGRAM_BOT_TOKEN"
ESPERANDO_CEDULA = 1

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("?? Consultar Puesto por Cédula", callback_data='consultar')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "?? ¡Bienvenido al Sistema de Consulta Electoral!\n\nSeleccione una opción:",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'consultar':
        await query.edit_message_text(text="Ingrese su número de cédula (NUIP) sin puntos ni espacios:")
        return ESPERANDO_CEDULA

async def consultar_cedula_db(cedula: str):
    query = text("""
        SELECT cedula, municipio, departamento, puesto_nombre, direccion, mesa, estado, latitud, longitud
        FROM votantes 
        WHERE cedula = :ced
    """)
    with engine.connect() as conn:
        result = conn.execute(query, {"ced": cedula}).fetchone()
        return result

async def procesar_cedula(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cedula_txt = update.message.text.strip()

    if not cedula_txt.isdigit():
        await update.message.reply_text("?? Por favor ingrese solo números.")
        return ESPERANDO_CEDULA

    registro = await consultar_cedula_db(cedula_txt)

    if registro:
        google_maps_url = f"https://www.google.com/maps?q={registro.latitud},{registro.longitud}"
        
        respuesta = (
            f"?? *Puesto de Votación Encontrado*\n\n"
            f"• *Cédula:* {registro.cedula}\n"
            f"• *Puesto:* {registro.puesto_nombre}\n"
            f"• *Mesa:* {registro.mesa}\n"
            f"• *Dirección:* {registro.direccion}\n"
            f"• *Municipio:* {registro.municipio} ({registro.departamento})\n"
            f"• *Estado:* {registro.estado}\n\n"
            f"??? [Ver ubicación en Google Maps]({google_maps_url})"
        )
        
        keyboard = [
            [InlineKeyboardButton("??? Abrir en Google Maps", url=google_maps_url)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            respuesta, 
            parse_mode='Markdown', 
            reply_markup=reply_markup,
            disable_web_page_preview=False
        )
    else:
        respuesta = (
            f"? La cédula *{cedula_txt}* no se encuentra registrada en la base de datos."
        )
        await update.message.reply_text(respuesta, parse_mode='Markdown')

    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Operación cancelada. Use /start para reiniciar.")
    return ConversationHandler.END

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(button_handler)],
        states={
            ESPERANDO_CEDULA: [MessageHandler(filters.TEXT & ~filters.COMMAND, procesar_cedula)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    app.add_handler(CommandHandler('start', start))
    app.add_handler(conv_handler)

    print("Bot en marcha...")
    app.run_polling()
