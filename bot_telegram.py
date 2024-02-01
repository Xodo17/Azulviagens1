from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Função para o comando /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Olá! Por favor, envie-me suas informações de pagamento.')

# Função para lidar com mensagens contendo informações de pagamento
def receive_payment_info(update: Update, context: CallbackContext) -> None:
    # Extrair as informações do usuário
    user_payment_info = update.message.text

    # Processar as informações de pagamento
    # Neste exemplo, apenas vamos confirmar que as informações foram recebidas
    update.message.reply_text('Informações de pagamento recebidas com sucesso! Obrigado.')

def main() -> None:
    # Token do bot do Telegram
    token = '6510838441:AAGYQdSpLKj4rInjwRtQNc_pYdYc7ImIW4c'

    # Criar o Updater e o Dispatcher
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    # Registrar os handlers
    start_handler = CommandHandler('start', start)
    receive_payment_info_handler = MessageHandler(Filters.text & (~Filters.command), receive_payment_info)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(receive_payment_info_handler)

    # Iniciar o bot
    updater.start_polling()
    updater.idle()

if name == '__main__':
    main()